import requests
from tmdb import URLMaker
from pprint import pprint


def popular_count():
    maker = URLMaker('fd49f4647840fb448f1f847df0bd624f')
    url = maker.get_url('movie', 'popular', region='KR', language='ko')
    res = requests.get(url)
    movie_dict = res.json()

    movie_list = movie_dict.get('results')

    result = 0
    for movie in movie_list:
        result += 1
    return result


if __name__ == '__main__':
    pprint(popular_count())