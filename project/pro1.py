from tmdb import URLMaker
import requests
from pprint import pprint

def top_rated_movie():
    maker = URLMaker('key 값')
    url = maker.get_url('movie', 'top_rated', region=, language=,)
    res = requests.get(url)
    movie_dict = res.json()

    movie_list = movie_dict.get('results')

    result = []
    for movie in movie_list:
        result.append(movie.get('title'))
    return result

top_rated_movie()