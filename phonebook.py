# 문제출처 : 프로그래머스
# 문제유형 : 해쉬
# 문제번호 : 코딩테스트 연습-해쉬-2번문제
# 문제명 : 전화번호 목록

def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))

    find_count = 0

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                find_count += 1
                answer = False
                break
        if find_count >= 1:  # 접두어를 찾았을 경우 i 또한 더 진행하지 않고 나가게 해주는 것이 효율성 득점에 필요
            break
    return answer

if __name__ == '__main__':
    phone_book = ['119', '97674223', '1195524421']
    # phone_book = ['123', '456', '789']
    # phone_book = ['12', '123', '1235', '567', '88']
    solution(phone_book)