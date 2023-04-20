li_1 = ["Hello", "World", "Python"]
# li_1의 원소를 사용하여 Hello World Python 이라고 출력하세요.
# print(li_1[0], li_1[1], li_1[2])
## join(리스트) : 리스트의 문자열을 합친다.
## " ".join(리스트) : " " 사이사이 넣어서 합쳐서 출력해준다.
## print(" ".join(li_1))
## print(li_1[0] + " " + li_1[1] + " " + li_1[2])

# li_1의 원소를 사용하여 Help라고 출력하세요.
# li_1.clear()
# li_1.append("Help")
# print(li_1["Help"])

## print(li_1[0][:3] + li_1[2][0])

li_2 = [1, 2, 3]

# li_1과 li_2를 사용하여 ["Hello", "World", "Python", 1, 2, 3] 을 출력하세요.
print(li_1 + li_2)
li_1.extend(li_2)
print(li_1)
# li_1과 li_2를 사용하여 ["Hello", 1, "World", 2, "Python", 3] 를 출력하세요.
li_1.insert(1, li_2[0])
li_1.insert(3, li_2[1])
li_1.insert(5, li_2[2])
print(li_1)

li_1.insert(1, li_2[0])
li_1.insert(3, li_2[1])
li_1.append(li_2[2])
print(li_1)


