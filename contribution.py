import requests
from bs4 import BeautifulSoup
import csv
import pandas 

header=['','PepperCai','DidoChan','Shinonomee','Jasmine-dudu','FLYSTEPHEN','guminyi','trista520','Rita0719','Wong-Ming','18408532','clairelau0108','hakutoccino','JIEYI22','coolxu8888','AlexZenghuashan','zacharyzeng','ZhangNingNina','elusiveburglar','maggie0114','efncij','Lsn-cecilia','shiyuning0987','ivywang958','kaiwenxu94','warrior960812','Yang9305','lullabymia','yaonuan1995','18426425','Zmh951010','ZHANGboh','ZhangHuimin97','zhangjingwei0512','NicoleZZC']

list=[]
for i in range(0,len(header)):
    list.append([])

for i in range(0,len(header)):
    if i==0:
        url='http://github.com/zhangjingwei0512'
        r=requests.get(url).text
        data=BeautifulSoup(r,"html.parser")
        information=data.find_all('rect')
        for j in range(330,len(information)):
            list[i].append(information[j]['data-date'])
    else:
        url='https://github.com/{0}'.format(header[i])
        r=requests.get(url).text
        data=BeautifulSoup(r,"html.parser")
        information=data.find_all('rect')
        for j in range(330,len(information)):
            list[i].append(information[j]['data-count'])

with open('contribution.csv','w',newline='') as f:
    writer=csv.writer(f)
    header=['','PepperCai','DidoChan','Shinonomee','Jasmine-dudu','FLYSTEPHEN','guminyi','trista520','Rita0719','Wong-Ming','18408532','clairelau0108','hakutoccino','JIEYI22','coolxu8888','AlexZenghuashan','zacharyzeng','ZhangNingNina','elusiveburglar','maggie0114','efncij','Lsn-cecilia','shiyuning0987','ivywang958','kaiwenxu94','warrior960812','Yang9305','lullabymia','yaonuan1995','18426425','Zmh951010','ZHANGboh','ZhangHuimin97','zhangjingwei0512','NicoleZZC']
    writer.writerow(header)
    for i in range(0,len(list[0])):
        writer.writerow([list[0][i],list[1][i],list[2][i],list[3][i],list[4][i],list[5][i],list[6][i],list[7][i],list[8][i],list[9][i],list[10][i],list[11][i],list[12][i],list[13][i],list[14][i],list[15][i],list[16][i],list[17][i],list[18][i],list[19][i],list[20][i],list[21][i],list[22][i],list[23][i],list[24][i],list[25][i],list[26][i],list[27][i],list[28][i],list[29][i],list[30][i],list[31][i],list[32][i],list[33][i],list[34][i]])

df=pandas.read_csv('contribution.csv')
a=df.sum(skipna=False)
b=a.iloc[1:]
c=b.sort_values(ascending=False)
print(c)
c.to_csv('sort.csv',header='contribution')