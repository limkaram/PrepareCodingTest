# 문제출처 : 이것이 코딩테스트다
# 문제유형 : 구현
# 문제번호 : 실전 3
# 문제명 : 게임 개발
# 진행중

from itertools import cycle

class user:
    def __init__(self, current_location, watching_direction):
        self.current_location = current_location
        self.watching_direction = watching_direction

    def turn_head(self):
        directions = iter(cycle([0, 1, 2, 3]))



    def move_foward(self):
        pass

    def move_backward(self):
        pass
