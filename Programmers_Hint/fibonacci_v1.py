"""
피보나치수 구하기

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.
"""

def solution(n):
    """
    p : n번째 피보나치 수
    p1 : n-2번째 피보나치 수
    p2 : n-1번째 피보나치 수
    """
    p1=0
    p2=1
    for idx in range(1,n): #1~n-1
        p = p1+p2
        p1 = p2
        p2 = p

    answer = p%1234567
    return answer

print(solution(100000))