# tuple(튜플) 형
# 튜플은 element(속성)의 값을 수정할 수 없다.
# mutable / immutable : 두 가지로 나뉠수 있다.
# mutable : 수정 가능한
# (list, dixt)
# immutable : 수정 불가능
# (int, float, str, tuple)

# my_list = [1, 2, 3]
# my_list[0] = 5
# print(my_list)

# my_tuple = (1, 2, 3)
# my_tuple[0] = 5 # Error 튜플형은 수정이 불가능 하다.
# print(my_tuple)
tuple_1 = ("Hello", "World", "Python")
t2 = (1, 2, 3, 4, 5)
t3 = (1, 2, "Hello")
t4 = 1, 2, 3 #가독성을 위해 괄호를 써주는게 좋다.
t5 = (1, 2, (3, 4, 5))
#자료형이랑 묶을 수 있는게 list랑 똑같다. 
t6 = tuple_1 + t2
# 연산자 '+ ,*' 이용하면 tuple에서는 합치는 걸로 적용이 된다.
# 수를 더하는게 아니다. 
# 연산자를 이용시 새로 만드는 느낌이다.
t7 = t3 * 3 #'*' 반복하는 의미.
t7 = t3 * 4
# print(t7)

t3 = (1, 2, "Hello")
# print(t3[2]) #str 문자형으로 가지고 온다.
# print(t3[0:2]) #슬라이싱형을 선택시 '튜플형'태로 가지고 오게 됨.
# print(len(t3)) #length 길이형으로 가지고 온다.

# print(t5[2][1]) #4가 출력이 된다.

# t8 = (5, 3, 1, 4, 2) #순서를 정렬하고 싶다. → 
# #튜플형은 값이 바뀌기 (수정하는걸로 인식되기) 때문에 정렬이 불가능.
# for i in t8: # 'for' 인덱스 순서로 입력되 있다.
#     print(i) #5, 3, 1, 4, 2

# 예제 1.
# 2 ~ 9 사이의 숫자를 입력받아 해당하는 단의 구구단을 출력하시오
# 2 ~ 9 사이의 숫자가 아닌 값이 입력된 경우, 잘못 입력되었다고
# 출력하고 다시 입력받으세요.

# n = int(input("몇 단?"))   
# # if n < 2 or n > 10: # 2 ~ 9 사이의 아닐때 True
# #      # 다시 입력받기.
# #     pass
# # if n >= 2 and n <= 9: # 2 ~ 9 사이의 값일 때 True
# #     pass
# # if 2 <= n <= 9:
# #     pass
# # if n < 2 or n > 10:
# # 2 <= n <= 9: → 2 ~ 9 사이라면 True
# while not 2 <= n <= 9: # not을 넣어 조건이 만족하지 않는면 다음으로 넘어간다.
#     print("2 ~ 9 사이의 숫자를 입력해주세요.")
#     n = int(input("몇 단?"))

# for i in range(1, 10):
#     print(n, "*", i, "=", n*i)
# for i in range(9):
    # print(n * (i + 1))

# 예제 2.
# 정수를 입력받고 그 정수보다 작은 수 중 가장 큰 제곱수를 출력하시오.
# m = int(input("정수 :")) #int()로 변수 선언_(input("정수 :"))
# i = 1 # i를 1로 선언
# while True: #무한 반복 while을 사용.
#     # i * i
#     if i ** 2 >= m: # i를 2 제곱을 m만큼 큰지 돌려봄.
#         break #위에 조건문이 True면 멈춘다.
#     answer = i ** 2 #answer : 대답하다 응답하다 라는 의미의 함수.
#     i += 1 #break가 안걸릴시 i의 1을 더한다.
# print(answer) #while 바깥쪽으로 출력한다.
# 1/2 == 0.5
# 4 ** 1/2 == 2 == 4 ** 0.5

# 예제 3.
# [1, 2, 3, 4, 5]
# [10, 20, 30, 40, 50]
# [532, 5941, 54682, 58, 5]
# 3개의 리스트에서 같은 인덱스의 값끼리 더하여 출력하세요
# n = [1, 2, 3, 4, 5]
# m = [10, 20, 30, 40, 50]
# k = [532, 5941, 54682, 58, 5]
# # for i in range(5):
# #     print(n[i], m[i], k[i]) 
# # for x, y, z in zip(n, m, k): #변수가 한개씩 꺼내 사용 <x,y,z 각각>
# #     print(x + y + z)
# # zip()
# # 길이가 같은 list를 묶어서 for문 등으로 사용 가능한 iterable을 반환한다.
# i = 0
# while i < 5:
#     print(n[i] + m[i] + k[i])
#     i += 1

# 예제 4.
# 정수를 입력받고 1부터 입력받은 정수까지 모두 출력하세요.
# 단, 숫자에 3, 6, 9가 들어있는 경우 숫자 대신 짝이라고 출력하세요.
# n = int(input("정수 :"))
# # for i in range(n): #for i in range(1, n + 1)
# #     print(n+1) #print(n)
# for i in range(1, n + 1): # n=0 이라고 과정하고 + 1을 한다.
#     anwser = i #anwser 함수를 i로 설정
#     for j in str(i): # for문을 사용하기 위해 str형 입력. for문이 하나씩 꺼내오기에 str형 입력이 적절하다.
#         if int(j) % 3 == 0 and j != "0": #int의 j를 넣어 3의 배수를 구한다 그리고 j의 '!=' 부정 부등호를 넣는다.
#             anwser = "짝"
#             break #continue
#     print(anwser)

# 예제 5.
# 정수를 입력받고 그 정수의 약수를 모두 출력하세요.
# 약수 : 나누었을 때 나머지가 0으로 나누어 떨어지게 하는 수

n = int(input("정수 :"))
# for i in range(1, n+1): # 1부터 n까지
#     if n % i == 0:
#         print(i)

# for i in range(n): # 0 ~ n-1
#     if n % (i+1) == 0:
#         print(i+1)

i = 1
while 1 <= n:
    if n % i == 0:
        print(i)
    i += 1