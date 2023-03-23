from bs4 import BeautifulSoup

with open('home.html','r') as htmlfile:
    content=htmlfile.read()

    soup=BeautifulSoup(content,'lxml')
    tags=soup.find_all('div',class_="one")
    for course in tags:
          print(course.h1.text.split()[-2])