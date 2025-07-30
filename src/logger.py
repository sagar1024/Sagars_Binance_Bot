# import logging

# def get_logger(name="bot"):
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#     fh = logging.FileHandler("bot.log")
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     fh.setFormatter(formatter)
#     if not logger.handlers:
#         logger.addHandler(fh)
#     return logger

import logging

def get_logger():
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler("bot.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
