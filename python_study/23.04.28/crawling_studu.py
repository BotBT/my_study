# 데이터 수집 단계
# 데이터 수집 → 데이터 분석/처리 → 인공지능 모델 학습. → 모델평가
# http(hypertext transfer protocol)
# request - response
# client - server
# html - 웹사이트를 표현하기 위한 언어 
# <html></html>
# html 파싱 

# import requests

# url = "http://www.naver.com/"
# response = requests.get(url)
# status = response.status_code
# html = response.text
# print(status)
# print(html)

# http 상태 코드
# 200 : OK
# 요청 성공
# 302 : 리다이렉트
# 다른 페이지로 바로 연결
# 400 : Bad Request 요청이 잘못됨
# 401 : Unauthorized 비인증됨
# 402 : 
# 403 : Forbidden 접근 권한 없음
# 404 : Not Found 요청받은 내용이 없음
# 405 : Merhond Not Allowed 접근 방법이 잘못 됨
# 500 : Internal Sever Rrror 서버 에러
# 501 : Not Implemented 개발중인 서버
# 502 : Bad Gateway 잘못된 응답

# url 구조
# 포로토콜://호스트주소:포트번호/경로?쿼리
# http://naver.com/?~~~~~
# 쿼리 - 추가적인 데이터를 포함할 때 쓰는 것.
# 쿼리이름=값&쿼리이름=값&쿼리이름=값

# BeautifulSoup
# html 파싱(parsing)
# html을 객체 구조화해서 사용
# html 태그
# <태그이름 속성 = 송성값>내용</태그이름>
# from bs4 import BeautifulSoup

# html = "<html><body>Hello</body></html>"
# soup = BeautifulSoup(html, "html.parser") # 객체가 만들어져 soup에 변수 선언
# print(soup.body.text)
# print(type(soup.body.text))

# import requests
# from bs4 import BeautifulSoup
# search_url = "https://www.google.com/search?q=%EB%A7%A5%EC%A3%BC&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiKvuiS_cv-AhVT_mEKHY1qA9AQ_AUoAXoECAEQAw&biw=747&bih=959&dpr=1"
# keyword = "맥주"
# url = search_url + keyword
# response = requests.get(url)
# # print(response.text)
# # print(type(response.text))
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img')
# import os #운영체제 관련된 기능을 사용가능(파일폴더 생성)
# folder_name = "imgs"
# if not os.path.exists(folder_name):
#     os.mkdir("imgs")
# for img in enumerate(imgs[1:]):
#     file_name = "img.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(imd['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f:#'wb' : 비트를 쓰겟다.
#         f.write(img_data)

# # enumerate(이터러블)
# # 번호를 붙인다.
# li1 = ["김연아", "류현진", "손흥민"]
# for idx, name in enumerate(li1):
#     print(name)



#  print(soup.finf('div')[4])
# print(imgs)
# container = soup.finf('div', attrs = {'id' : 'container'})
# print(container.find_all('img'))


# 셀레니움(selenium)


# 네이버 IT/과학 뉴스 크롤링
import  requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# headers = {"User-Agent" : "Mozilla/5.0"} → 크롤링 방지 회피
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text
soup = BeautifulSoup(html, "html.parser")
div = soup.body.find('div', attrs={'class' : 'list_body'})
headlines = div.find_all('a', attrs={'class': 'cluster_text_headline'})
import os
folder_name = "crauling_result"
if not os.path.exists("crwaling_result"):
    os.mkdir(folder_name)
for headline in headlines:
    # 과제 : crawling_result 폴더의 headlines.txt 파일에 저장하기.
    # with open("crawling_result/headlines.txt", "a", encoding="utf-8") as f:
    # f.write(headline.text.strip())
    # f.write("\n")
    # print(html.text.strip())
    article_response = requests.get(headline['href'])
    aritcle_soup = BeautifulSoup(article_response.text, "html.parser")
    article = aritcle_soup.find('div', attrs={"id": "dic_area"})
    print(article.text)
