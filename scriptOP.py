import csv
import requests
from bs4 import BeautifulSoup
url = "https://www.it-connect.fr/actualites/"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, 'html.parser')

titres = soup.find_all("h2", class_="entry-title")
titres_textes = []
for titre in titres:
    titres_textes.append(titre.string)


descriptions = soup.find_all("div", class_="entry-content clearfix")
descriptions_textes = []
for description in descriptions:
    descriptions_textes.append(description.string)

en_tete = ['titre', 'description']
with open('data.csv', 'w')  as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    for titre, description in zip(titres_textes, descriptions_textes):
        writer.writerow([titre, description])
