''' 3120 : 리모컨

컴퓨터실에서 수업 중인 정보 선생님은 냉난방기의 온도를 조절하려고 한다.
냉난방기가 멀리 있어서 리모컨으로 조작하려고 하는데, 리모컨의 온도 조절 버튼은 다음과 같다.

1) 온도를 1도 올리는 버튼

2) 온도를 1도 내리는 버튼

3) 온도를 5도 올리는 버튼

4) 온도를 5도 내리는 버튼

5) 온도를 10도 올리는 버튼

6) 온도를 10도 내리는 버튼

이와 같이 총 6개의 버튼으로 목표 온도를 조절해야 한다.
*현재 설정 온도*와 변경하고자 하는 *목표 온도*가 주어지면 이 버튼들을 이용하여 목표 온도로 변경하고자 한다.

이 때 버튼 누름의 최소 횟수를 구하시오.

예를 들어, 7도에서 34도로 변경하는 경우,
7 -> 17 -> 27 -> 32 -> 33 -> 34

이렇게 총 5번 누르면 된다. '''


# ---------------------------------------------------------------------------------------------
## 입력 예시
## 현재 온도a 와 목표 온도b가 입력된다. ( 0 <= a , b <= 40 )
## ex) 7 34

## 출력 예시
## 최소한의 버튼 사용으로 목표온도가 되는 버튼의 횟수를 출력한다.
## ex) 5
# ---------------------------------------------------------------------------------------------

# 첫 번째 풀이는 조건문 만으로 푼 풀이 이며, 두 번째 풀이는 while문을 사용했습니다.
# 첫 번째 풀이는 fea_gap 의 갱신없이, +-10버튼을 누른 후 나머지 정보만으로 push_no 구합니다.
# 두 번째 풀이는 fea_gap을 갱신하며, 매 loop 마다 push_no을 업데이트 합니다.

## 1. 조건문 풀이 : 수행 시간:170 ms / 메모리 :157,796 kb
##    --> numpy 사용 x 시 수행시간:수행 시간: 20ms / 메모리 : 27,724

import sys
import numpy as np

def remote_control(a, b):
    push_no = 0

    fea_gap = np.abs(b - a)

    '''
    np.abs 대체 코드:
    if a > b:
    a, b = b, a
    fea_gap = b - a
    '''

    # +- 10 버튼 누르는 횟수
    push_no += fea_gap // 10
    rest = fea_gap % 10

    if rest >= 8:
        # +- 10 버튼 한 번 더
        push_no += 1
        # +- 1 남은 온도
        push_no += 10 - rest

    elif rest >= 5:
        # +- 5 버튼 (rest: 5, 6, 7 일 때)
        push_no += 1
        rest = rest % 5
        # +- 1 남은 온도
        push_no += rest

    elif rest == 4:
        # +-5 and -+1
        push_no += 2

    else:
        # rest : 1, 2, 3 일 때
        push_no += rest

    return push_no


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(remote_control(a, b))




## 2. while 문 풀이 : 수행 시간:19 ms / 메모리 :27,724 kb

def remote_control(a, b):
    push_no = 0

    if a > b:
        a, b = b, a
    fea_gap = b - a

    while True:
        if fea_gap == 0:
            return push_no

        elif fea_gap >= 8:
            fea_gap -= 10

        elif fea_gap >= 4:  # fea_gap 3부터는 +-1버튼을 누르는 것과 동일 또는 더 적은 비용
            fea_gap -= 5

        elif fea_gap >= 1:
            fea_gap -= 1

        elif fea_gap < 0:
            fea_gap *= -1
            push_no -= 1  # 음수를 양수로 바꾸는 과정은 버튼 push에 해당되지 않으므로 뒤에서 더하는 +=1 을 미리 차감

        push_no += 1


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(remote_control(a, b))
