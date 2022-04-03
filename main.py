from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_movie_info(listing_url, links_url, movie_id):
    # tratamento link dos dados gerais do filme
    listing_url= convert_link_to_raw(listing_url)
    html = urlopen(listing_url)
    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find_all('tbody')
    base_inicial= read_date(linhas)
    #fim do tratamento

    #tratamento da bases dos links dos filmes
    links_url= convert_link_to_raw(links_url)
    html = urlopen(links_url)
    bs_links = BeautifulSoup(html, 'html.parser')
    linhas = bs_links.find_all('tbody')
    base_links = read_link(linhas)
    #fim
    # capturando os dados e alocando no dicionário
    movie_id = movie_id.split("/")
    titulo = movie_id[1]
    genero=movie_id[0]
    duracao= "Nao Encontrada"
    link= "Nao Encontrado"
    diretor="Não Encontrado"
    for f in base_inicial:
        if(base_inicial[f]["nome"]==titulo):
            titulo= base_inicial[f]["nome"]
            genero=base_inicial[f]["genero"]
            diretor=base_inicial[f]["diretor"]
            break
    for f in base_links:
        try:
            if(base_links[f][titulo] != None):
                duracao=base_links[f]["duracao"]
                link= base_links[f][titulo]
                break
        except: 
            break
    filme ={
        "url":link,

        "titulo": titulo,
        "genero": genero,
        "diretor":diretor,
        "duracao":duracao
    }
    return filme
    
def read_link(dados):
    base = {}
    k=0
    x=0
    filme= {}
    nome= ""
    link=""
    diretor=""
    duracao=""
    for i in dados:
        filhas = i.findChildren("td")
        for j in filhas:  
                if k == 0:
                    link= j.text
                    duracao =read_duracao(link)
                    k+=1
                else:
                    nome= j.text
                    filme={nome : link, "duracao": duracao}
                    base[x]= filme
                    x+=1
                    k=0
            
    return base
def read_duracao(link):
    link= convert_link_to_raw(link)
    html = urlopen(link)
    bs_link= BeautifulSoup(html, 'html.parser')
    linhas = bs_link.find_all('dd')
    return linhas[1].text
    

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
def convert_link_to_raw(link):
    link = link.split("/")
    link = link[0]+'//'+link[2]+'/raw/'+link[3]
    return link
        
print(get_movie_info("https://pastebin.com/PcVfQ1ff","https://pastebin.com/Tdp532rr", "terror/a vila"))