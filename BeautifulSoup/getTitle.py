from bs4 import BeautifulSoup
import requests


def find_title(url):
    link_stuff = requests.get(url).text
    soup = BeautifulSoup(link_stuff, 'lxml')

    title = soup.find('title').text

    return title


link = input('Enter a link: ')

site_title = find_title(link)
print(f"The title of {link} is {site_title}")
