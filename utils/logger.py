import logging
import sys
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter


LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "movies.log"

FILE_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

COLOR_FORMAT = (
    "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
COLOR_FORMATTER = ColoredFormatter(
    COLOR_FORMAT,
    datefmt=DATE_FORMAT,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

file_handler = TimedRotatingFileHandler(
    filename=LOG_FILE,
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)
file_handler.setFormatter(logging.Formatter(FILE_LOG_FORMAT, datefmt=DATE_FORMAT))


stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(COLOR_FORMATTER)

logger = logging.getLogger("movies")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.propagate = True
# logger.propagate = False

