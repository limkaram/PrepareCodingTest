import itertools

def solution(clothes):
    answer = 0
    clothes_dict = {}
    all_clothes = 0
    temp = 1

    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]].append(cloth[0])
        elif cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = [cloth[0]]

    clothes_count_list = list(map(lambda x: len(x), clothes_dict.values()))
    for i in range(1, len(clothes_dict)+1):
        for cloth in clothes_dict.values():
            answer += len(itertools.combinations(cloth, 1))




    # # 1개의 의상만 입을 경우
    # for value in clothes_dict.values():
    #     answer += len(value)
    #
    # # 2개 이상의 의상을 골라 입는 경우
    # if len(clothes_dict) >= 2:
    #     for value in clothes_dict.values():
    #         temp *= len(value)
    #     answer += temp
    # print(answer)
    # for _, value in clothes_dict.items():
    #     all_clothes += len(value)
    #     if len(clothes_dict.keys()) > 1:
    #         multi_clothes *= len(value)
    #
    # if multi_clothes > 1:
    #     answer = all_clothes + multi_clothes
    # elif multi_clothes == 1:
    #     answer = all_clothes
    # return answer


if __name__ == '__main__':
    # clothes = [['yellow_hat', 'headgear'],
    #            ['blue_sunglasses', 'eyewear'],
    #            ['green_turban', 'headgear']]

    # clothes = [['crow_mask', 'face'],
    #            ['blue_sunglasses', 'face'],
    #            ['smoky_makeup', 'face']]

    clothes = [['yellow_hat', 'headgear'],
               ['blue_sunglasses', 'eyewear'],
               ['green_turban', 'headgear'],
               ['crow_mask', 'face']]
    solution(clothes)