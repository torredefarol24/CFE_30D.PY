import os

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

FILE_SAVE_DIR = os.path.join(BASE_DIR, "images")

# if not os.path.exists(FILE_SAVE_DIR):
# 	print("INVALID PATH")

os.makedirs(FILE_SAVE_DIR, exist_ok=True)

my_images = range(0,10)

for i in my_images:
	fname = f"Image{i}.txt"
	file_path = os.path.join(FILE_SAVE_DIR, fname)
	if os.path.exists(file_path):
		print(f"skipped fname")
		continue
	with open(file_path, "w") as f:
		f.write("Hey There Hey World")
