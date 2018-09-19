import requests
from bs4 import BeautifulSoup
import csv

with open('further2(2).csv','w',newline='')as f:
    writer=csv.writer(f)
    header=['month','detail']
    writer.writerow(header)
    for i in range(1,9):
        for j in range(1,13):
            if i==8 and j>9:
                break
            else:
                url='https://github.com/myersjustinc?tab=overview&from=201{0}-{1:02d}-01&to=201{0}-{1:02d}-31'.format(i,j)
                r=requests.get(url).text
                data=BeautifulSoup(r,"html.parser")
                month_1='201{0}/{1:02d}'.format(i,j)
                if data.find('span',attrs={'class':'text-gray m-0'})!=None:
                    detail=data.find('span',attrs={'class':'text-gray m-0'}).text.strip()
                    writer.writerow([month_1,detail])
                    continue
                if data.find('span',attrs={'class':'float-left'})!=None:
                    detail=data.find_all('button',attrs={'class':'btn-link f4 muted-link no-underline lh-condensed width-full js-details-target'})
                    for k in range(0,len(detail)):
                        detail_1=detail[k].text.strip().replace('\n           ','')
                        writer.writerow([month_1,detail_1])
                if data.find('h4',attrs={'class':'text-normal text-gray lh-condensed pr-3'})!=None:
                    detail=data.find_all('h4',attrs={'class':'text-normal text-gray lh-condensed pr-3'})
                    for l in range(0,len(detail)):
                        detail_1=detail[l].text.strip().replace('\n     ','')
                        writer.writerow([month_1,detail_1])