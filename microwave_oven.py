# 문제출처 : 백준 온라인 저지
# 문제유형 : 그리디
# 문제번호 : 10162번
# 문제명 : 전자레인지

def solution(T):
    bottons = {'A': 300,
              'B':60,
              'C':10}

    total_click_count = []

    for botton in bottons:
        click_count = T // bottons[botton]
        total_click_count.append(click_count)
        T %= bottons[botton]
        if len(total_click_count) == 3 and T != 0:
            return -1
    return total_click_count


if __name__ == '__main__':
    T = int(input())
    result = solution(T)
    if result != -1:
        for count in result:
            print(count, end=' ')
    elif result == -1:
        print(result)