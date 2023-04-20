# """
# eng 변수, kor 변수, math 변수를 만들고
# 각 변수는 과목의 시험 점수이다.
# 영어 점수는 80점
# 국어 점수는 60점
# 수학 점수는 50점
# 3과목 점수의 평균을 내고
# 평균 점수에 따라 성적을 출력한다.
# A : 91 ~ 100
# B : 81 ~ 90
# C : 71 ~ 80
# D : 61 ~ 70
# F : 60 이하
# """

# eng = 80
# kor = 60
# math = 50
# a = (eng + kor + math)
# b = 3
# print(a / b)

# A = 91
# B = 81
# C = 71
# D = 61
# F = 60
# if a / b >= A:
#     print("A 학점")
# elif a / b >= B:
#     print("B 학점")
# elif a / b >= C:
#     print("C 학점")
# elif a / b >= D:
#     print("D 학점")
# elif a / b <= F:
#     print("F 학점")
# else:
#     print()

# user_input = input()
# print(user_input)

# eng = int(input("영어 점수"))
# kor = int(input("국어 점수"))
# math = int(input("수학 점수"))

# avg = (eng + kor + math) / 3
# if avg >= 91:
#     print("A 학점")
# elif avg >= 81:
#     print("B 학점")
# elif avg >= 71:
#     print("C 학점")
# elif avg >= 61:
#     print("D 학점")
# elif avg <= 60:
#     print("F 학점")
# else:
#     print()


# scores = []
# scores = list() #비어있는 리스트 생성.
# scores.append(int(input("영어 점수:")))
# scores.append(int(input("국어 점수:")))
# scores.append(int(input("수학 점수:")))


# avg = (scores[0] + scores[1] + scores[2]) / 3 #터미널에 점수를 입력해서 평균을 구한다.
# avg = sum(scores) / 3
# # sum()
# # 리스트의 요소를 모두 더한다.
# # 숫자를 더하기 때문에 문자랑 섞이지 않게 조심해야 한다.
# if avg >= 91:
#     print("A 학점")
# elif avg >= 81:
#     print("B 학점")
# elif avg >= 71:
#     print("C 학점")
# elif avg >= 61:
#     print("D 학점")
# elif avg <= 60:
#     print("F 학점")
# else:
#     print()

# 정수형 변환 함수
# 정수형, integer형, int혈
# int(값)
#  ex) int(input("점수"))  or int(eng)

# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건을 몇개 살 수 있는지 출력한다.
# 물건의 가격은 500원 이다.
# age = input("나이:") # input 함수로 할당한다.
# money = int(input("돈")) #int 함수를 안에 input함수를 할당한다
# price = 500
# print(money // price) # 정수로 나와야 한다.
# print(money % price) # 연산자가 나온다

# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건별로 각각
# 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1번 물건 1000원
# 2번 물건 50원 3번 물건 120원이다.

age = input("나이:") 
money2 = int(input("돈")) 
prices = [1000, 50, 120]
print(money2 // prices[0], money2 % prices[0])
print(money2 // prices[1], money2 % prices[1])
print(money2 // prices[2], money2 % prices[2])

# Input 함수
# - 정보를 입력받는 함수
# ex) user_input = input()
#  - 터미널에서 대기 상태로 진입하여 문자를 입력 가능하다.
#  - 문자 입력하고 난 후 컴퓨터가 작성한 함수를 똑같이 출력 함.

# (함수 : sum → 총합을 구하는 함수 / avg → 평균을 구하는 함수