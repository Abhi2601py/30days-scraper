import requests
from bs4 import BeautifulSoup

res=requests.get("https://quotes.toscrape.com/")
#print(res.status_code)
#print(res.text[:500])
soup=BeautifulSoup(res.text,'html.parser')
quotes=soup.find_all('div',class_='quote')
print(len(quotes))

print(quotes[0].prettify()[:500])

data=[]
for quote in quotes:
    text=quote.select_one('.text').text
    author=quote.select_one('.author').text
    print(f'{text}-{author}')
    data.append([text,author])

import csv
with open('file.csv','w',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(['col1','col2'])
    writer.writerow(['value1','value2'])
    writer.writerow(['Quote','Author'])
    writer.writerow(data)
