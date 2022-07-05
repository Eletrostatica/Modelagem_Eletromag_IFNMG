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
Eo=float(8.85e-12)

#####################  Calcula a força magnetica devido uma carga  #####################
def forca_magnetica(q,B,v,Teta):
    #B= campomagnetico(); caso tenha que calcular o campo magnetico primeiro
    #B=float(input("Valor do campo magnetico: (em Tesla)"))
    #q=float(input("Digite o valor da carga elétrica: (em Coloumbs)"))
    #Teta = float(input("Digite o angulo entre o Campo de a velocidade (em graus): "))
    #Tetarad= numpy.radians(Teta);
    #op = int(input("Digite a opção referente a seu angulo? 1-Graus     2-Radianos:"))
    #v=float(input("Digite a velocidade (em m/s)"))
    Fm=abs(q)*v*B*math.sin(conv_angulo(Teta))
    Fm=cientific_format(Fm)
    print("A força magnetica que age sobre a carga é de ", Fm)
    #return Fm

############################  Conversor de graus para radianos  ############################
def conv_angulo(T):
    Tetarad=numpy.radians(T)
    return Tetarad

########################  Conversor de numeros para cientifico  ############################
def cientific_format(X):
    limitador= round(X,2)
    formatado=numpy.format_float_scientific(limitador)
    return formatado


#Força Magnetica entre condutores paralelos ou força entre elementos de corrente
#Função ForcaM Calcula a Força Magnetica entre dois condutores
def ForcaM(i1, i2, r, l):
    FM=((MIo*i1*i2*l)/(2*math.pi*r))
    print("Força Magnetica entre dois elementos de corrente é igual a",FM)
    return FM

def distancia_equivalente(d12,d23,d13):
    mult=d12*d13*d23
    Deq=pow(mult,1/3)
    Deq=round(Deq,3)
    print("A distancia equivalente entre as fases e de ", cientific_format(Deq),"metros")
    return Deq

def raio_equivalente(d,r):
    mult=r*pow(d,3)*math.sqrt(2)
    Req=pow(mult,1/4)
    Req=Req/100
    Req=round(Req,4)
    print("O raio equivalente entre as fases e de ", cientific_format(Req) ,"metros")
    return Req

def calculator_capacitancia(Req,Deq):
    const=2*math.pi*Eo
    ln=math.log(Deq/(Req))
    capacitance=const/ln
    print("A capacitancia da linha é de " ,capacitance ,"F")

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
        # Definindo valores das variaveis
        q=0.000004 #Valor da carga (C)
        B=8        #Valor do campo magnetico (T)
        v=5000     #Velocidade (m/s)
        Teta=60    #Angulo (graus)
        forca_magnetica(q,B,v,Teta)   #Chamando a formula

    ########################### Força magnética entre dois condutores #############################
    if resp == 2:
        #Definindo valores das variaveis
        i1=1.5
        i2=4
        r=0.03
        l=0.1

        ForcaM(i1, i2, r, l)
    ########################### Capacitancia ###############
    if resp == 3:
        ####### Letra A #######
        Deq=distancia_equivalente(10,20,10)
        Req=raio_equivalente(20, 2.5)
        print(calculator_capacitancia(Req,Deq))

        ####### Letra B #######


    ########################## Indutores, Indutancia e Indutancia Mútua ################
    if resp == 4:
        print("nada ainda")

    ##########################   Circuitos Magneticos   ##########################
    if resp == 5:
        print("nada ainda")

    ##########################   Campos Variáveis no tempo   ##########################
    if resp == 6:
        print("nada ainda")



Menu_Linhas_de_transmissao()
# 1. Força magnética e força entre elementos de corrente.
# 2. Capacitância
# 3. Indutores, Indutância e Indutância Mútua
# 4. Circuitos Magnéticos
# 5. Campos Variáveis no tempo
