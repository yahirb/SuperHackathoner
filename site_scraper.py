from bs4 import BeautifulSoup
import requests

# returns current list of hackathons.
def hackathonList():

    url = 'https://mlh.io/seasons/na-2017/events'
    result = requests.get(url)
    c = result.content
    #
    soup = BeautifulSoup(c, 'html.parser')
    hackathon_divs = soup.find_all("div", {"class": "event-wrapper"})



    # Create hackathon dictionaries and add to list.
    hackathon_object_list = []
    data = {}
    for div in hackathon_divs:

        soup = BeautifulSoup(str(div), 'html.parser')
        hackathon_a_element = soup.find("a", {"class": "event-link"})
        hackathon_startdate_element = soup.find("meta", {"itemprop": "startDate"})
        hackathon_enddate_element = soup.find("meta", {"itemprop": "endDate"})
        hackathon_city_element = soup.find("span", {"itemprop": "addressLocality"})
        hackathon_state_element = soup.find("span", {"itemprop": "addressRegion"})


        hackathon_object = {}
        hackathon_object['title'] = hackathon_a_element['title']
        hackathon_object['url'] = hackathon_a_element['href']
        hackathon_object['startDate'] = hackathon_startdate_element['content']
        hackathon_object['endDate'] = hackathon_enddate_element['content']
        hackathon_object['city'] = hackathon_city_element.text
        # replace() removes white space that may be present.
        hackathon_object['state'] = hackathon_state_element.text.replace(" ", "")

        # High School Tag
        if soup.find("div", {"class": "ribbon yellow"}):
            hackathon_highschool_element = soup.find("div", {"class": "ribbon yellow"})
            hackathon_object['highSchoolBoolean'] = hackathon_highschool_element.text
        else:
            hackathon_object['highSchoolBoolean'] = ' '

        hackathon_object_list.append(hackathon_object)
    return hackathon_object_list
