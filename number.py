import requests
import re
import urllib
from lxml import etree
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import csv
#name = sys.argv[1]
#2017_3
name = []
result = []
z=0
for i in [4,3,2,1]:
    content = "2017_"+str(i)
    name.append(content)
for i in [12,11,10]:
    content = "2016_"+str(i)
    name.append(content)

for k in name:
    print(str(k))
    url = "http://lotto.auzonet.com/biglotto/list_"+str(k)+".html"
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")
    table = soup.find_all('table', attrs={'class':'history_awards'})
    for tableI in table:
        res=[]
        i = 0
        for tdd in tableI.find_all('tr'):
            content = re.sub('\n', ' ', tdd.text)
            content = re.sub(',', '', content)
            res = content.split(' ')
            if (i ==1):
                result.append(res);
            i = i+1
    
    for em in soup.find_all("em"):
        content = re.sub('\$', '', em.text)
        content = re.sub(',', '', content)
        result[z][0] = content
        z=z+1
f = open("number.csv","w")  
w = csv.writer(f)  
w.writerows(result)
f.close() 
