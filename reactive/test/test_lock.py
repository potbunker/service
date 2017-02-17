import pytest
import logging
import os
from rx import Observable
from reactive.lock import LockFile


logger = logging.getLogger(__name__)


def test_file_lock():

    def lock_and_release(file_name):
        acquired = False
        with LockFile(file_name) as lock:
            acquired = lock.acquired
            logger.info(acquired)
        assert not acquired or not os.path.isfile(file_name)

    Observable.interval(130).map(lambda x: lock_and_release('/tmp/aaaa')).subscribe(logger.info)
    Observable.interval(105).map(lambda x: lock_and_release('/tmp/aaaa')).subscribe(logger.info)

    import time
    time.sleep(10)
