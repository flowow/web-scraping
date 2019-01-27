#데이터수집->전처리->분석->알고리즘선택->모델링->모델(<-data)->예측/분류 결과
            #bs4모듈에 있는 BeautifulSoup 가져와라(대문자로 시작하면 class)
            #html에서
from bs4 import BeautifulSoup
import urllib.request
#class는 메모리적재가 안 됨 객체 생성해야함
text="""(띄어쓰기 그대로 출력하고 싶을 때)
<html>
<body>
<h1>GERMANY</h1>  
<p>49</p>
<p>BERLIN</p>
<p>international</p>
</body>
</html>
"""
print(text)
#1)BeautifulSoup 객체생성(붕어빵 만들어냄, 분석 결과 즉 추출이 되어있는 것이 아니라 대상의 명시)
#html.parser라는 분석기를 사용하여 html문서를 분석하겠다
soup= BeautifulSoup(text,'html.parser') #html, 분석기=html.분석기=parser
print(soup)
            #soup객체 내부 h1태그로 이동해 값추출
            ###1. 태그로 요소 추출
p1=soup.html.body.p
h1=soup.h1 #h1 여기서는 하나여서 무관하지만 여러개라면 전체 경로를 명시해줘야 한다,
#다음 노드로 이동할 때 (두 번 해줘야 하는 이유는 한 번은 (생략된)줄바꿈 이기 때문에
p2=p1.next_sibling.next_sibling
p3=p2.next_sibling.next_sibling
print("h1태그로 묶인 값:",h1.string)
print("p태그로 묶인 값:",p1.string)
print("태그로 묶인 값:",p2.string)




            ###2.아이디로 요소 추출
text="""(띄어쓰기 그대로 출력하고 싶을 때)
<html>
<body>
<h1 id="title">GERMANY</h1>  
<p id="pos">49</p>
<p id="name">BERLIN</p>
<p id="spc">international</p>
</body>
</html>
"""
soup2=BeautifulSoup(text,'html.parser')
title=soup2.find(id="title") #태그이름으로 접근시에는 점(.)으로 구분해서
name=soup2.find(id="name")
print("나라:",title.string)
print("도시:",name.string)

            ###find_all:여러 개의 태그를 한번에 추출하고 싶은 경우
text="""(띄어쓰기 그대로 출력하고 싶을 때)
<html>
<body>
<ul> #순서가 없는 리스트
<li><a href="http://www.sap.com">sap</a>/li>
<li><a href="http://www.gmail.com">gmail</a>/li>
</ul>
</body>
</html>
"""
soup3=BeautifulSoup(text, 'html.parser')
links= soup3.find_all("a")#a에관한 모든 걸 파싱하라
for a in links: #각 a태그에 해당하는 목록들이
              # <태그 속성명=속성값1...>내용</태그>
    # print(a) #---><a href="http://www.naver.com">naver</a>
    # print(a.attrs['href'])#속성에 해당하는 값만 나옴
    # print(a.string)
              hr=a.attrs['href']
              con=a.string
              print(con, "--->",hr)

addr= "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res=urllib.request.urlopen(addr)
print(res)
soup9=BeautifulSoup(res,'html.parser')
#url open 후 read까지 하는 방법 그 data를 디코딩해서
#그냥 옾픈해서 beautifulsoup이 읽어오도록 해서 출력
print(soup9) #페이지 내용이 모두 출력
#다음은 디코딩으로 불러오는 예시
# data=urllib.request.urlopen(url).read()
# print(data) #16진수로 나온다 디코딩 필요
# text=data.decode("utf-8")
# print(text)

            #wf포함태그 추출하고 싶다?
wf=soup9.find("wf")
print(wf)

            #css
#             info.finance.naver.com/marketindex
# https://finance.naver.com/marketindex/worldExchangeDetail.nhn?marketindexCd=FX_GBPUSD

#ex)span 태그 이름과 class 알아야 해당 내용 추출할 수 있다
text="""(띄어쓰기 그대로 출력하고 싶을 때)
<html>
<body><div id="myid">
<h1>데이터 추출</h1>
<ul class="items">
<li>머신러닝</li>
<li>딥러닝</li>
<li>강화학습</li>
</ul>
</div>
</body>
</html>
"""
soup8=BeautifulSoup(text,'html.parser')
h1=soup8.select_one("div#myid > h1").string #'#'은 아이디를 의미함 마이아이디를 그 뒤에 써줌 그러면 myid로 접근ㅇㅇ
#'>'를 통해 hi 하부로 들어감을 의미
print(h1)

#이제 전부를 뽑아보자
myList=soup8.select("div#myid > ul.items > li") # .기준 왼쪽 태그 오른쪽 class 태그#id >태그.class>...
print(myList) #리스트로 출력되기에 for문 가능
for li in myList:
    print(li.string)

import urllib.request as rep#(이를 rep라고 하자. 그러면 반복되는 urllib.request대신 축약형으로 이용 가능
url="https://finance.naver.com/marketindex/"
#url 오픈메서드
#urllib.request.urlopen()
#rep.urlopen(url)
res=rep.urlopen(url)
#BeautifulSoup(res,'html.parser')
soup=BeautifulSoup(res,'html.parser')
#soup.select_one("div.head_info point_up>span.value").string
price=soup.select_one("div.head_info > "
                      "span.value").string
#추출목표: div.head_info point_up>span.value
print("파운드",price)
