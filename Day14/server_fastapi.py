from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save

app = FastAPI()

@app.get("/fastapi")
def hello_world():
	return {"hello" : "world"}

@app.post("/scraper")
def scraper():
	trigger_log_save()
	scrape_runner()
	return {"message" : "Done"}