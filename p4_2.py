import re
import requests
from bs4 import BeautifulSoup
r= requests.get("https://www.hamrah-mechanic.com/carprice/")

soup = BeautifulSoup(r.text, 'html.parser')
data = []

regex = re.compile('.*carsBrandPriceList_price.*')
for EachTable in soup.find_all("table", {"class" : regex}):
    table_body = EachTable.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values


for d in data :
    print("Name: %s , Price: %s" %(d[0],d[1]))