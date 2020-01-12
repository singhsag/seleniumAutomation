import inspect
import logging


def customLogger(log_level=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    # Ger Logger
    logger = logging.getLogger(logger_name)
    logger.setLevel("DEBUG")

    # Get Handler
    file_handler = logging.FileHandler("automation.log", mode='w')
    file_handler.setLevel(log_level)

    # Set Formatter
    formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s",
                                  datefmt="%m/%d/%Y %H:%M:%S")
    file_handler.setFormatter(formatter)

    # Add to file to logger handler
    logger.addHandler(file_handler)
    return logger
