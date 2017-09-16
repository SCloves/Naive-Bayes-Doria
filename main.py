# encoding:utf-8

from tools import obter_comentarios, salvar_comentarios
import pandas as pd


def main():
    df = pd.read_excel('urls.xlsx')
    df['data'].replace(u' ' ,'None', inplace=True)
    tuplas = [tuple(x) for x in df.to_records(index=False)]
    comentarios = []
    try:
        for i in range(len(tuplas)):
            c = obter_comentarios(tuplas[i], i)
            if c != 0:
                comentarios += c

        salvar_comentarios(comentarios)
        print "================================================================"
        print "======== Todos os Comentários foram salvos com sucesso ========="
        print "================================================================"
    except:
        salvar_comentarios(comentarios)
        print "================================================================"
        print "====== Erro! Mas comentários foram salvos até a página %d ======" %(i-1)
        print "================================================================"

if __name__ == '__main__':
    main()
