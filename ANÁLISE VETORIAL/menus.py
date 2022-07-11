import math
import numpy

def Menu_analise_vetorial():
  
    print("########################################################################################")
    print("# Digite a opção desejada:  Grupo 01 – ANÁLISE VETORIAL                                #")
    print("# 1 - Conversão de coordenadas cartesianas esféricas, cilíndricas (pontos e vetores)   #")
    print("# 2 - Cálculo de vetores unitários                                                     #")
    print("# 3 - Produto escalar, produto vetorial                                                #")
    print("# 4 - Deslocamento diferencial, área diferencial, volume diferencial (dl, dS, dV)      #")
    print("# 5 - Integral de linha, integral de circulação, integral de fluxo, integral de volume #")
    print("# 6 - Gradiente, divergente, rotacional, laplaciano.                                   #")
    print("# 7 - Teorema da divergência e teorema de Stokes                                       #") 
    print("# 8 - Sair                                                                             #")
    print("########################################################################################")

    resp = int(input("# Número escolhido: "))

    ############################## Força elétrica ###########################
    if resp == 1:

        ######################################### Exemplo 1 ##########################################
        # Suponha que uma carga elétrica de 4 μC seja lançada em um campo magnético uniforme de 8 T. #
        # Sendo de 60ºC o ângulo formado entre v e B, determine a força magnética que atua sobre a    #
        # carga supondo que a mesma foi lançada com velocidade igual a 5x10³ m/s.                  #
        ##############################################################################################

        # Definindo valores das variaveis
        
        input("Pressione Enter para continuar")

    ########################### Força magnética entre dois condutores #############################
    if resp == 2:

        ######################################### Exemplo 2 ##########################################
        # Suponha que uma carga elétrica de 4 μC seja lançada em um campo magnético uniforme de 8 T. #
        # Sendo de 60ºC o ângulo formado entre v e B, determine a força magnética que atua sobre a   #
        # carga supondo que a mesma foi lançada com velocidade igual a 5x10³ m/s.                    #
        ##############################################################################################


        #Definindo valores das variaveis
        
        input("Pressione Enter para continuar")
    ########################### Capacitancia ###############
    if resp == 3:
        ####### Letra A #######
       
        input("Pressione Enter para continuar")

    ########################## Indutores, Indutancia e Indutancia Mútua ################
    if resp == 4:
        #INDUTANCIA
        
        input("Pressione Enter para continuar")

    ##########################   Circuitos Magneticos   ##########################
    if resp == 5:
        #RELUTANCIA E PERMEABILIDADE MAGNETICA
        
        
       
        input("Pressione Enter para continuar")

    ##########################   Campos Variáveis no tempo   ##########################
    if resp == 6:
        ##########################   Campos Variáveis no tempo   ##########################
      

        input("Pressione Enter para continuar")
    return resp

while Menu_analise_vetorial()!=8:
    Menu_analise_vetorial()
