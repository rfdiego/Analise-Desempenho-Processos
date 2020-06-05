from multiprocessing import Process
import time
import random
import timeit

#Funcao que verifica se o numero passado por parametro eh primo
def isprimo(numero):
    if numero >=2:
        for i in range(2, numero):
            if numero % i == 0:
                return False
    else:
        return False
    return True

#funcao que gera numeros primos dentro de um range especifico
def gerar_primos(id,init, fim):

    #numeros primos
    primos = []

    #qutde total de numeros primos encontrados no range
    total =0

    Timeinicio = timeit.default_timer()

    for numero in range(init, fim + 1):
        if isprimo(numero):
           primos.append(numero)
           total += 1

    Timefim = timeit.default_timer()

    print('[Processo %i' %id + '] Numero %i' %init + ' a %i' %fim)
    print(primos)
    print('Total de numeros primos: %i' % total)

    #sl.append(Timefim - Timeinicio)
    #print('Maior tempo ate thread atual: %.1f' % max(sl, key=float))

    if (Timefim - Timeinicio) >=1 and (Timefim - Timeinicio) <60:
        print ('Duracao: %.1f' % (Timefim - Timeinicio) + ' seconds.') #Faz o calculo de quanto tempo demorou para achar os numeros
    else:
        print ('Duracao: %.1f' % (Timefim - Timeinicio)+ ' miliseconds') #Faz o calculo de quanto tempo demorou para achar os numeros
    print('')

    return

if __name__ == '__main__':

    Timeinicio = timeit.default_timer()

    arrProcesso = []
    inicial =0
    final =50000
    qtdethreads=7
    inc= int(final / qtdethreads)
    mrange= inc
    for i in range(qtdethreads):
        t = Process(target=gerar_primos,args=(i+1,inicial,mrange,))
        arrProcesso.append(t)
        t.start()
        inicial += inc
        mrange =inicial+inc

    for x in arrProcesso:
        x.join()

    Timefim = timeit.default_timer()
    print ('Duracao: %.1f' % (Timefim - Timeinicio) ) #Faz o calculo de quanto tempo demorou para achar os numeros


    """"if (Timefim - Timeinicio) >=1 and (Timefim - Timeinicio) <60:
        print ('Duracao: %.1f' % (Timefim - Timeinicio) + ' seconds.') #Faz o calculo de quanto tempo demorou para achar os numeros
    else:
        print ('Duracao: %.1f' % (Timefim - Timeinicio)+ ' miliseconds') #Faz o calculo de quanto tempo demorou para achar os numeros
    print('')"""

"""
OBS: PELO FATO DE QUE AS VARIAVEIS NAO PODEM SER COMPARTILHADAS EM
MULTIPROCESSING, NAO EH POSSIVEL INCREMENTAR A CONTABILIZACAO DE
NUMEROS,E A CONTAGEM DE TEMPO DE DURACAO FINAL DA FUNCAO FICA
POR FORA DA FUNCAO, NAO SERA COMPROMETIDO A FIM DE CALCULO
"""