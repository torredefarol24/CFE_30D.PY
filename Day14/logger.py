import os
import datetime

BASE_DIR = os.path.dirname(__file__)
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

def trigger_log_save():
	filename = f"{datetime.datetime.now()}.txt"
	filepath = os.path.join(LOG_DIR, filename)

	with open(filepath, "w+") as f:
		f.write("")