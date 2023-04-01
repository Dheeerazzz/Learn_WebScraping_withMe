import requests
from bs4 import BeautifulSoup

html=requests.get('https://quotes.toscrape.com/').content
content=BeautifulSoup(html,"html.parser")
#print(content.text)
def quotefinder():
     mm=[]
     addr= "html body div.container div.row div.col-md-8 div.quote span.text"           
     for i in range (0,10) :
          contents =content.select(addr)
          mm.append(contents)
     return mm
z=quotefinder()
print(z[0])
