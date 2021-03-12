import requests
import random
from django.shortcuts import render

def lotto(request):
    # 로또 정보 받아 오기
    url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    res = requests.get(url).json()

    # 번호 가져오기
    bonus = res['bnusNo']
    winner = []
    for idx in range(1, 7):
        winner.append(res[f'drwtNo{idx}'])
    
    # 당첨 횟수를 저장하기 위한 dictionary 만들기
    win_rate = {
        '1': 0, '2': 0, '3': 0,
        '4': 0, '5': 0, '6' : 0,
    }

    # 1000 번 반복을 통해서 당첨번호와 비교하기
    for _ in range(1000):
        my_numbers = random.sample(range(1, 46), 6)

        # 랜덤으로 생성된 번호와 당첨번호 비교
        matched = 0
        for num in my_numbers:
            if num in winner:
                matched += 1
        
        # 교집합으로 비교도 가능
        # matched = len(set(winner) & set(my_numbers))

        # 당첨 횟수 체크
        if matched == 6:
            win_rate['1'] += 1
        elif matched == 5 and bonus in my_numbers:
            win_rate['2'] += 1
        elif matched == 5:
            win_rate['3'] += 1
        elif matched == 4:
            win_rate['4'] += 1
        elif matched == 3:
            win_rate['5'] += 1
        else:
            win_rate['6'] += 1

    # html 에 보여주기 위해 context 에 담기
    context = {
        'winner': winner, 
        'bonus': bonus,
        'win_rate': win_rate
    }

    return render(request, 'pages/lotto.html', context)