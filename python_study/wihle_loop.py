# while 반보문
"""
wihle 조건:
    반복할 코드
"""
# 조건이 참인 경우에 코드를 계속 반복

# i = 1
# while i <= 10:
#     print(i)
#     i += 1 # i = i+1


# '+=' 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미
# -= 1은 n = n-1
# *=
# /=
# **=
# //=
# %=
# ex) s1 = "안녕"  /  s1 += "하세요" (연산자를 사용해서 사용 가능.)
# ex) s1 = s1 + "하세요"

# while 반복문을 활용하여 10부터 1까지 순서대로 출력하세요

# n = 10
# while n > 0: # while n >= 1:
    # print(n)
    # n -= 1

# money = 10000
# price = 1000
# while money >= price:
# # while money - price > 0:
#     print('커피를 구매했습니다.')
#     money -= price
"""
money = 10000
price = 1000
coffe = 5
while money >= price:
# while money - price > 0:
    print('커피를 구매했습니다.')
    money -= price
    coffe -= 1
    print("남은 커피", coffe)
    if coffe == 0:
        break #함수를 사용하여 반복문 조건에서 중간에 프로세스를 종료한다. 
"""
# break  
# 반복문을 즉시 종료한다.
# if문과 함계 같이 사용되기도 한다.

#while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다.
# a = 1
# while a <= 10:
#     if a % 2 == 1:
#         print(a)
#     a += 1

# continue
# 반복문의 제일 처음으로 돌아감
# b = 1
# while b <= 10:
#     if b % 2 == 0:
#         continue
#     print(b)
#     b =+ 1 
# c = 0
# while c <= 9:
#     c =+ 1 
#     if c % 2 == 0:
#         continue
#     print(c)


"""while True: # 무한 반복문 / 무한 루프
    print("hi")"""
# while의 뒤에 조건문에 따라 반복한다.
# 조건식에 True를 입력해 항상 참이 되조록 하여 무한히 반복하게 한다.
# 터미널에서 출력물 무한 반복시에 crtl + c를 입력하여 강제 종료 할 수 있다.
# KeyboardInterrupt

# while True:
#     user_input = input("종료하려면 1을 입력해주세요")
#     if user_input == '1':
#         break

# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# 2개의 수를 계산 a + b
# while True:
#     print("""
#     계산기
#     =======
#     1. 더하기(+)
#     2. 빼기 (-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     """)
#     operator = input("계산을 선택하세요 : ")
#     if operator == '1': # '==' 비교 연산자 데이터가 서로 같냐를 사용.
#         print('1+2 = ', 1 + 2)
#     if operator == '2':
#         print('1-2 = ', 1 - 2)
#     if operator == '3':
#         print('1*2 = ', 1 * 2)
#     if operator == '4':
#         print('1/2 = ', 1 / 2)

# 코드를 수정해서 사용자가 입력한 숫자를 이용해
# 계산하도록 변경하시오.
# while True:
#     print("""
#     계산기
#     ==========
#        /  *
#     1  2  3  -
#     4  5  6  +
#     7  8  9  ▶
#     """)
#     operator = input("계산을 선택하세요 : ")
#     x = int(input("숫자를 입력하세요"))
#     y = int(input("숫자를 입력하세요"))
#     if operator == ' 1 ': # '==' 비교 연산자 데이터가 서로 같냐를 사용.
#         print(x, "+", y, "=", a + b)
#     elif operator == ' 2 ':
#         print(x, '-', y, '=', x - y)
#     elif operator == ' 3 ':
#         print(x, '*', y, '=', x * y)
#     elif operator == ' 4 ':
#         print(x, "/", y, "=", x / y)
#     elif operator == 'q':
#         break

# 사용자가 가지고 있는 돈을 입력받는다
# 구매할 수 있는 커피의 개수와 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다.
# 구매할 수 있는 콜라의 개수와 잔돈을 출력한다
# 커피는 500원 음료수는 700원 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.
# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈:"))
# while idx < len(prices): # 유동적으로 사용하기 위해 정수 대신 코드 사용.
#      # while idx < 3: or while idx <= 2:
#     price = prices[idx]
#     print(money // price)
#     print(money % price)
#     idx += 1

# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를
# 정수형으로 입력받으세요.
# ave = 0
# course = ["국어", "영어", "수학", "과학", "사회"]
# scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
# er = int(input("평균 점수:"))
# while er < len(score):
#     score = scores[ave]
#     print(len(course) // score)
#     print(len(course) % score)
#     ave += 1

# scores = []
# n = 0
# while n < 5:
#     score = int(input("시험점수"))
#     scores.append(score)
#     n += 1

#  while 반복문을 사용하여 구구단 2단을 출력하세요.
"""
e = []
l = 2
while l <= 9:
    print(l)
    l *= 1
""" 

o = 1
while o < 10:
    print("2 *", o, "=", 2*o)
    o += 1