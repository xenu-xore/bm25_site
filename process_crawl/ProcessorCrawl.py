from multiprocessing import Pool
import requests
import bs4
from run import behavior, HEADERS, SITEMAP, URL


class CrawlRun(object):
    def __init__(self, url):
        self.url = url

    def data(self):
        """Сбор URL из sitemap для дальнейшего обхода в behavior(data_urls)"""
        try:
            c = requests.get(self.url, allow_redirects=True, headers=HEADERS, timeout=5)
            if c.headers['Content-type'] == 'application/xml':
                soup = bs4.BeautifulSoup(c.content, 'html.parser')
                list_urls_s = [i.get_text() for i in soup.find_all('loc')]
                return list_urls_s
            else:
                return behavior(self.url)

        finally:
            try:
                with open(self.url, 'r') as f:
                    soup = bs4.BeautifulSoup(f, 'html.process_crawl')
                    list_urls_s = [i.get_text() for i in soup.find_all('loc')]
                    return list_urls_s
            except Exception as e:
                if e == 'Errno 22':
                    print(e)
                    pass


def PoolCrawl(object_pars,n=5):
    try:
        M = CrawlRun(object_pars)
        pool = Pool(n)
        pool.map(behavior, M.data())
    except:
        pass