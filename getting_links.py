# encoding:utf-8

import requests
import ast
import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
import re
from sys import argv

def main(url_raiz):
    paginas_noticias_doria = [url_raiz.format(i) for i in range(1,41)]
    print "================================================================"
    print "==================== Capturando dados! ========================="
    print "================================================================"
    informacoes = obter_dics_informacoes(paginas_noticias_doria)
    print "================================================================"
    print "============ Dados salvos em planilha urls.xlsx! ==============="
    print "================================================================"
    salvar_dados_em_excel(informacoes)


def obter_dics_informacoes(paginas):
    lista_dic = []
    for link in paginas:
        lista_dic += pegar_info_pagina(link)
    return lista_dic



def parse_date(lista):
    dates = []
    teste = re.compile('(\d+[-/]\d+[-/]\d+)')
    for date in lista:
        date = date.split()
        if teste.match(date[0]):
            dates.append(date[0])
        else:
            dates.append(' ')
        
    return dates


def pegar_info_pagina(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    titulos = [titulo.text for titulo in soup.findAll("a", attrs={"class":"cor-produto busca-titulo"})]
    datas = parse_date([data.text for data in soup.findAll("span", attrs={"class":"busca-tempo-decorrido"})])
    urls = parse_url([a['href'] for a in soup.find_all('a', attrs={"class":"cor-produto busca-titulo"}, href=True) if a.text.strip()])
    lista_dic = []
    for t, d, u in zip(titulos, datas, urls):
        lista_dic.append({'titulo':t, 'data':d, 'url':u})
    return lista_dic


def salvar_dados_em_excel(lista):
    df = pd.DataFrame(lista)
    df.to_excel('urls.xlsx')
    


def parse_url(lista_urls):
    urls = ['http://' + url[url.find('Fg1') + 1: url.find('&t')].replace('%2F', '/') for url in lista_urls]
    return urls

def parse_date(lista):
    dates = []
    teste = re.compile('(\d+[-/]\d+[-/]\d+)')
    for date in lista:
        date = date.split()
        if teste.match(date[0]):
            dates.append(date[0])
        else:
            dates.append(' ')
        
    return dates

if __name__=="__main__":
    #url_raiz = 'http://g1.globo.com/busca/?q=Jo%C3%A3o+Doria&species=not%C3%ADcias&page={}'
    main(argv[1] + '{}')    
