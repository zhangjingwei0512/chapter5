import requests
from bs4 import BeautifulSoup
import csv

contribution_1=[]
contribution_2=[]
date=[]

for i in range(1,9):
    url_1='https://github.com/myersjustinc?tab=overview&from=201{number}-01-01&to=201{number}-12-31'.format(number=i)
    r_1=requests.get(url_1).text
    data_1=BeautifulSoup(r_1,"html.parser")
    information_1=data_1.find_all('rect')
    for details_1 in information_1:
        date.append(details_1['data-date'])
        contribution_1.append(details_1['data-count'])

for j in range(1,9):
    url_2='https://github.com/hupili?tab=overview&from=201{number}-01-01&to=201{number}-12-31'.format(number=j)
    r_2=requests.get(url_2).text
    data_2=BeautifulSoup(r_2,"html.parser")
    information_2=data_2.find_all('rect')
    for details_2 in information_2:
        contribution_2.append(details_2['data-count'])

with open('furthur1.csv','w',newline='') as f:
    writer=csv.writer(f)
    header=['','myersjustic','hupili']
    writer.writerow(header)
    for i in range (0,len(contribution_2)):
        writer.writerow([date[i],contribution_1[i],contribution_2[i]])