# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 구현
# 문제번호 :
# 문제명 : 문자열 재정렬

import re

string = input()

regex_str = re.compile(r'[A-Z]')
regex_num = re.compile(r'[0-9]')

result_str = ''.join(sorted(regex_str.findall(string), reverse=False))
result_num = str(sum(map(int, regex_num.findall(string))))

print(result_str + result_num)