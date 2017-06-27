from bs4 import BeautifulSoup
import requests

url = 'https://mlh.io/seasons/na-2017/events'
result = requests.get(url)
c = result.content

soup = BeautifulSoup(c, 'html.parser')
hackathon_divs = soup.find_all("div", {"class": "event-wrapper"})
print (hackathon_divs[0])
