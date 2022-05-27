# CodeUp 2.0 Greedy 2001
# 파파 파스타 가게는 점심 추천 파스타와 생과일 쥬스 세트 메뉴가 인기가 좋다.
# 이 세트 메뉴를 주문하면 그 날의 3 종류의 파스타와 2 종류의 생과일 쥬스에서 하나씩 선택한다.
# 파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.
# 어느 날의 파스타와 생과일 쥬스의 가격이 주어졌을 때, 그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.

# 입력은 5행, 한 줄에 하나씩 야의 정수

# 1행 정수 첫 번째 파스타 가격
# 2행 정수 두 번째 파스타 가격
# 3행 정수 세 번째 파스타 가격
# 4행 정수는 첫 번째 쥬스 가격
# 5행 정수는 두 번재 쥬스 가격
# (모든 파스타와 쥬스의 가격은 100원 이상 2000원 이하)




'''
# min method

pasta1 = int(input())
pasta2 = int(input())
pasta3 = int(input())

juice1 = int(input())
juice2 = int(input())

pasta = [pasta1, pasta2, pasta3]
juice = [juice1, juice2]

minimum_pay = (min(pasta)+min(juice))*1.1

print(f'{minimum_pay:.1f}')
'''


# greedy


pasta = list()
juice = list()

p_min = 2000
j_min = 2000

for i in range(3):
    temp = int(input())
    if p_min > temp:
        p_min = temp

for j in range(2):
    temp2 = int(input())
    if j_min > temp2:
        j_min = temp2

minimum_pay = (p_min+j_min)*1.1

print(f'{minimum_pay:.1f}')






