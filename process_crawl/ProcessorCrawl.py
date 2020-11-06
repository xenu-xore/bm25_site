import os
from multiprocessing import Pool
import requests
import bs4
from run import behavior, HEADERS, SITEMAP2


class CrawlRun(object):
    def __init__(self, url):
        self.url = url

    def data(self):
        """Сбор URL из sitemap для дальнейшего обхода в behavior(data_urls)"""
        dir_url = os.path.exists(self.url)
        if not dir_url:
            c = requests.get(self.url, allow_redirects=True, headers=HEADERS, timeout=5)
            if c.headers['Content-type'] == 'application/xml':

                soup = bs4.BeautifulSoup(c.content, 'html.parser')
                list_urls_s = [i.get_text() for i in soup.find_all('loc')]
                return list_urls_s
            else:
                return behavior(self.url)

        elif dir_url:
            print(self.url)
            with open(self.url, 'r') as f:
                soup = bs4.BeautifulSoup(f, 'html.parser')
                list_urls_s = [i.get_text() for i in soup.find_all('loc')]
                return list_urls_s
        else:
            print('Not URL')


def PoolCrawl(object_pars, n=5):
    try:
        M = CrawlRun(object_pars)
        pool = Pool(n)
        pool.map(behavior, M.data())
    except Exception as e:
        return e
