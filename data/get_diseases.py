#!/usr/bin/env python3


#Scrapes a list of diseases and conditions from the CDC's website

from urllib.request import urlopen
from bs4 import BeautifulSoup

diseases = []
for letter in 'abcdefghijklmnopqrstuvwxyz':
    url = "https://www.cdc.gov/diseasesconditions/az/" + letter + ".html"
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    span16 = soup.find('div', class_="span16")
    dis = BeautifulSoup(span16.text.strip())
    for disease in dis.text.replace('\n\n\n','\n').split('\n'):
        diseases.append(disease)

with open("input.txt",'w') as f:
    temp = ('\n').join(diseases)
    f.write(temp)
