# 문제출처 : 백준 온라인 저지
# 문제유형 : 그리디
# 문제번호 : 14720번
# 문제명 : 우유 축제

from itertools import cycle
from collections import deque

store_num = int(input())
store = deque(map(int, input().split()))

count = 0

for milk in cycle([0, 1, 2]):
    while len(store) > 0:
        milk_kind = store.popleft()
        if milk == milk_kind:
            count += 1
            break
    if len(store) == 0:
        break
print(count)
