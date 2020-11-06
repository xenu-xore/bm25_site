from count.CountWords import CountModel

HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

URL = 'https://kaffelkrasnodar.ru/'

SITEMAP = 'https://kaffelkrasnodar.ru/sitemap-index.xml'


def behavior(requests):
    """Поведение(обработка) полученых из data() URL"""
    try:
        url = CountModel(requests)
        url.get_the_corpus('bm25', 'плитку')

    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    from process_crawl.ProcessorCrawl import PoolCrawl
    PoolCrawl(URL)
