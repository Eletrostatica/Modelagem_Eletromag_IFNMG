import math
import numpy
#from magnetostatica import camposmagneticos

################### Instruções de Uso ##################

# 1. Força magnética e força entre elementos de corrente.
# 2. Capacitância
# 3. Indutores, Indutância e Indutância Mútua
# 4. Circuitos Magnéticos
# 5. Campos Variáveis no tempo

#Constantes
MIo= 4*math.pi*math.pow(10, -7)

def forca_magnetica(q,B,v,Teta):
    #B= campomagnetico(); caso tenha que calcular o campo magnetico primeiro
    #B=float(input("Valor do campo magnetico: (em Tesla)"))
    #q=float(input("Digite o valor da carga elétrica: (em Coloumbs)"))
    #Teta = float(input("Digite o angulo entre o Campo de a velocidade (em graus): "))
    #Tetarad= numpy.radians(Teta);
    #op = int(input("Digite a opção referente a seu angulo? 1-Graus     2-Radianos:"))
    #v=float(input("Digite a velocidade (em m/s)"))
    Fm=abs(q)*v*B*math.sin(conv_angulo(Teta))
    print("A força magnetica que age sobre a carga é de ",Fm)

def conv_angulo(T):
    Tetarad=numpy.radians(T)
    return Tetarad

#Força Magnetica entre condutores paralelos ou força entre elementos de corrente
#Função ForcaM Calcula a Força Magnetica entre dois condutores

def ForcaM(i1, i2, r, l):
    FM=((MIo*i1*i2*l)/(2*math.pi*r))
    print("Força Magnetica entre dois elementos de corrente é igual a",FM)
    return FM


def Menu_Linhas_de_transmissao():
    print("################################################################")
    print("# Digite a opção desejada:                                     #")
    print("# 1 - Força magnética                                          #")
    print("# 2 - Força magnética entre dois condutores                    #")
    print("# 3 - Capacitancia                                             #")
    print("# 4 - Indutores, Indutancia e Indutancia Mútua                 #")
    print("# 5 - Circuitos Magneticos                                     #")
    print("# 6 - Campos Variáveis no tempo                                #")
    print("################################################################")
    resp = int(input("# Número escolhido: "))

    ############################## Força elétrica ###########################
    if resp == 1:
        q=0.000004 #Valor da carga (C)
        B=8        #Valor do campo magnetico (T)
        v=5000     #Velocidade (m/s)
        Teta=60    #Angulo (graus)
        forca_magnetica(q,B,v,Teta)   #Chamando a formula

    ########################### Campo Elétrico #############################
    if resp == 2:
        #Definindo valores das variaveis
        i1=1.5
        i2=4
        r=0.03
        l=0.1

        ForcaM(i1, i2, r, l)

    ########################### Intensidade de Campo elétrico ###############
    if resp == 3:
        print("nada")

    ########################## Sobreposição de Força ou Campo ################
    if resp == 4:
        print("nada")

Menu_Linhas_de_transmissao()
# 1. Força magnética e força entre elementos de corrente.
# 2. Capacitância
# 3. Indutores, Indutância e Indutância Mútua
# 4. Circuitos Magnéticos
# 5. Campos Variáveis no tempo
