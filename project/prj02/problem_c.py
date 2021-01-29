import requests
from tmdb import URLMaker
from pprint import pprint
from operator import itemgetter, attrgetter


def ranking():
    maker = URLMaker('fd49f4647840fb448f1f847df0bd624f')
    url = maker.get_url('movie', 'popular', region='KR', language='ko')
    res = requests.get(url)
    movie_dict = res.json()

    movie_list = movie_dict.get('results')
    
    result = []
    a = sorted(movie_list, key=itemgetter('vote_average'), reverse=True)
    result.append(a[0:5])

    return result


if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())