# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 구현
# 문제번호 : 실전 2
# 문제명 : 왕실의 나이트

plans = ['UUL', 'UUR', 'LLU', 'LLD', 'DDL', 'DDR', 'RRU', 'RRD']

columns = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7, 'h': 8}

rows = range(1, 9)

loc = input()
i, j = int(loc[1]), columns[loc[0]]

result = 0
result_list = []

for plan in plans:
    fail_count = 0
    i, j = int(loc[1]), columns[loc[0]]

    for move in plan:
        if move == 'U':
            if (i - 1) <= 0:
                fail_count += 1
                pass
            else:
                i -= 1
        elif move == 'D':
            if (i + 1) > 8:
                fail_count += 1
            else:
                i += 1
        elif move == 'R':
            if (j + 1) > 8:
                fail_count += 1
            else:
                j += 1
        elif move == 'L':
            if (j - 1) <= 0:
                fail_count += 1
            else:
                j -= 1

    if fail_count == 0:
        result_list.append((i, j))
        result += 1

print(result_list)
print(result)



