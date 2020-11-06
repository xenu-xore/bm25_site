from count.CountWords import CountModel
from textlib.Text import PageText
from process_crawl.ProcessorCrawl import *


HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
URL = 'https://vc.ru/'
SITEMAP = 'https://vc.ru/sitemap/standard.xml'

# run process crawling requests - data base is sitemap.xml PoolCrawl(URL, n=7)
def behavior(request):
    url = CountModel(request)
    url.get_the_corpus('bm25', query='купить')


# run process write words for file
def write_file():
    write = PageText('csv')
    write.writeFile(URL)


# Defining logic
if __name__ == "__main__":
    # For sitemap
    #PoolCrawl(SITEMAP)

    # For counting and writing words
    write_file()
