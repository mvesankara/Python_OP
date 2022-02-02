import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content
print (page)
