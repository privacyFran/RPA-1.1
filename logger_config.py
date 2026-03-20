import logging
import os
import sys

def setup_logger():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "robot.log")

    logger = logging.getLogger("RPA_Bot")
    logger.setLevel(logging.INFO)

    log_format = "%(asctime)s %(levelname)s %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(log_format, datefmt=date_format)

    # Console Handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    # File Handler
    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    # Add handlers if not already added
    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger

logger = setup_logger()
