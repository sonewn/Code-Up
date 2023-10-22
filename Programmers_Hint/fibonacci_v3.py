"""
피보나치수 나머지 구하기 v3
: F(n-1), F(n-2) 변수를 동시할당으로 변경, 이에 의해 for 문 range 도 변경

"""

def solution(n):
    """
    p1 : n번째 피보나치 수
    p2 : n+1 번째 피보나치 수
    """
    p1, p2=0, 1
    for idx in range(n): #0~n-1
        p1, p2 = p2, (p1%1234567+p2%1234567)%1234567
 
    return p1

print(solution(100000))