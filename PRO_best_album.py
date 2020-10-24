# 문제출처 : 프로그래머스
# 문제유형 : 해시
# 문제번호 : 코딩테스트 연습 > 해시 > 베스트앨범
# 문제명 : 베스트앨범

import pandas as pd


def solution(genres, plays):
    answer = []
    df = pd.DataFrame({'genres': genres,
                       'plays': plays})
    sorted_by_plays = df.groupby('genres').sum().sort_values(by='plays', ascending=False)

    for genre in sorted_by_plays.index:
        result = df[df['genres'] == genre].sort_values(by='plays', ascending=False).head(2)
        answer.extend(list(result.index))
    print(answer)
    return answer