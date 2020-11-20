import requests
import re


class Crawler:
    def __init__(self):
        self.search_url = 'http://www.google.com/search?q=cnpj '
        self.cnpj_pattern = r'[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}'

    def remove_duplicates(self, cnpjs):
        return list(set([re.sub('[^0-9]', '', cnpj) for cnpj in cnpjs]))

    def regex_cnpj(self, text):
        return re.findall(self.cnpj_pattern, text)

    def request_cnpj(self, name):
        res = requests.get(self.search_url + name)
        return {'status': res.status_code, 'text': res.text}

    def main(self, name):
        res = self.request_cnpj(name)

        if res['status'] == 200:
            cnpj_list = self.remove_duplicates(self.regex_cnpj(res['text']))
            if cnpj_list:
                return {'status': 200, 'cnpjs': cnpj_list}
            else:
                return {'status': 404, 'cnpjs': []}
        else:
            return {'status': 400, 'cnpjs': []}
