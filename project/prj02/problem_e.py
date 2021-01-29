import requests
from tmdb import URLMaker
from pprint import pprint


def credits(title):
    maker = URLMaker('fd49f4647840fb448f1f847df0bd624f')
    
    id = maker.movie_id(title)
    if not id:
        return None

    ad_url = maker.get_url(region='KR', language='ko', feature = f'{id}/credits')
    ad_list = requests.get(ad_url).json()
    print(ad_url)

    act_list = []
    dir_list = []
    a = len(ad_list['cast'])
    b = len(ad_list['crew'])
    for num in range(0, a):
        c = ad_list['cast'][num]['cast_id']
        if c < 10:
            act_list.append(ad_list['cast'][num]['name'])
    for num in range(0, b):
        d = ad_list['crew'][num]['known_for_department']
        if d == 'Directing':
            if not ad_list['crew'][num]['name'] in dir_list:
                dir_list.append(ad_list['crew'][num]['name']) 

    result = {}
    result['cast'] = act_list
    result['crew'] = dir_list

    return result


if __name__ == '__main__':
    # id 기준 주연배우 감독 출력
    pprint(credits('기생충'))
    # => 
    # {
    #     'cast': [
    #         'Song Kang-ho',
    #         'Lee Sun-kyun',
    #         'Cho Yeo-jeong',
    #         'Choi Woo-shik',
    #         'Park So-dam',
    #         'Lee Jung-eun',
    #         'Chang Hyae-jin'
    #     ],
    #      'crew': [
    #         'Bong Joon-ho',
    #         'Han Jin-won',
    #         'Kim Seong-sik',
    #         'Lee Jung-hoon',
    #         'Park Hyun-cheol',
    #         'Yoon Young-woo'
    #     ]
    # } 
    pprint(credits('id없는 영화'))
    # => None