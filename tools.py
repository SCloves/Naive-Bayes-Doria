# encoding:utf-8

import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

reload(sys)
sys.setdefaultencoding('utf-8') # tornando o encoding utf-8 como padrão  

def esperar(drive, xpath):
    element = WebDriverWait(drive, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    return element

def iniciar_google_drive(path_do_google_drive):
    browser = webdriver.Chrome(path_do_google_drive)
    browser.maximize_window() # para maximizar janela da página
    browser.implicitly_wait(20) # espera implicitamente 20 segundos caso conexão falhe

    return browser 

def apertar_botao_mais_comentarios(browser, xpath):
    #return browser.find_element_by_xpath(xpath).click()
    n = 0
    try:
        elemento = WebDriverWait(browser, 20).until(
                                        EC.element_to_be_clickable((By.XPATH, xpath))
                                      )
        elemento.click()
        print "================================================================"
        print "= Butão 'Carregar mais comentários' foi clicado com sucesso!!! ="
        print "================================================================"
    except (TimeoutException, WebDriverException) as e:
        n += 1
        if n == 5:
            print 'Não foi possível apertar o maldito butão!'
            return None
        apertar_botao_mais_comentarios(browser, xpath)



def obter_comentarios(url, n):
    browser = iniciar_google_drive('/home/cloves/Documentos/chromedriver')
    browser.get(url)
    apertar_botao_mais_comentarios(browser, './/button[contains(@class, "glbComentarios-botao-mais")]')
    lista_comentarios = []
    for comentario in esperar(browser, '//p[contains(@class, "glbComentarios-texto-comentario")]'):
        lista_comentarios.append(comentario.text)

    print "================================================================"
    print "========= Comentários da página %d obtidos com sucesso =========" % n
    print "================================================================"

    browser.close()

    return lista_comentarios

def salvar_comentarios(lista_comentarios):
    arquivo = open('comentariosG1.txt', 'w')
    for item in lista_comentarios:
        #arquivo.write("%s\n" % item)
        print>>arquivo, item
    arquivo.close()





