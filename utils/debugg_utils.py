import time
from utils.logger_utils import build_logger

logger = build_logger(__name__)


def process_time_wrapper(func):
    """"""
    def process_time(*args, **kwrags):
        """"""
        t1 = time.time()
        result = func(*args, **kwrags)
        logger.info(f"The method took: {time.time() - t1}s")
        return result
    return process_time