import logging

def get_logger():
    logger = logging.getLogger("test_log")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

logger = get_logger()