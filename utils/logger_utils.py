import logging
import sys


def build_logger(name):
    """
    Function to config a normal logger
    :param name: name of the source of the logger
    :return:
    """
    logger = logging.getLogger(name)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    return logger