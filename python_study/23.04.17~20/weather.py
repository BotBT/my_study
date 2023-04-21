# weather = "비" # weather 변수에 값 할당
# print("비가 오나요?", weather == "비") # 
# if weather == "비": # weather의 값이 "비"와 같으면 조건식이 True이므로 안쪽 코드 블록 실행
#     print("우산을 가져간다")
# else: # 조건식이 False이면 실행
#     print("우산을 가져가지 않는다.")

weather = "맑음" # weather 변수에 값 할당
print("비가 오나요?", weather == "비") # 
if weather == "비": # weather의 값이 "비"와 같으면 조건식이 True이므로 안쪽 코드 블록 실행
    print("우산을 가져간다")
elif weather == "맑음":
    print("날씨가 좋다.")
else: # 조건식이 False이면 실행
    print("우산을 가져가지 않는다.")
# 첫 조건에서 False가 나와야 elif를 사용하고 조건식을 걸 수 있다.


