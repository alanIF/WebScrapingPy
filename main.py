from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://pastebin.com/PcVfQ1ff")
bs = BeautifulSoup(html, 'html.parser')
