from abc import abstractmethod
from rx import Observable as O
from time import time
import logging
logger = logging.getLogger(__name__)


def log_time_it(start, end):
    logger.info(end - start)


def handle_error(context, error):
    logger.exception(error)
    context.deliver(error)


class EndPointBase(object):

    @abstractmethod
    def _execute(self, request):
        pass

    def _check_access(self, context):
        pass

    def execute(self, context, request):
        start = time()
        O.just(context)\
            .do_action(self._check_access)\
            .select(lambda x: x.makeResponse())\
            .zip(O.just(request).select(lambda q: q._toPy()).select(self._execute),
                 lambda response, result: setattr(response, __name__, result))\
            .do_action(lambda r: context.deliver(r)) \
            .finally_action(lambda: log_time_it(start, time()))\
            .subscribe(
                context.deliver,
                handle_error
            )
