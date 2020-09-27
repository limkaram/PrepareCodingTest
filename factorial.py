# 문제출처 : 백준 온라인 저지
# 문제유형 : 재귀함수
# 문제번호 : 10872번
# 문제명 : 팩토리얼

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))