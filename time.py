# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 구현
# 문제번호 : 예제 4-2
# 문제명 : 시각

count = 0

hours = int(input())
minutes = range(60)
seconds = range(60)

for hour in range(hours+1):
    for minute in minutes:
        for second in seconds:
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

print(count)
