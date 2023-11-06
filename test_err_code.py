'''
악성코드는 파일의 숫자 배열에 대해 슬라이딩 창을 사용하여 다음 패턴과 일치시키려고 시도한다.
> T, _, _, X, _, _, _, T

여기서 X 위치는 각 위치 T와 비교된다. 창이 이동되어 X가 모든 값을 통과한다.
악성코드에는 다음과 같은 규칙이 있다.
  - 패턴의 'T' 위치 중 하나라도 'X' 보다 크거나 같으면 악성코드는 'X' 를 0으로 바꿉니다.
  - 패턴의 'X' 위치가 왼쪽 또는 오른쪽 경계 근처에 있고 'T' 위치 이웃이 누락된 경우 반대쪽만 고련된다.
  - 악성코드는 먼저 모든 위치를 찾은 다음 이를 0으로 설정한다.

Input: [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]
Output: [1, 0, 0, 5, 0, 0, 0, 3, 3, 0]  
'''

def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    # Write your code here
    answer = entries.copy()
    for x in range(len(entries)):
      t1, t2 = x-3, x+4
      
      if (t1>= 0) and (entries[x] <= entries[t1]):
        answer[x] = 0
      if (t2 < len(entries)) and (entries[x] <= entries[t2]):
        answer[x] = 0      

    return answer
  
records = [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]
print(simulate(records))
# Expected output
# [1, 0, 0, 5, 0, 0, 0, 3, 3, 0]