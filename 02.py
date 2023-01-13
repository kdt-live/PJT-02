import requests
from pprint import pprint
url = "https://api.themoviedb.org/3/movie/popular?api_key=1408bd2d08a0c61ad1492eca9e590bc3&language=en-US"
response = requests.get(url).json()
for i in range(len(response['results'])):
  if response['results'][i]['vote_average'] >= 8:
    print(response['results'][i])
