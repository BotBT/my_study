# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 작은 수 중 3의 배수와 5의 배수를 모두
# 더한 합을 반환하는 함수.
# 함수 이름 : sum_3_5

# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 0:
#     return result

def sum_3_5(n):
    result = 0
    for i in range(n):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i
    return result

# 정육면체 주사위 2갸가 있다.
# 2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을
# 모두 print하는 함수를 정의하세요
# 함수 이름 : draw_dice
# 출력 예시
# 1, 2
# 6, 3

def double_dice():
    for i in range(1, 7): # 1-6
        for j in range(1, 7): # 1
            print(i, j)

# def double_dice():
#     while i < 7:
#         j = 1
#     while j <7:
#         print(i, j)

# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를
# 정의하세요
# 함수 이름 : get_diff
# 파라미터 : a, b
# 반환값 : result

def get_diff(a, b):
    result = abs(a - b) 
    # if a > b :
        # result = a - b
    # else a < b :
        # result = b - a
    return result

# 가장 큰 수를 만드는 함수.
# 함수에 입력된 5개 정수를 사용하여 만들 수 있는 가장 큰 수를
# 반환하는 함수를 정의하세요.
# 함수 이름 : get_biggest
# 피라미터 : a, v, c, d, e
# 반환값 : result
def get_biggest(a,b,c,d,e):
    # numbers = [a, b, c, d, e]
    numbers.sort() # 리스트 값을 정렬을 한다
    numbers = [1,2,3,4,5]
    result = 0
    for i in range(len(numbers)): # 0~4
        result += numbers[i] * (10 ** i)
    return result

    # numbers = [a,b,c,d,e]
    # numbers.sort(reverse=True)
    # result = ""
    # for i in numbers:
    #     result += str(i)
    # return int(result)

# 별 찍기 2
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을
# 화면에 출력한다
# 함수이름 : print_stars2

def print_stars2(n):
    for i in range(1, n+1): #1~n
        print(" " * (n - i) + "*" * i) 
        # i는 *의 개수 / n-i
