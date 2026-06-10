import logging
from logging import Logger


def get_logger(name: str) -> Logger:
    logger = logging.getLogger(name=name)
    logger.setLevel("DEBUG")

    handler = logging.StreamHandler()
    handler.setLevel("DEBUG")

    formatter = logging.Formatter("%(asctime)s || %(name)s || %(levelname)s || %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
