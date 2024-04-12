from datetime import datetime

def validarmes(x,y=''):
        if x[0] == 'J':
            print('PRIMEIRO MES DO ANO')
        elif x[-1] == 'J':
            print('Estamos no mes de festa junina ze ruela ')


mes = 'JFM'
mes2 = 'AMJ'
atual = datetime.now()
mes_atual = atual.month
print(mes_atual)
validarmes(mes2)

