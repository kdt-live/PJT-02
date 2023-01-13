import requests
from pprint import pprint
url = "https://api.themoviedb.org/3/movie/popular?api_key=1408bd2d08a0c61ad1492eca9e590bc3&language=en-US"
response = requests.get(url).json()
data = response['results']
dic1 = {}
x=sorted(response['results'] , key= lambda y: y['vote_average'], reverse=True)
pprint(x[:5])