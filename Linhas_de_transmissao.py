import math
import numpy


 # 1. Força magnética e força entre elementos de corrente.
 # 2. Capacitância
 # 3. Indutores, Indutância e Indutância Mútua
 # 4. Circuitos Magnéticos
 # 5. Campos Variáveis no tempo

#Constantes
Uo= 4*math.pi*math.pow(10, -7)
Eo=float(8.85e-12) #Epson
Po=float(12.56e-7) #permissividade magnetica no vacuo

#####################Calcula a força magnetica devido uma carga#####################
def forca_magnetica(q,B,v,Teta):
    # B= campomagnetico(); caso tenha que calcular o campo magnetico primeiro
    Fm=abs(q)*v*B*math.sin(conv_angulo(Teta))
    Fm=cientific_format(Fm)
    print("A força magnetica que age sobre a carga é de ", Fm)
    # return Fm

############################    Conversor de graus para radianos    ############################
def conv_angulo(T):
    Tetarad=numpy.radians(T)
    return Tetarad

########################    Conversor de numeros para cientifico    ############################
def cientific_format(X):
    limitador= round(X,3)
    formatado=numpy.format_float_scientific(limitador)
    return formatado


 #Força Magnetica entre condutores paralelos ou força entre elementos de corrente
 #Função ForcaM Calcula a Força Magnetica entre dois condutores
def ForcaM(i1, i2, r, l):
    FM=((Uo*i1*i2*l)/(2*math.pi*r))
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

def const_a(d):
    d1=d/2
    d2=d1*math.pow(math.e,-1/4)
    return d2

   # a= constante                b= distancia entre os fios (metros)
def calculator_indutancia(a,b):
    multipx=Po/math.pi
    logzin=math.log(b/a)
    indutance=multipx*logzin
    print("A indutancia da linha é de " ,indutance ,"H/m")

 #INDUTANCIA MUTUA
def calculator_indutanciamutua(fem, I0, If, variatempo):
    variacorrent = If - I0
    didt = variacorrent / variatempo
    if didt < 0:
        didt = (variacorrent / variatempo) * -1
    indutancemutua = fem / didt
    print("A indutancia mutua é de ", indutancemutua, "H")

def permeabilidade_mag(Uo, Ur):
    U=Ur*Uo
    return U

def relutancia(l, u, a):
    R=l/(u*a)
    return R

def fluxo_mag(B, a):
    fluxo=B*a*math.pow(10,-2)
    return fluxo

def calc_corrente(n, f, r):
    i=f*r/n
    return i

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

    ########################## Indutores, Indutancia e Indutancia Mútua ################
    if resp == 4:
        #INDUTANCIA
        diametro = 0.00254 #Dado em metros
        dist_fios = 3.05 #Dado em metros
        a=const_a(diametro)
        b=dist_fios
        calculator_indutancia(a, b)

        # INDUTANCIA MUTUA
        fem=30*math.pow(10,3) # Força eletromotriz induzida (V)
        I0= 6 # Corrente inicial (A)
        If= 0 # Corrente final (A)
        variatempo = 2.5e-3 #Variação do tempo (s)
        calculator_indutanciamutua(fem, I0, If, variatempo)

    ##########################   Circuitos Magneticos   ##########################
    if resp == 5:
        #RELUTANCIA E PERMEABILIDADE MAGNETICA
        a=0.04 #area (m^2)
        Ur=80000 #Permeabilidade Relativa
        B = 1  # Densidade fluxo magnetico (T)
        n= 200  #Numero de espiras
        u=permeabilidade_mag(Uo,Ur)
        print("A permeabilidade magnética é de ", cientific_format(u))
        l = 30 #Comprimento total
        r=relutancia(l,u,a)
        print("A relutância do circuito é de ", r, "Ae/Wb")

        #FLUXO MAGNETICO
        f=fluxo_mag(B,a)
        print("O valor do fluxo magnetico é de ", f, "Wb")

        #CORRENTE
        i=calc_corrente(n,f,r)
        print("A corrente encontrada é de ",cientific_format(i)," A")

    ##########################   Campos Variáveis no tempo   ##########################
    if resp == 6:
        ##########################   Campos Variáveis no tempo   ##########################
        if resp == 6:
            t = numpy.arange(0, 100, 1)  # tempo
            Ro = 0.15  # variavel P(Ro)
            r = 250  # resistencia
            fi = 2 * math.pi
            vcos = 120
            B = 0.2  # *math.cos(120*math.pi*t)
            flux = 0.2 * ((Ro * Ro) / 2) * fi  # *math.cos(120*math.pi*t)
            fem = 0.2 * ((Ro * Ro) / 2) * fi * 120 * math.pi  # *math.sin(120*math.pi*t)
            I = (0.2 * ((Ro * Ro) / 2) * fi * 120 * math.pi) / r  # *math.sin(120*math.pi*t)
            Vab = -fem

            print(B'')
            print(flux)
            print(fem)
            print(I)
            print(Vab)



Menu_Linhas_de_transmissao()
# 1. Força magnética e força entre elementos de corrente.
# 2. Capacitância
# 3. Indutores, Indutância e Indutância Mútua
# 4. Circuitos Magnéticos
# 5. Campos Variáveis no tempo
