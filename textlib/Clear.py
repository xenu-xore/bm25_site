# import stanza
# from spacy_stanza import StanzaLanguage

class ClearText:
    def __init__(self, corpus):
        self.corpus = corpus

    def corpus_text(self):
        trans_table = {ord(c): None for c in u'\r\t'}
        dela = ' '.join(self.corpus).replace('/', '').replace(',', '').replace(';', '').replace(':', '') \
            .replace('/', '').replace("'", '').replace('_', '').replace('-', '').replace('}', '').replace('{', '') \
            .replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('&', '').replace('#', '') \
            .replace('+', '').replace('.', '').replace(']', '').replace('[', '').replace("\'", '').replace("$", '') \
            .replace('"', '').replace('*', '').replace('«', '').replace('»', '').replace('»', '').replace('>', '') \
            .replace('<', '').replace('%', '').replace('|', '').replace('!', '').replace('\\', '').replace('@', '') \
            .replace('~', '')

        res_pos = [i for i, e in enumerate(dela + 'Z') if e.isupper()]
        res_list = [dela[res_pos[j]:res_pos[j + 1]] for j in range(len(res_pos) - 1)]
        corpus_text_reform = [delete_sim.strip().translate(trans_table) for delete_sim in res_list]

        return corpus_text_reform


class lematization(object):
    pass
