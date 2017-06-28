from bs4 import BeautifulSoup
import requests

url = 'https://mlh.io/seasons/na-2017/events'
result = requests.get(url)
c = result.content

soup = BeautifulSoup(c, 'html.parser')
hackathon_divs = soup.find_all("div", {"class": "event-wrapper"})

list_data = []
data = {}
for div in hackathon_divs:

    soup = BeautifulSoup(str(div), 'html.parser')
    hackathon_title_a = soup.find("a", {"class": "event-link"})
    list_data.append(hackathon_title_a)

for elem in list_data:
        print (elem['title'])

print (len(list_data))
