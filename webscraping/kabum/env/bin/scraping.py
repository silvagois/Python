# Import
from gettext import gettext
from multiprocessing.sharedctypes import Value
from traceback import print_tb
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
import os 

path = r"C:/Users/016110631/Documents/python/df.csv"
url = "https://www.kabum.com.br/espaco-gamer/cadeiras-gamer"


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
          (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)

#instanciando o objeto beautifulsoup e fazendo o parser da pagina
soup = BeautifulSoup(site.content, 'html.parser')

# coletando a quantidade de intens total da pagina e obtendo o texto
qt_produtos = soup.find('div', id='listingCount').get_text().strip()

# qtd_itens_pagina = soup.find('select', class_='sc-gicCDI hZZNVR').get_text().strip()

#print(qt_produtos[0:4])

# encontrando a posicao do espaco em branco no texto da variavel qt_produtos
index = qt_produtos.find(' ') # posicao do index no caso do espaco em branco
qtd = qt_produtos[:index] # adicionando a informacao ate o espaco em branco , quantidade de produtos
#print(qtd)

ultima_pagina = math.ceil(int(qtd) / 20) # ceil arredonda para cima

# Criando dicionario para fazer o append e criar um data frame 
dicionario_produtos = {
    'marca':[],
    'preco':[]
}

# Percorrendo todas as paginas
for i in range(1,ultima_pagina+1):
    # alterando o pagenumber para receber o i interador do laço
    url_pagina = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pagina, headers=headers)
    #instanciando o objeto beautifulsoup e fazendo o parser da pagina
    soup = BeautifulSoup(site.content, 'html.parser')
    
    # find_all para procurar em todos os produtos
    # usando o re.compile como regex para trazer parte de uma string no caso productCard
    produtos = soup.find_all('div', class_=re.compile('productCard'))

    # Interação para cada produto dentro da pagina 
    for produto in produtos:
        # Obtendo a descrição e marca de cada produto da página
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()

        print(marca, preco)

        dicionario_produtos['marca'].append(marca)
        dicionario_produtos['preco'].append(preco)

    print(url_pagina)

df = pd.DataFrame(dicionario_produtos)
#df.to_csv(path, encoding='utf-8',sep= ';', index= False,)
df.to_csv(path, encoding='utf-8-sig',sep= ';', index= False,)