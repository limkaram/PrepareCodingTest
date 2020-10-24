# 문제출처 : 백준 온라인 저지
# 문제유형 : 구현
# 문제번호 : 1110번
# 문제명 : 더하기 사이클

n = input()
initial = n

cycle_count = 0

while True:
    if cycle_count > 0 and n == initial:
        break

    if int(n) < 10:
        n = '0' + str(int(n))

    addition = str(int(n[0]) + int(n[1]))
    n = n[-1] + addition[-1]
    n = str(int(n))
    cycle_count += 1

print(cycle_count)