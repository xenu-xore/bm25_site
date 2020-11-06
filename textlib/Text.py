from bs4 import BeautifulSoup
import requests
from collections import Counter
import csv
import json
import codecs


class PageText:
    def __init__(self, format_doc):
        self.format_doc = format_doc

    def writeFile(self, url):
        def generatorFunc():
            if self.format_doc == 'csv' or self.format_doc == 'txt' or self.format_doc == 'json' \
                    or self.format_doc == 'default' or self.format_doc == 'bm25':
                req = requests.get(url)
                responses = req.content
                page_text = BeautifulSoup(responses, 'html.parser')
                result = page_text.get_text(strip=False)
                result2 = result.split('\n')
                general = (i for i in result2)
                for i in general:
                    if i != '':
                        yield i
            else:
                print('Unknown format')

            return generatorFunc

        if self.format_doc == 'csv':
            with open('format.csv', mode='w', encoding='utf-8') as f:
                c = Counter(generatorFunc())
                file_write = csv.writer(f, delimiter=";", lineterminator="\r")
                [file_write.writerow((s, c[str(s)])) for s in c.keys()]
                print('Done csv')

        elif self.format_doc == 'json':
            with codecs.open('format.json', 'w', encoding='utf-8') as f:
                c = Counter(generatorFunc())
                dicts = json.dumps(c, ensure_ascii=False)
                f.write(str(dicts))
                print('Done json')

        elif self.format_doc == 'txt':
            with codecs.open('format.txt', 'w', encoding='utf-8') as f:
                c = Counter(generatorFunc())
                [f.write(str(k) + ' ' + str(v) + '\n') for k, v in c.items()]
                print('Done txt')

        elif self.format_doc == 'default':
            with codecs.open('default.txt', 'w', encoding='utf-8') as f:
                for i in generatorFunc():
                    f.write(i + ' ')
                print('Done default')

        elif self.format_doc == 'bm25':
            list_corpus = [i for i in generatorFunc()]
            return list_corpus

        else:
            print('Unknown format')
