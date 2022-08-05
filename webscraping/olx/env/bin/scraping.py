from bs4 import BeautifulSoup
import requests
import pandas as pd

URL= f"https://go.olx.com.br/grande-goiania-e-anapolis/autos-e-pecas/carros-vans-e-utilitarios?me=80000&pe=60000&q=onix&rs=35"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
path = r"C:/Users/016110631/Documents/python/olx.csv"

site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

veiculos = soup.findAll('div', attrs={'class':'sc-12rk7z2-0 bjnzhV'})

dicionario_veiculo={
    'titulo':[],
    'link':[],
    'informacao_anuncio':[],
    'preco_veiculo':[],
    'localizacao':[],
    'data_anuncio':[],
    'qt_fotos_anuncio':[],
}

for veiculo in veiculos:    
    titulo = veiculo.find('h2',attrs={'class':'kgl1mq-0 eFXRHn sc-fzsDOv jiCiNE'}).get_text().strip()
    link = veiculo.find('a', attrs={'class':'sc-12rk7z2-1 huFwya sc-giadOv dXANPZ'})
    informacao_anuncio = veiculo.find('div', attrs={'class':'sc-1ftm7qz-2 ilPFvN'}).get_text().strip()
    preco_veiculo = veiculo.find('span', attrs={'class':'m7nrfa-0 eJCbzj sc-fzsDOv kHeyHD'}).get_text().strip()
    localizacao = veiculo.find('span', attrs={'class':'sc-1c3ysll-1 iDvjkv sc-fzsDOv dTHJIA'}).get_text().strip()
    data_anuncio = veiculo.find('span', attrs={'sc-11h4wdr-0 gBAToP sc-fzsDOv dTHJIA'}).get_text().strip()
    qt_fotos_anuncio = veiculo.find('span', attrs={'sc-1n4y6ur-1 bzUofP sc-fzsDOv bYaEay'}).get_text().strip()
    
    print('Titulo do Veiculo:', titulo)
    #print('Link do Veiculo:', link)
    print('Link do Veiculo:', link['href'])
    print('Informações do Veiculo:', informacao_anuncio)
    print('Localização:', localizacao)
    print('Data Anuncio:', data_anuncio)
    print('Quantidade de fotos anunciadas:', qt_fotos_anuncio)
    print('Preço do Veiculo:', preco_veiculo)

    print('\n\n')

    dicionario_veiculo['titulo'].append(titulo)
    dicionario_veiculo['link'].append(link)
    dicionario_veiculo['informacao_anuncio'].append(informacao_anuncio)
    dicionario_veiculo['preco_veiculo'].append(preco_veiculo)
    dicionario_veiculo['localizacao'].append(localizacao)
    dicionario_veiculo['data_anuncio'].append(data_anuncio)
    dicionario_veiculo['qt_fotos_anuncio'].append(qt_fotos_anuncio)


df = pd.DataFrame(dicionario_veiculo)

# Fazendo split na coluna informacao_anuncio e dividindo em novas colunas
inf_anuncio_split = df['informacao_anuncio'].str.split('|', n=2, expand=True)
df["Km"] = inf_anuncio_split[0]
df["Cambio"] = inf_anuncio_split[1].str.replace('Câmbio:','')
df["Combustivel"] = inf_anuncio_split[2].str.replace('|','')

#print(df["Combustivel"])
df.to_csv(path, encoding='utf-8-sig',sep= ';', index= False,)
#print(dados_veiculo.prettify())





