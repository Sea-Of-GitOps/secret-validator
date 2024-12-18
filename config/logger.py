import logging
import os

LOGGER = "secret-validator"


class CustomFormatter(logging.Formatter):
    def format(self, record):
        full_path = record.pathname
        relative_path = os.path.relpath(full_path, start=os.getcwd())
        record.relative_filename = relative_path
        return super().format(record)


def setup_logger():
    logger = logging.getLogger(LOGGER)
    logger.setLevel(logging.DEBUG)

    formatter = CustomFormatter(
        "%(asctime)s - %(relative_filename)s - %(funcName)s - "
        "%(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
