# testWebScraping
Web Scraping com python
# Descrição do problema
* Juliana, que é uma programadora Python, estava pesquisando algumas coisas na internet
e encontrou várias postagens públicas no https://pastebin.com com o que parecia ser
uma página HTML de uma agência de filmes. Aparentemente nenhum filme listado lá era
real, mas ela achou interessante a disposição das informações nas páginas. Ela pegou
uma das postagens que encontrou e iniciou uma análise mais detalhada. A postagem no
pastebin levou ela à dois links:
- https://pastebin.com/PcVfQ1ff
- https://pastebin.com/Tdp532rr
* O primeiro link ela notou que continha um HTML com o gênero, nome e diretor do filme.
O segundo link ela notou que continha apenas um outro link e o nome do filme. O link
que cada filme continha levava a outro pastebin. Esse último pastebin continha mais
alguns outros detalhes do filme como a duração dele.
* Ela percebeu ainda que cada filme tinha um diretor único e link único, ou seja, não
havia dois filmes com essas informações repetidas. Porém, ela percebeu que um filme
poderia conter nomes iguais embora seus gêneros fossem diferentes. Ou seja, poderia
haver dois ou mais filmes de mesmo nome, porém de gêneros diferentes.
* Juliana então se desafiou a escrever uma função Python get_movie_info que recebe três
strings: uma string que contem o link da primeira listagem, uma segunda string que
recebe o link no pastebin da página que lista a url de cada filme (a segunda listagem)
e uma terceira string no formato: "genero/nome". A função deveria fazer um scrapping
nas páginas e retornar um dicionário contendo todas as informações possíveis do filme,
por exemplo, uma chamada à:
- get_movie_info(
"https://pastebin.com/PcVfQ1ff",
"https://pastebin.com/Tdp532rr",
"terror/a vila"
)
* deveria retornar um dicionário igual a:
- {
"url": "https://pastebin.com/26ApMRdm",
"titulo": "a vila",
"genero": "terror",
"diretor": "reginaldo catarino",
"duracao": "02:12"
}

* Observações: o código precisa ser escrito em Python 3 a resposta ao desafio deve ser entregue no formato zip por email ou um link a um projeto do github, contendo dois arquivos: main.py e requirements.txt , este último contendo as dependências para executar a função.