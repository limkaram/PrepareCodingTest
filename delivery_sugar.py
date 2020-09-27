# 문제출처 : 백준 온라인 저지
# 문제유형 : 그리드 알고리즘
# 문제번호 : 2839번
# 문제명 : 설탕 배달

N = int(input())  # 배달해야하는 N
count_of_5kg = 0
count_of_3kg = 0
remain = 0
total = 0

if N % 5 == 0:  # 5로 나누어 떨어지는 경우
    count_of_5kg = N // 5
    print(count_of_5kg)
else:  # 5로 나누어 떨어지지 않는 경우
    count_of_5kg = N // 5
    remain = N % 5
    if remain % 3 == 0:  # 5로 나눈 나머지가 3으로 나누어 떨어지는 경우
        count_of_3kg = remain // 3
        total = count_of_5kg + count_of_3kg
    else:  # 5로 나눈 나머지가 3으로도 나누어 떨어지지 않는 경우
        while count_of_5kg >= 0:
            count_of_5kg -= 1
            remain += 5
            if remain % 3 == 0:
                count_of_3kg = remain // 3
                total = count_of_5kg + count_of_3kg
            else:
                total = -1
print(total)

