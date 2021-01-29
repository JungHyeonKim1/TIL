import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    maker = URLMaker('fd49f4647840fb448f1f847df0bd624f')
    url = maker.get_url('movie', 'popular', region='KR', language='ko')
    res = requests.get(url)
    movie_dict = res.json()

    movie_list = movie_dict.get('results')

    result = []
    for movie in movie_list:
        a = movie.get('vote_average')
        if a >= 8:
            result.append(movie)
    return result


if __name__ == '__main__':
    pprint(vote_average_movies())    
