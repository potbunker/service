import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format='%(asctime)s %(levelname)s %(process)d %(thread)d %(module)s %(funcName)s [%(filename)s:%(lineno)d] %(message)s'
)