#MyCalculator 클래스를 만들어보세요
# add, sub, mul, giv 메소드
my_calculator = MyCalculator
# while True:
#     print("계산기 ---- 1: +")
#     operator = input()
#     if operator == 'q':
#         break
#     n1 = int(input())
#     n2 = int(input())
#     if operator == "1":
#         my_calculator.add(n1, n2)
        
class MyCalculator:
    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1+n2}")
    def sub(self, n1, n2):
         print(f"{n1} - {n2} = {n1-n2}")
    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1*n2}")
    def div (self, n1, n2):
        print(f"{n1} / {n2} = {n1/n2}")
while True:
    print("""
    계산기 
    1. +
    2. -
    3. *
    4. /
    """)
    
    operator = input()
    if operator == 'q':
        print("종료합니다.")
        break
    n1 = int(input())
    n2 = int(input())
    if operator == "1":
        my_calculator.add(n1, n2)
    elif operator == "2":
        my_calculator.add(n1, n2)
    elif operator == "3":
        my_calculator.add(n1, n2)
    else:
        print("잘못 입력했습니다.")






