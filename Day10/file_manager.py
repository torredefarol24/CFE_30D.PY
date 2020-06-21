import os

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
# ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)


# email_text = "templates/email.txt"
# email_text = os.path.join("templates", "email.txt")
email_text = os.path.join(BASE_DIR, "templates", "email.txt")
context = ""

with open(email_text, "r") as f:
	context = f.read()

print(context.format(name="Tom"))