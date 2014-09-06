from urllib import urlopen
from urlparse import urljoin
import json

URL_BASE = """https://api.educ.ar/0.9/"""

URL_EBOOKS = urljoin(URL_BASE, 'recursos/ebooks')

API_KEY = "40f6f3d814bdfd1bcf96523ee20f578028ea39d9"

def get_json(path, query={}):
    url =  urljoin(URL_BASE, path) + "?q=%s&key=%s" % (json.dumps(query), API_KEY)
    response = urlopen(url).read()
    return json.loads(response)


def get_descripciones_ebooks():
    descripciones = []
    total = None
    n_read = 0
    while total is None or n_read < total:
        res = get_json('recursos/ebooks', {"limit": 10, "offset": n_read})
        result = res['result']

        if not total:
            total = int(result['totalFound'])        
        data = result['data']
        descripciones += data
        n_read += len(data)
        print "read %d" % n_read
    
    return descripciones


def get_ebook(_id):
    pass


def get_categorias_ebooks():
    res = get_json(path='recursos/catalogacion/ebooks')
    return res
    

