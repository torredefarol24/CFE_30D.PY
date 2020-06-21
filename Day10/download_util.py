import requests
import shutil
import os

def download_file(url, directory):
	DL_FILENAME = os.path.basename(url)
	NEW_DLED_PATH = os.path.join(directory, DL_FILENAME)

	with requests.get(url, stream=True) as r:
		with open(NEW_DLED_PATH, "wb") as f:
			shutil.copyfileobj(r.raw, f)
	
	return NEW_DLED_PATH
