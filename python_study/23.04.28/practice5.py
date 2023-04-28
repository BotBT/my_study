# 거꾸로 배열해도 같은 단어 또는 문장이 되는
# 회문(pralindrome)인지 판별하는 함수를 정의하시오
# 함수에 문자열을 입력받고 회문하면 True
# 아니면 False를 반환하도록 정의하세요.
# 함수 이름 : is_palindrome
# 반환 값 : True 또는 False

"""
exit
word = input('단어를 입력하세요:')

is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False        # 회문이 아님
        break
 
print(is_palindrome)   
"""

def is_palindrome(input_string):
    input_string = input_string.replace(" ", " ") # 문자열 중간에 있는 공백 제거
    # length = len(input_string) #1번째 방법
    # for i in range(length//2):
    #     length - 1
    #     if input_string[i] == input_string[length - 1 - i]:
    #         #회문
    #         return False
    # return True

    return input_string == input_string[::-1] #2번째 방법(리스트를 뒤집을 수 있음.)      

result = is_palindrome("다시 합창합시다")
print(result)

reversed("안녕하세요") # 내장함수
li1 = [1,2,3,4]
# li1.reverse()
# li2.reverse(li1)
# print(li1)
# print(li2)

string1 = "안녕하세요"
string2 = reversed(string1)
for i in string2:
    print()
