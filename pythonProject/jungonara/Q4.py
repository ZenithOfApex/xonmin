# 유저가 달성한 점수(score)에 따라 실시간 랭킹을 보여주는 랭킹 페이지가 있습니다. 랭킹 페이지는 한 페이지에 K명씩 닉네임을 보여주며, 랭킹이 산정되는 규칙은 다음과 같습니다.
#
# 점수가 높은 유저의 랭킹이 더 높습니다.
# 점수가 같다면 해당 점수를 먼저 달성한 유저의 랭킹이 높습니다.
# 어떤 유저가 이전 기록보다 더 높은 점수를 달성하면, 이전 기록은 사라지고 새로운 기록이 랭킹에 반영됩니다.
# 어떤 유저가 이전 기록보다 더 낮거나 같은 점수를 달성했다면 이 기록은 무시합니다.
# 시즌이 바뀌면서 랭킹이 초기화되어 랭킹 페이지가 비어있는 상태가 됐습니다. 이때, 각 유저의 닉네임과 점수가 해당 점수를 달성한 순서대로 주어지면, 1페이지는 몇 번 바뀌는지 알아보려 합니다. 단, 랭킹 페이지에는 유저 닉네임만 표시되므로 점수 변화가 있더라도 랭킹에 변화가 없다면 랭킹 페이지는 바뀌지 않습니다.
#
# 한 페이지에 표시되는 닉네임 수 K, 유저의 닉네임과 점수가 달성 순서대로 들어있는 배열 user_scores가 매개변수로 주어질 때, 랭킹 1페이지는 몇 번 바뀌는지 return 하도록 solution 함수를 완성해주세요.
#
# K는 1 이상 100 이하인 자연수입니다.
# user_scores의 길이는 1 이상 1,000 이하입니다.
# user_scores의 각 원소는 유저 닉네임과 해당 유저가 달성한 점수로 이루어진 문자열입니다.
# 유저 닉네임과 달성 점수는 "닉네임 점수" 형태의 문자열로 주어집니다.
# 닉네임과 점수는 공백(스페이스 바) 한 개로 구분되어 주어집니다.
# 닉네임은 알파벳 소문자와 숫자로만 이루어져 있으며, 길이는 1 이상 10 이하입니다.
# 점수는 숫자로만 이루어져 있으며, 길이는 1 이상 9 이하이고 0으로 시작하지 않습니다.
# 모든 유저는 닉네임 하나만 사용하며, 서로 다른 유저의 닉네임이 같은 경우는 없습니다.
# user_scores의 원소는 각 유저가 해당 점수를 달성한 순서대로 들어있습니다.
# 따라서 같은 점수를 동시에 달성한 유저는 없다고 가정해도 좋습니다.


import copy
from collections import OrderedDict

def solution(K, user_scores):
    count = 0

    # 점수 갱신 확인
    score_dict = OrderedDict()


    # 첫 페이지 채우기
    rank = []
    for i in range(K):

        origin_page = rank
        name, score = user_scores[i].split()

        if name in score_dict:
            before = score_dict.get(name)
            if int(before) <= int(score):  # 4번 규칙
                score_dict[name] = score
            else:
                continue
        else:
            score_dict[name] = score

        ranking_page = sorted(score_dict.items(), key=lambda x: (x[1],x), reverse=True)
        rank = [i[0] for i in ranking_page]
        rank = rank[:K]

        if origin_page != rank:
            count += 1

        print(ranking_page)

    print()
    user_scores = user_scores[K:]

    for data in user_scores:
        origin_page = rank

        name, score = data.split()

        # 점수가 더 높은지 확인
        if name in score_dict:
            before = score_dict.get(name)
            if int(before) <= int(score):  # 4번 규칙
                score_dict[name] = score
            else:
                continue
        else:
            score_dict[name] = score

        ranking_page = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
        rank = [i[0] for i in ranking_page]
        rank = rank[:K]

        print(origin_page)

        print(rank)
        print()
        if origin_page != rank:
            count += 1

    return count

print(solution(3, ["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"]))

print(solution(3, ["alex111 100", "cheries2 200", "alex111 200", "cheries2 150", "coco 50", "coco 200"]))
