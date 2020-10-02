# 문제출처 : 프로그래머스
# 문제유형 : 정렬
# 문제번호 : 코딩테스트 연습 > 정렬 > 가장 큰 수
# 문제명 : 가장 큰 수

# 1번째 솔루션
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))


# 2번째 솔루션
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


if __name__ == '__main__':
    numbers = [6, 4, 2, 0]
    # numbers = [0, 0, 0, 0]
    # numbers = [1, 11, 111, 1111]
    # numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))