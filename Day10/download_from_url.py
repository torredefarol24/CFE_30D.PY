from download_util import download_file
import os
import requests

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
DLED_IMGPATH = os.path.join(DOWNLOAD_DIR, "1.jpg")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

image_url1 = "https://media.wired.com/photos/5d09594a62bcb0c9752779d9/4:3/w_2000,h_1500,c_limit/Transpo_G70_TA-518126.jpg"
DL_FILENAME = os.path.basename(image_url1)
NEW_DLED_PATH = os.path.join(DOWNLOAD_DIR, DL_FILENAME)

# r = requests.get(image_url1, stream = True)
# with open(DLED_IMGPATH, "wb") as f:
# 	f.write(r.content)


download_file(image_url1, DOWNLOAD_DIR)
