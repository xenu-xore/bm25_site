from count.CountWords import CountModel
from textlib.Text import PageText

HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}
URL = 'https://vc.ru/sitemap/standard.xml'
SITEMAP = 'https://vc.ru/sitemap/standard.xml'


# Запустить процес краулинга requests - data base is sitemap.xml
# def behavior(requests):
#    url = CountModel(requests)
#    url.get_the_corpus('bm25', query='купить')

# Запустить процес подсчета слов
def write_file():
    write = PageText('txt')
    write.writeFile('https://dolgoletmed.ru/uslugi-i-tseny/')


# Определение логики
if __name__ == "__main__":
    # Для sitemap
    # from process_crawl.ProcessorCrawl import PoolCrawl
    # PoolCrawl(URL, n=7)
    # Для подсчета и записи слов
    write_file()
