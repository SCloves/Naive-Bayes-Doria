# encoding:utf-8

from tools import obter_comentarios, salvar_comentarios
import pandas as pd


def main():
    df = pd.read_excel('urls.xlsx')
    urls = df['url'].tolist()
    comentarios = []
    for i in range(len(urls)):
        c = obter_comentarios(urls[i], i)
        comentarios += c

    salvar_comentarios(comentarios)


if __name__ == '__main__':
    main()
