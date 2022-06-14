## 1172 : 세 수 정렬하기

'''
세 수를 오름차순으로 정렬하려고 한다. (낮은 숫자 -> 높은 숫자)
ex)
5 8 2 --> 2 5 8 로 출력

# 입력 : 세 정수가 입력된다
# 출력 : 낮은 숫자 부터 출력한다
'''


# 해당 문제를 2 가지 방법으로 풀이했습니다.


# 1. sorted 내장 함수 사용

def sorting_3no_1(no1, no2, no3):
  temp_lst = [no1, no2, no3]
  temp_lst = sorted(temp_lst)
  print(f'{temp_lst[0]} {temp_lst[1]} {temp_lst[2]}')


if __name__ == '__main__':
  a, b, c = map(int, input().split())
  sorting_3no_1(a, b, c)


# =======================================================================================================


# 2. 조건문 사용

def sorting_3no_2(no1, no2, no3):
  temp_lst = [no1, no2, no3]
  while True:
      if (temp_lst[0] <= temp_lst[1]) & (temp_lst[1] <= temp_lst[2]):
          print(f'{temp_lst[0]} {temp_lst[1]} {temp_lst[2]}')
          break
      forward = temp_lst[0]
      middle = temp_lst[1]
      backward = temp_lst[2]

      if forward > middle:
          temp_lst[0] = middle
          temp_lst[1] = forward

      elif forward > backward:
          temp_lst[0] = backward
          temp_lst[2] = forward

      elif middle > backward:
          temp_lst[1] = backward
          temp_lst[2] = middle


if __name__ == '__main__':
  a, b, c = map(int, input().split())
  sorting_3no_2(a, b, c)