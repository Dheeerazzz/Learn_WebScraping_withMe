from bs4 import BeautifulSoup
import requests

htmltext=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
print(htmltext)