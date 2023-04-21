# # dictionary(딕셔너리) 자료형
# # key-value 형태
# # key: value
# # person = {"이름": "이름",
# #             "나이": 18,
# #             "점수": {
# #                     "영어": 80,
# #                     "국어": 90,
# #                     "수학": 100},
# #                                 }
# # 1: "ㅎㅎ"
# # print(person["나이"])
# # print(person["점수"]["영어"]) # 키값을 두개 입력해서 정보를 받을 수 있다. (1개도 가능)

# # dict_1 = {1: 'a'}
# # dict_1['B'] = 2 # 'B' : 2 Key-value 쌍 추가
# # dict_1[1] = 'c'
# # del dict_1[1]
# # print(dict_1)

dict_2 = {1: 'a', 2:'b', 3: 'c'}
# #  keys()
# # 딕셔너리에서 key 값만 리스트 형태로 돌려준다.
# dict_key = dict_2.keys()
# print(dict_key)
# # values()
# # 딕셔너리에서 value 값만 리스트 형태로 돌려준다.
# dict_values = dict_2.values()
# print(dict_values)
# # items()
# # 딕셔너리에서 key-value 쌍을 튜플로 묵은 값을 리스트 형태로 돌려준다.
# dict_items = dict_2.items()
# print(dict_items)

# # get(key)
# # key에 대응되는 value를 돌려준다
# # key값이 존재하지 않으면 None을 돌려준다.
# # dict_2.get("나이")
# # print(dict_2.get("나이")) #None이 나오는경우 데이터는 존재하고 '0'이라고 보면 됨.
# print(dict_2.get("나이", "나이 불명")) # 키가 None일 경우 뒷자리에 0을 처리하도록 하며, 
#                                       # 뒤에 적힌 값에 출력이 된다.

# clear()
# 딕셔너리 안의 모든 요소를 삭제한다.
dict_2.clear()
print(dict_2) # 출력값 {}