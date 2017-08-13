from ..abstract import EndPointBase
from rx import Observable as O

class EndPoint(EndPointBase):

    def _execute(self, request):
        return