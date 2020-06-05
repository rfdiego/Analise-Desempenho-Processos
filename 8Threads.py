import time
import timeit
import threading

#Funcao que verifica se o numero passado por parametro eh primo
def isprimo(numero):
    if numero >=2:
        for i in range(2, numero):
            if numero % i == 0:
                return False
    else:
        return False
    return True

class Threads:

    #array para gerenciar a lista de duracao do tempo da funcao
    global sl
    sl=[]

    global total_geral
    total_geral=0

    #funcao que gera numeros primos dentro de um range especifico
    def gerar_primos(id,init, fim):


        #array de numeros primos
        primos = []

        #qutde total de numeros primos encontrados dentro do range
        #global total
        total_range =0

        Timeinicio = timeit.default_timer()

        #percorre um range verificando se o numero eh primo, se for add no array
        for numero in range(init, fim + 1):
            if isprimo(numero):
               primos.append(numero)
               total_range += 1

        Timefim = timeit.default_timer()

        print('[Thread %i' %id + '] Numero %i' %init + ' a %i' %fim)
        print(primos)
        print('Total de numeros primos: %i' % total_range)

        #Contabilizar total geral de numeros primos
        global total_geral
        total_geral += total_range

        #adiciona em um array a duracao do tempo da funcao
        sl.append(Timefim - Timeinicio)

        #mostra o tempo de duracao de cada funcao
        if (Timefim - Timeinicio) >=1 and (Timefim - Timeinicio) <60:
            print ('Duracao: %.1f' % (Timefim - Timeinicio) + ' seconds.') #Faz o calculo de quanto tempo demorou para achar os numeros
        else:
            print ('Duracao: %.1f' % (Timefim - Timeinicio)+ ' miliseconds') #Faz o calculo de quanto tempo demorou para achar os numeros
        print('')

        return

    #Distribui as funcoes em array de threads dentro de cada range incremental
    threads = []
    inicial =0
    final =50000
    qtdethreads=7
    inc= int(final / qtdethreads)
    mrange= inc

    for i in range(qtdethreads):
        t = threading.Thread(target=gerar_primos,args=(i+1,inicial,mrange,))
        threads.append(t)
        t.start()
        inicial += inc
        mrange =inicial+inc

    #aguarda todos os threads finalizarem para proceder as linhas subsequentes
    for x in threads:
        x.join()

    #mostra o tempo de duracao total da tread
    print('Maior tempo ate thread atual: %.1f' % max(sl, key=float))

    #mostra a qtde do total geral de numeros primos encontrados
    print('Total Geral numeros primos encontrados: %.i' % total_geral)