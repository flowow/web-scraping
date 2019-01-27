"""
스크래핑: 웹 데이터 추출
-파이썬 urllib 라이브러리
"""
            #파일 저장
#urllib패키지(파이썬 파일들 모임) 내부에 request모듈(이 파일 안에 많은 함수들)을 가져와라
import urllib.request
#url지정
url="https://images.asos-media.com/products/" \
    "adidas-originals-three-stripe-long-sleeve-t-shirt-in-black/" \
    "9389795-1-black?$XL$?$XXL$&wid=300&fmt=jpeg&qlt=80,0&op_sharpen" \
    "=0&resMode=sharp2&op_usm=1,0.4,6,1&iccEmbed=0&printRes=72"
#이미지 저장경로
sname="test.png"
#다운로드
urllib.request.urlretrieve(url,sname) #가고싶은 url
print("다운로드 완료")

#request.urlretrieve :다운로드 ->파일 저장
#request.urlopen(): 다운>메모리에 데이터 적재->필요시 파일 저장

url="https://images.asos-media.com/products/" \
    "adidas-originals-three-stripe-long-sleeve-t-shirt-in-black/" \
    "9389795-1-black?$XL$?$XXL$&wid=300&fmt=jpeg&qlt=80,0&op_sharpen" \
    "=0&resMode=sharp2&op_usm=1,0.4,6,1&iccEmbed=0&printRes=72"
#이미지 저장경로
sname="test2.png"
#다운로드
mem=urllib.request.urlopen(url).read() #다운받은 것 메모리에 저장
with open(sname, mode="wb") as f: #이미지는 binary file이라 wb
    f.write(mem)
    print("파일 저장 완료")


"""
정해진 태그를 이용해야하는 html과 달리 
내가 태그를 정의할 수 있는 xml(확장가능한 마크업 언어)로 작성하면 기계가 정보를 받아들일 수 있다
내가 알고싶은 데이터를 태그를 지정해 줄 수 있기 때문에 추출 용이이
"""

import urllib.request
import urllib.parse
addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
values={'stnId':'184'} #제주도 /중괄호 ->딕셔너리
params=urllib.parse.urlencode(values) #parameter 설정 #urllib패키지,parse모듈,urlencode메서드
url=addr+"?"+params
print(url)
            #2.
data=urllib.request.urlopen(url).read()
print(data) #16진수로 나온다 디코딩 필요
text=data.decode("utf-8")
print(text)