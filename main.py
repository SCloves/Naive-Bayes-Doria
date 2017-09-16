# encoding:utf-8

from tools import obter_comentarios, salvar_comentarios
import pandas as pd


def main():
    df = pd.read_excel('urls.xlsx')
    urls = df['url'].tolist()
    comentarios = []
    try:
        for i in range(len(urls)):
            c = obter_comentarios(urls[i], i)
            if c != 0:
                comentarios += c

        salvar_comentarios(comentarios)
    except:
        salvar_comentarios(comentarios)

if __name__ == '__main__':
    main()
