from bs4 import BeautifulSoup
import requests
ProductUrl=[]
url='https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
htmltext=requests.get(url,headers=headers).content
soup=BeautifulSoup(htmltext,'lxml')
showname=soup.select('div:"row" div:"col-sm-12" table:"table_id" tbody tr:"odd" td a')
#links=soup.find_all("a",attrs={'onclick'="prevnext(8421626)"})
for i in showName:
    ProductUrl.append(i.get('href'))

#print(ProductUrl)
for i in ProductUrl:
    print(i)