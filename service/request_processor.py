from functools import wraps


def add_endpoints(dir):
    import os
    os.listdir(dir)


class RequestProcessorMeta(type):

    def __new__(cls, *args, **kwargs):
        from types import MethodType
        from endpoints.findEntityById import EndPoint as findEntityById
        unbound = findEntityById.execute
        cls.findEntityById = unbound
        return super(RequestProcessorMeta, cls).__new__(cls, *args, **kwargs)

class RequestProcessor(object):
    __metaclass__ = RequestProcessorMeta

    def __init__(self):
        pass