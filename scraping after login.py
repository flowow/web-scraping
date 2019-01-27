#태그 속성 중 클래스,아이디로 추출 하는 scraping
#실습: 로그인 후, 영화, 특정 검색어에 대한 질의 응답 부분 (더나아가면 자연어처리 형태소분석)

#css(스타일시트-용이한 작업을 위해 반복될 부분을 지정) 선택자

from bs4 import BeautifulSoup
fp=open("asos.html", encoding='utf-8')
soup=BeautifulSoup(fp,'html.parser')
print(soup)

#sel이라는 람다 함수 q변수에 전달된 문자열(태그,id 등)에 해당하는 데이터 추출
sel=lambda q:print(soup.select_one(q).string)
            #같은 표현법
sel("#dl")
sel("li#dl")
sel("ul>li#dl") #ul태그의 자식 태그 중 id가 dl인 태그
#태그 말고 아이디만으로 찾는 법
sel("#programming #dl") #programming 하위에 dl 띄어쓰기 꼭
sel("ul#programming li#dl")
sel("li[id='dl']")
sel("li:nth-of-type(4)") #nth는 0부터가 아니라 1부터
print(soup.select("li")[2].string)
print(soup.find_all("li")[3].string)

# myList=soup.select("li")
# for li in myList:
#     value=li.string
#     print(value)

fp2=open("frve.html", encoding='utf-8') #euc-kr, iso8859
soup=BeautifulSoup(fp2, 'html.parser')
print(soup)
print(soup.select_one("li:nth-of-type(3)").string)
print(soup.select_one("#fr-list>li:nth-of-type(3)").string)
#select_one은 최초의 하나만 추출하기에 결과 '파프리카'
print(soup.select_one("#ve-list>li[data-lo='us']").string)
#속성[data-lo="us"]대괄호 안쪽은 홑따옴표, 바깥은 곁
print(soup.select("#ve-list>li[data-lo='us']")[1].string)
print(soup.select("#ve-list>li.black")[1].string)


from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
########태그를 알아야 추출한다!!!!!! 죽 마일리지와 한빛이코인의 태그를 알아야한다
"""http://www.hanbit.co.kr/index.html
http://www.hanbit.co.kr/member/login.html
http://www.hanbit.co.kr/member/login_proc.php
http://www.hanbit.co.kr/myhanbit/myhanbit.html
"""
user="fjgvg"
pw="852456!!!"

#세션(웹서버와 클라이언트간의 연결) 시작하기
#세션이 유지(연결 상태), 세션 정보(연결(id/pw...) 정보)
#세션 유지 시간(클라이언트가 별도의 동작 없이도 서버와 연결을 유지하는 시간)
#세션 해제(종료):일정 시간이 경과되어 서버<->클라이언트 연결해제
session=requests.session() #세션객체가 만들어짐 접속된 거X
login_info={"m_id":user, "m_passwd":pw}

            # 접속
url_login="http://www.hanbit.co.kr/member/login_proc.php"
#get방식:url에 전달되는 인수가 출력됨(속도)
#post방식:url에 전달되는 인수가 출력이 안 됨(but보안성good) 개인정보같은 민감한 정보는 주소에 숨겨져야 하므로
res=session.post(url_login, data=login_info) #서버 연결됨(세션 만들어짐)
print(res)
url_mypage="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res=session.get(url_mypage)
print(res)
soup=BeautifulSoup(res.text, "html.parser")
print(soup)

#마일리지 선택자: #container > div > div.sm_mymileage > dl.mileage_section1 > dt
#이코인 선택자: #container > div > div.sm_mymileage > dl.mileage_section2 > dt
url_mil="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
url_coin="#container > div > div.sm_mymileage > dl.mileage_section2 > dt"
res=session.get(url_mil)
soup=BeautifulSoup(res.text,"html.parser")
mil=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dt")
print(mil)
