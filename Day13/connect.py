import requests
import pprint
import pandas


# VERSION 3
api_key = "6ae52c897737367d57795a8131264911"
sig = f"api_key={api_key}"

movie_id = 550
# endpoint_path = f"movie/{movie_id}"
endpoint_path = "search/movie"


api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"

qval = "The Matrix"
query = f"query=${qval}"

endpoint = f"{api_base_url}/{endpoint_path}?{sig}&{query}"

r = requests.get(endpoint)
# pprint.pprint(r.json())


if r.status_code in range(200,299):
	data = r.json()
	results = data['results']
	
	if len(results) > 0:
		movie_ids = set()
		for result in results:
			_id = result["id"]
			print(result["title"], "->", _id)
			movie_ids.add(_id)
		
		# print("MovieIds", list(movie_ids))


output_file = "movies.csv"
movie_data = []

api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"


for movie_id in movie_ids:
	endpoint_path = f"/movie/{movie_id}"
	endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
	
	r = requests.get(endpoint)
	
	if r.status_code in range(200, 299):
		data = r.json()
		movie_data.append(data)



data_frame = pandas.DataFrame(movie_data)
print(data_frame.head())
data_frame.to_csv(output_file, index=False)

################################################
# VERSION 4
################################################

# api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YWU1MmM4OTc3MzczNjdkNTc3OTVhODEzMTI2NDkxMSIsInN1YiI6IjVlYTEzZDMxZWEzN2UwMDAxYzI4M2E4YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mER6N6sUI8dw1pjhctavO0e4fPAbk-DTMa-rUsJlum8"


# movie_id = 550
# endpoint_path = f"movie/{movie_id}"

# api_version = 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"

# headers = {
# 	"Authorization": f"Bearer {api_token}",
# 	"Content-Type" : "application/json"
# }


# endpoint = f"{api_base_url}/{endpoint_path}"

# r = requests.get(endpoint, headers = headers)
# print(r.status_code, r.text)
