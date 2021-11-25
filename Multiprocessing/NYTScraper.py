from bs4 import BeautifulSoup as bs
from multiprocessing import Process
import requests

HOMEPAGE = 'https://www.nytimes.com/'


class NewsScraper:
    def __init__(self):
        pass

    # get headlines from nytimes (as urls)
    def get_headline_urls(self):
        # get the homepage
        raw = requests.get(HOMEPAGE).text

        # make it a soup
        soup = bs(raw, 'lxml')

        # ge all article tags
        articles = soup.find_all('h3')

        # get the a tags with the links --> get the parents
        urls = []

        for article in articles:
            parent_tag = article.parent

            try:
                url = parent_tag['href']
                urls.append(url)
            except TypeError:
                pass
            except KeyError:
                pass

        return urls

    # get text out of url
    def get_url_text(self, url, filename):
        # get the article page
        raw = requests.get(url).text

        soup = bs(raw, 'lxml')

        p_tags = soup.find_all('p')

        # put the p tags into text
        paragraphs = [tag.text for tag in p_tags]

        # write it to a file
        with open(filename, 'a') as infile:
            for paragraph in paragraphs:
                try:
                    infile.write(paragraph)
                except UnicodeEncodeError:
                    pass


if __name__ == '__main__':
    # crate a scraper
    scraper = NewsScraper()

    urls = scraper.get_headline_urls()

    counter = 0

    '''
    # SLOW AND ITERATIVE
    for url in urls[:4]:
        scraper.get_url_text(url, f"{counter}.txt")

        counter += 1
    '''

    # FAST AND MULTIPROCESSED
    article_limit = 5
    processes = []
    for i in range(article_limit):
        p = Process(target=scraper.get_url_text, args=(urls[i], f"{i}.txt"))
        p.start()
        processes.append(p)

    # join the processes
    for p in processes:
        p.join()
