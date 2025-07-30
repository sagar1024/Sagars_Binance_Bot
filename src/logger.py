# import logging
# import os
# from datetime import datetime

# log_dir = "logs"
# os.makedirs(log_dir, exist_ok=True)

# log_file = os.path.join(log_dir, f"bot_{datetime.now().strftime('%Y%m%d')}.log")

# logging.basicConfig(
#     filename=log_file,
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# def log_info(message):
#     print(f"[INFO] {message}")
#     logging.info(message)

# def log_error(message):
#     print(f"[ERROR] {message}")
#     logging.error(message)

import logging

def setup_logger():
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = setup_logger()
