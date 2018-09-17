import requests
from bs4 import BeautifulSoup
import csv

with open('Justin.csv','w',newline='')as f:
    writer=csv.writer(f)
    header=['contribution','date']
    writer.writerow(header)
    for i in range(1,9):
        url='https://github.com/myersjustinc?tab=overview&from=201{number}-01-01&to=201{number}-12-31'.format(number=i)
        r=requests.get(url).text
        data=BeautifulSoup(r,"html.parser")
        information=data.find_all('rect')
        for details in information:
            writer.writerow([details['data-count'],details['data-date']])

