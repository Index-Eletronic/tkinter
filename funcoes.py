
c = ('\033[m',         # cor 0 = sem cores
     '\033[0;30;41m',  # cor 1 = Vermelho
     '\033[0;30;42m',  # cor 2 = Verde
     '\033[0;30;43m',  # cor 3 = Amarelo
     '\033[0;30;44m',  # cor 4 = Azul
     '\033[0;30;45m',  # cor 5 = Roxo
     '\033[7;30m',  # cor 6 = Branco
    )


def titulo(msg, cor=0):
        tam = len(msg) +4
        print('~' * tam)
        print(f' {msg}')
        print('~' * tam)

caixa = dict()
def calccaixa(lar=0, comp=0):
      calc = lar * comp
      print(calc)



#principal
laterais = caixa['Laterais'] = int(input('Digite a quantidade de Laterais: '))
dim = caixa['DimLaterais'] = int(input('Digite a Dimensão das Laterais: '))
mat = caixa['Mat'] = str(input('Digite Material '))
calccaixa(laterais, dim)
