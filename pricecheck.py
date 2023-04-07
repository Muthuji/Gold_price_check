from bs4 import BeautifulSoup as Bs
import requests
import re

def price(url):
    page=requests.get(url, verify=False ,timeout=10)
    soup=Bs(page.text ,'html.parser')
    ans=soup.find("div",class_='rate slide-rates').text
    Price=re.search('Gold.*', ans)
    return Price.group()
    
url="https://www.grtjewels.com/"
ans=price(url)
print(ans)
