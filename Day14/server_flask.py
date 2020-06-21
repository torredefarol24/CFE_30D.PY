from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save

app = Flask(__name__)

@app.route("/flask", methods=["GET"])
def hello():
	return """
		<html>
			<h1>Hey, This is Flask</h1>
		</html>
	"""

@app.route('/scrape', methods=['POST'])
def scraper_view():
	trigger_log_save()
	scrape_runner()
	return "Done HAHA"