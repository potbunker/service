import pytest


def test_constructor():
    from ..request_processor import RequestProcessor
    processor = RequestProcessor()
    processor.findEntityById(11, 2)
    print processor