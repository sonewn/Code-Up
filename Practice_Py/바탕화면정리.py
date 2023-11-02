import pandas as pd

'''
https://school.programmers.co.kr/learn/courses/30/lessons/161990
'''

def solution(wallpaper):
    answer = []
    row = []
    col = []
    #walldf = pd.DataFrame([list(w) for w in wallpaper])
    
    for idx, r in enumerate(wallpaper):
        for idx2, c in enumerate(r):
            if c == '#':
                row.append(idx)
                col.append(idx2)
                
    answer.append(min(row))
    answer.append(min(col))
    answer.append(max(row)+1)
    answer.append(max(col)+1)
    return answer

