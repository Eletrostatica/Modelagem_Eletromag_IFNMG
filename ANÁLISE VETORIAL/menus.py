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

    ############################## Conversão de coordenadas cartesianas esféricas, cilíndricas (pontos e vetores) ###########################
    if resp == 1:

       

    
        
        input("Pressione Enter para continuar")

    ###########################  Cálculo de vetores unitários  #############################
    if resp == 2:

       

        
        input("Pressione Enter para continuar")
    ########################### Produto escalar, produto vetorial ###############
    if resp == 3:
       
        input("Pressione Enter para continuar")

    ########################## Deslocamento diferencial, área diferencial, volume diferencial (dl, dS, dV)  ################
    if resp == 4:
      
        
        input("Pressione Enter para continuar")

    ##########################   Integral de linha, integral de circulação, integral de fluxo, integral de volume  ##########################
    if resp == 5:
      
        
       
        input("Pressione Enter para continuar")

    ##########################   Gradiente, divergente, rotacional, laplaciano.   ##########################
    if resp == 6:
              
        input("Pressione Enter para continuar")
    
    if resp == 7:
    ##########################   Teorema da divergência e teorema de Stokes    ##########################
      
        input("Pressione Enter para continuar")
    return resp

while Menu_analise_vetorial()!=8:
    Menu_analise_vetorial()
