import requests 

ngrok_url = 'http://a27dbc70.ngrok.io'
endpoint = f'{ngrok_url}/scraper'

r = requests.post(endpoint, json={})
print(r.json())