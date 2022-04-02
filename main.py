from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_movie_info(listing_url, links_url, movie_id):
   
    filme = {
        "url": "https://pastebin.com/26ApMRdm",
        "titulo": "a vila",
        "genero": "terror",
        "diretor": "reginaldo catarino",
        "duracao": "02:12"
    }
    html = urlopen(listing_url)
    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find_all('tbody')
    base = read_date(linhas)
    print(base)
    

def read_date(dados):
    base = {}
    k=0
    x=0
    filme= {}
    nome= ""
    genero=""
    diretor=""
    for i in dados:
        filhas = i.findChildren("td")
        for j in filhas:
                if k == 0:
                    genero= j.text
                    k+=1
                elif k == 1:
                    nome= j.text
                    k+=1
                else:
                    diretor= j.text
                    filme={"nome" : nome, "genero": genero, "diretor": diretor}
                    base[x]= filme
                    x+=1
                    k=0
            
    return base
get_movie_info("https://pastebin.com/raw/PcVfQ1ff","https://pastebin.com/raw/Tdp532rr", "terror/a vila")