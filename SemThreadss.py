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

class Sem_Threads:

    #array para gerenciar a lista de duracao do tempo da funcao
    global sl
    sl=[]

    #funcao que gera numeros primos dentro de um range especifico
    def gerar_primos(id,init, fim):

        #numeros primos
        primos = []

        #qutde total de numeros primos encontrados
        global total_geral
        total_geral =0

        Timeinicio = timeit.default_timer()
        for numero in range(init, fim + 1):
            if isprimo(numero):
               primos.append(numero)
               total_geral += 1
        Timefim = timeit.default_timer()

        print('[Thread %i' %id + '] Numero %i' %init + ' a %i' %fim)
        print(primos)
        print('Total de numeros primos: %i' % total_geral)

        #adiciona em um array a duracao do tempo da funcao
        sl.append(Timefim - Timeinicio)

        if (Timefim - Timeinicio) >=1 and (Timefim - Timeinicio) <60:
            print ('Duracao: %.1f' % (Timefim - Timeinicio) + ' seconds.') #Faz o calculo de quanto tempo demorou para achar os numeros
        else:
            print ('Duracao: %.1f' % (Timefim - Timeinicio)+ ' miliseconds') #Faz o calculo de quanto tempo demorou para achar os numeros
        print('')

        return primos

    #chamada da funcao
    gerar_primos(1,0,50000)

    #mostra o tempo de duracao total da tread
    print('Maior tempo ate thread atual: %.1f' % max(sl, key=float))

    #mostra a qtde do total geral de numeros primos encontrados
    print('Total Geral numeros primos encontrados: %.i' % total_geral)