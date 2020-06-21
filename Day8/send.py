import requests
import sys

from formatting import format_msg
from datetime import datetime

def send(name, website=None, verbose=True):
	if website != None:
		msg = format_msg(name, website)
	else: 
		msg = format_msg(name)
		
	
	if verbose == True:
		print(name, website)

	r = requests.get("http://httpbin.org/json")
	if r.status_code == 200:
		return r.json()
	else: 
		"There was an error"


if __name__ == "__main__":
	print(sys.argv)
	name = "Unknown"

	if len(sys.argv) > 1:
		name = sys.argv[1]

	response = send(name, verbose=True)
	print(response)