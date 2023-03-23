from bs4 import BeautifulSoup

with open('home.html','r') as htmlfile:
    content=htmlfile.read()
 #   print(content)
    soup=BeautifulSoup(content,'lxml')
    tags=soup.find_all('h1')
    for info in tags:
        print(info.text)
 #   print(tags)
 #   print(soup.prettify)
