import os
import sys
import time
import logging
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

logfile_path = os.path.join(BASE_DIR, "logfiles")
if not os.path.exists(logfile_path):
    os.mkdir(logfile_path)

formatter = logging.Formatter(fmt='[%(levelname)s] [%(asctime)s] %(message)s', datefmt='%Y_%m_%d %H:%M:%S')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
batch_handler = logging.FileHandler(os.path.join(logfile_path, f"{time.strftime('%Y_%m_%d')}.log"))
batch_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(batch_handler)
logger.addHandler(stream_handler)

