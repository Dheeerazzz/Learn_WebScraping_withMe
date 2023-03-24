from bs4 import BeautifulSoup
import requests

url='https://www.amazon.in/s?k=clothes+for+dogs&crid=1EI24QJ4KBODX&sprefix=clothes+for%2Caps%2C359&ref=nb_sb_ss_ts-doa-p_8_11'
headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.5'})
htmltext=requests.get(url,headers=headers).content
soup=BeautifulSoup(htmltext,'lxml')
links=soup.find_all("a",attrs={'class':"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
link=links[0].get('href')
listi="https://amazon.in"+link
print(listi)