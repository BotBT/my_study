if :#조건:
    실행하려는 코드
    코드 2줄
    코드 3줄
코드 4줄
파이썬은 들여쓰기로 코드블록을 구별한다.

bool (블타입)
Ture(참), False(거짓)

if조건 :
    True(참)일 때만 안쪽 코드블럭을 실행
else :
    True가 아닐때 실행하려는 코드
    else는 조건이 False(거짓)일 때 안쪽 코드 블럭을 실행

if 조건1:
    조건1 이 참일 때 실행
else 조건2:
    조건1은 False, 조건2는 True일때 실행
else :
    조건1 False 조건2 False 일때 실행

number1 = 6
number2 = 7
if number1 > number2:
    print(number1 > number2)
    print("number1이 더 크다.")
elif number1 == number2:
    print(number1 == number2)
    print("같다.")
else: 
    print(number1>number2)
    print("number1이 더 크다.")
비교 연산자
>
>=
<
<=
==
!= 같지 않을대 사용

number1 = 8
number2 = 7
if number1 > number2:
    print(number1 > number2)
    print("number1이 더 크다.")
elif number1 == number2:
    print(number1 == number2)
    print("같다.")
else: 
    print(number1>number2)
    print("number1이 더 크다.")
print ("a" < "b") #True
print ("CAT" < "DOG") #True
print("COW" > "CAT") #True
print("DOG" == "dog") #False
print("DOG" > "dog") #False

논리 연산자 (Ture, False에 적용)
and (그리고) - <a and b> 둘다/모두 True면 Ture, True가 아닐경우 False
or (또는) - <a or b>둘 중 하나라도 True면 True 둘다 False면 False
not (아니다) - <a not b> True면 False로 False면 Ture로

print(True and True) # T
print(True and False) # F
print(False and True) # F
print(False and False) # F

print(True or True) # T
print(True or False) # T
print(False or True) # T
print(False or False) # F

print(not True) # F
print(not False) # T

age = 19
if age >= 20 and money >= 10000:
    print("성인이고 부자입니다.")

age = 19
if age >= 20 or money >= 10000:
    print("성인 혹은 부자입니다.")

if "안녕":
    print("안녕하세요")
if 0:
    print(0) # 숫자에서 비어있는 값 = 0
#  False면 = 0 , true면 = 1

