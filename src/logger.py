import logging

logger = logging.getLogger("BinanceBot")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("bot.log")
file_handler.setFormatter(formatter)

# Avoid duplicate handlers if re-imported
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
