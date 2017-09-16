# encoding:utf-8

import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')  # tornando o encoding utf-8 como padrão


def get(drive, xpath):
    element = WebDriverWait(drive, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    return element


def iniciar_google_drive(path_do_google_drive):
    browser = webdriver.Chrome(path_do_google_drive)
    browser.maximize_window()  # para maximizar janela da página
    # espera implicitamente 20 segundos caso conexão falhe
    browser.implicitly_wait(20)

    return browser


def apertar_botao_mais_comentarios(browser, xpath):
    # return browser.find_element_by_xpath(xpath).click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    n = 0
    try:
        botao = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        browser.execute_script("arguments[0].focus();", botao)  # scrolar até achar elemento botao
        botao.click()
        return 1
    except (TimeoutException, WebDriverException) as e:
        return 0

def obter_comentarios(tupla, n):
    data = tupla[0]
    titulo = tupla[1]
    url = tupla[2]
    browser = iniciar_google_drive('/home/cloves/Documentos/chromedriver')
    browser.get(url)
    r = apertar_botao_mais_comentarios(
        browser, './/button[contains(@class, "glbComentarios-botao-mais")]')
    if r == 0:
        print "=========================================================================="
        print "========= Não foi possível capturar os comentários da página %d  =========" % n
        print "=========================================================================="
        return 0
    lista_comentarios = []
    for comentario in get(
            browser, '//p[contains(@class, "glbComentarios-texto-comentario")]'):
        lista_comentarios.append((data, titulo, url, comentario.text))

    print "================================================================"
    print "========= Comentários da página %d obtidos com sucesso =========" % n
    print "================================================================"

    browser.close()

    return lista_comentarios


def salvar_comentarios(tuplas):
    df = pd.DataFrame(tuplas, columns=['data', 'titulo', 'url', 'comentario'])
    df.to_excel('comentarios.xlsx', header=True, index=False)

