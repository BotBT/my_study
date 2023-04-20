# 리스트(list) 자료형
# 여러개의 값을 변수 1개에 저장
# [1, 2, 3] - 대괄호 안에 쉼표를 넣어 여러개를 넣을 수 있다.
# [1, 1, 1, 1] - 똑같은 값을 여러번 넣을 수 있다.
# 메모리에 입력된 값에 데이터 크기를 파이썬이 알아서 잡아준다.
# ["Hello", "World", "Python"] - 문자열 입력 가능.
# [1, "Hello", 2, "Oh"] - 자료형을 섞어서 사용 가능.
# [1, 2, ["Hello", "World"]] - 리스트 안에 또 리스트를 넣을 수 있음.
#  [] - 아무값도 않넣을 수 도 있다.
#  리스트는 0개 이상 넣을 수 있는 자료형이다.

# li_1 = [1, 2, 3]
# # print(li_1[0])
# # print(li_1[1])
# # print(li_1[2])
# # print(li_1[-1])
# # print(li_1[0] + li_1[1])

# li_2 = [1, 2, 3, [4, 5, 6]]
# # print(li_2[3][0])

# # # [[1, 2, 3],
# # # [4, 5, 6],
# # # [7, 8, 9]]

# # print(li_2[1:])
# # print(li_2[:2])
# # print(li_2[3][0:2])
# # print(li_2[1:])
# # print(li_2[0]) # 출력값 1dl 나옴

# li_3 = [1, 2, 3, 4, 5]
# # 출력 결과가 [2, 3]이 되도록 만드세요.
# # print(li_3[1:3])
# # li_3[0] = 10
# # print(li_3)

# # 추가하는 함수 append(원소)
# # 리스트의 마지막에 원소를 추가한다.
# li_4 = [1, 2, 3]
# li_4.append(4) #.append() 를 붙여 리스트를 추가한다.
# print(li_4)

# # insert(인덱스, 원소)
# # 인덱스 위치에 원소 삽입
# li = [1, 2, 3]
# li.insert(1, 10)
# print(li)

# remove(값) 리스트를 없애는 함수.
# 리스트에서 함수에 입력된 값과 같은 값을 찾아 삭제함.
# li = [1, 2, 3,]
# li.remove(2)
# print(li) # 출력값 [1, 3]
# 같은 수가 있을 경우 제일 앞에 있는 값만 삭제된다.
# 리스트의 없는 값을 삭제하려고 하면 에러가 난다.

# pop(인덱스)
# 리스트의 인덱스 위치의 요소를 꺼낸다.
# 인덱스를 함수에 전달하지 않으면 제일 마지막 요소를 꺼낸다.
# li = [1, 2, 3, 4]
# a = li.pop()
# print(li) # [1, 2, 3]
# print(a)
# b = li.pop(1)
# print(li) # [1, 3]
# print(b)

# index(값)
# 리스트에서 값을 찾아 그 값이 인덱스를 알려준다.
#  값이 리스트에 없으면 에러가 난다.
# li = [1, 2, 3]
# idx = li.index(2)
# # li[2] → 인덱싱(인덱스로 값에 접근)
# # li.index(2) → 인덱스 알아내기
# print(idx)

# # sort() : 정렬하는 함수.
# # 리스트의 요소를 정렬한다.
# li = [5, 3, 1, 4, 2]
# li.sort()
# print(li) # [1, 2, 3, 4, 5]
# li.sort(reverse = True) # reverse를 사용하여 정자 반대로 정렬.
# print(li)

# reverse()
# 리스트의 순서를 뒤집는 함수
# 정렬이 아니다.
# li = [1, 2, 4, 5, 3]
# li.reverse()
# print(li) # [3, 5, 4, 2, 1] 순서만 뒤짚어서 값이 나온다.

# count(값)
# 리스트 안에서 해당 값이 몇 개 있는지 세는 함수.
li = [1, 2, 3, 2, 5]
cnt = li.count(2) # 값 '2'에 카운트를 변수 설정
print(cnt) # 같은 값이 2개 있으면 카운트가 숫자가 나오며, 각각 있으면 1개만 나온다.

# 리스트 연산
#  '+'연산자 : 리스트를 연결한다.
li_1 = [1, 2, 3]
li_2 = [4, 5, 6]
print(li_1 + li_2) # [1, 2, 3, 4, 5, 6] 출력값이 나옴.

# exrned() 함수와 같다.
li_1.extend(li_2) # 리스트를 합친다.

# '*' 연산자 : 리스트를 반복한다
li = [1, 2, 3]
print(li * 3) # 3번 반복 한다 - 출력값 : [1, 2, 3, 1, 2, 3, 1, 2, 3] 