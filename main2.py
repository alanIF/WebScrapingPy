from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_movie_info(listing_url, links_url, movie_id):
    movie_id = movie_id.split("/")
    titulo = movie_id[1]
    genero=movie_id[0]
    # tratamento link dos dados gerais do filme
    listing_url= convert_link_to_raw(listing_url)
    html = urlopen(listing_url)
    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find_all('tbody')
    filme_dados_gerais= get_dados_gerais_filme(linhas,titulo)
    #fim do tratamento

    #tratamento da bases dos links dos filmes
    links_url= convert_link_to_raw(links_url)
    html = urlopen(links_url)
    bs_links = BeautifulSoup(html, 'html.parser')
    linhas = bs_links.find_all('tbody')
    filme_dados_especificos = read_link(linhas,titulo)
    #fim
    filme ={
        "url":filme_dados_especificos[titulo],
        "titulo": titulo,
        "genero": genero,
        "diretor":filme_dados_gerais["diretor"],
        "duracao":filme_dados_especificos["duracao"]
    }
    return filme
  
    
    
def read_link(dados,titulo):
    k=0 
    filme= {}
    nome= ""
    link=""
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
                    if(nome==titulo):
                        return filme
                    k=0
            
    return False
def read_duracao(link):
    link= convert_link_to_raw(link)
    html = urlopen(link)
    bs_link= BeautifulSoup(html, 'html.parser')
    linhas = bs_link.find_all('dd')
    return linhas[1].text
    

def get_dados_gerais_filme(dados,titulo):
    k=0
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
                    if(filme["nome"]==titulo):
                        return filme
                    k=0
            
    return false
def convert_link_to_raw(link):
    link = link.split("/")
    link = link[0]+'//'+link[2]+'/raw/'+link[3]
    return link
        
print(get_movie_info("https://pastebin.com/PcVfQ1ff","https://pastebin.com/Tdp532rr", "terror/a vila"))