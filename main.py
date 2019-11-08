from bs4 import BeautifulSoup
import requests
import ssl



coins = [0,1,14]

priceReq = requests.get('https://coinranking.com')


soup = BeautifulSoup(priceReq.text,'html.parser')



for coin in coins:
    #profile link had two underscores in class name
    
    names = soup.findAll('a', {'class': 'profile__link'})[coin].text.strip()
    price = soup.findAll('td',{'class':'table__cell table__cell--2-of-8 table__cell--s-3-of-10'})[coin].findAll('div',{'class':'valuta'})[0].text.replace("$","").replace("\n","")
    print(names + price)


 




