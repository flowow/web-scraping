import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
base_url="https://www.featuredcustomers.com/vendor/sap/testimonials?p={}"
d=pd.DataFrame()
c=[]
for i in range(1,13):
    url=base_url.format(i)
    req = urllib.request.Request(url,
                                 headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()
    text = response.decode('utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    industries = soup.select('div.half_width>span')
    b = []
    for industry in industries:
        field = industry.get_text()
        a = field.split(sep="Employees")
        b += a #한페이지의 전체 크롤링 리스트
    print(len(b))
    c=c+b
print(len(c))
all=pd.DataFrame(c)

#creating new dataset by 'Company size' and 'Industry' with scraped data from the web
s=all[0].value_counts()
ds=dict(s)
print(ds)
wanted_keys=['10,000+ ', '1001-5000 ', '5001-10,000 ',\
'11-50 ', '201-500 ', '51-200 ','501-1000 ','1-10 ']
size={k: ds[k] for k in set(wanted_keys) & set(ds.keys())}
print(size)

for i in set(wanted_keys):
    del(ds[i])
del(ds[''])
industry=ds
#Now, we get the dataset size{}, industry{} that get to know features of SAP's customers



"""
https://www.featuredcustomers.com/vendor/sap/testimonials
https://www.featuredcustomers.com/vendor/sap/testimonials?p=2
https://www.featuredcustomers.com/vendor/sap/testimonials?p=12

body > div.tab_links_bg.clearboth > div:nth-child(2) >
div > div > div > div.tab_link_right > div.tab_link_right_inner >
div.testimonials_bg.clearboth.premium_border > div:nth-child(2) >
div.testi_box_left.premium_border_right > div:nth-child(3) > span

body > div.tab_links_bg.clearboth > div:nth-child(2) >
div > div > div > div.tab_link_right > div.tab_link_right_inner >
div.testimonials_bg.clearboth.premium_border > div:nth-child(3) >
div.testi_box_left.premium_border_right > div:nth-child(3) > span

body > div.tab_links_bg.clearboth > div:nth-child(2) >
div > div > div > div.tab_link_right > div.tab_link_right_inner >
div.testimonials_bg.clearboth.premium_border > div:nth-child(4) >
div.testi_box_left.premium_border_right > div:nth-child(3) > span

body > div.tab_links_bg.clearboth > div:nth-child(2) > 
div > div > div > div.tab_link_right > div.tab_link_right_inner > 
div.testimonials_bg.clearboth.premium_border > div:nth-child(19) > 
div.testi_box_left.premium_border_right > div.half_width > span
"""
# %matplotlib inline
# import matplotlib.pyplot as plt
