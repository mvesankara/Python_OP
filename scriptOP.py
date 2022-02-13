import requests
from bs4 import BeautifulSoup
url = "https://www.it-connect.fr/actualites/"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, 'html.parser')

titres = soup.find_all("h2")
#print(titres)

descriptions = soup.find_all("div", class_="entry-content clearfix")
print(titres, descriptions)
