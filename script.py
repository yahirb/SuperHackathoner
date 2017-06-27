from lxml import html
import requests

page = requests.get('https://mlh.io/seasons/na-2017/events')
tree = html.fromstring(page.content)

#This will create a list of hackathons:
hackathons = tree.xpath('//h3[@itemprop="name"]/text()')

print ('Buyers: %s,' % hackathons)
