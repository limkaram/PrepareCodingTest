# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 구현
# 문제번호 : 예제 4-1
# 문제명 : 상하좌우

N = int(input())

movement = input().split()

i, j = 1, 1


for move in movement:
    if move == 'U':
        if (i - 1) <= 0:
            pass
        elif (i - 1) > 0:
            i -= 1
    elif move == 'D':
        if (i + 1) > N:
            pass
        elif (i + 1) <= N:
            i += 1
    elif move == 'L':
        if (j - 1) <= 0:
            pass
        elif (j - 1) > 0:
            j -= 1
    elif move == 'R':
        if (j + 1) > N:
            pass
        elif (j + 1) <= N:
            j += 1

print(i, j)

