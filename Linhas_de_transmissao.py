import math
import numpy
import magnetostatica from hlinha
############### NOMES ###############
# - MARCOS VINICIUS VIEIRA BARNABE
# -
# -
# -
# -
#####################################

    ###################   Instruções de Uso    ##################

 # 1. Força magnética e força entre elementos de corrente.
 # 2. Capacitância
 # 3. Indutores, Indutância e Indutância Mútua
 # 4. Circuitos Magnéticos
 # 5. Campos Variáveis no tempo

#Constantes
Uo= 4*math.pi*math.pow(10, -7) # Permeabilidade do vacúo
Eo=float(8.85e-12) # Constante de permissividade do vácuo
Po=float(12.56e-7) # Permeabilidade magnética do vácuo

#####################    Calcula a força magnetica devido uma carga    #####################
def forca_magnetica(q,B,v,Teta):

    Fm=abs(q)*v*B*math.sin(conv_angulo(Teta))
    Fm=cientific_format(Fm)
    return Fm

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

#Calcula a distancia equivalente para tres fases, de acordo com as distancias de: (1 a 2; 2 a 3; 1 a 3)
def distancia_equivalente(d12,d23,d13):
    mult=d12*d13*d23
    Deq=pow(mult,1/3)
    Deq=round(Deq,3)
    print("A distancia equivalente entre as fases e de ", cientific_format(Deq)," metros")
    return Deq

#####################    Calcula o raio equivalente     #####################
def raio_equivalente(d,r):
    mult=r*pow(d,3)*math.sqrt(2)
    Req=pow(mult,1/4)
    Req=Req/100
    Req=round(Req,4)
    print("O raio equivalente entre as fases e de ", cientific_format(Req) ,"metros")
    return Req

#####################    Calcula a capacitancia    #####################
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

#####################    Calcula a indutancia    #####################
def calculator_indutancia(a,b):
    multipx=Po/math.pi
    logzin=math.log(b/a)
    indutance=multipx*logzin
    print("A indutancia da linha é de " ,indutance ,"H/m")


#####################    Calcula a indutancia mutua    #####################
def calculator_indutanciamutua(fem, I0, If, variatempo):
    variacorrent = If - I0
    didt = variacorrent / variatempo
    if didt < 0:
        didt = (variacorrent / variatempo) * -1
    indutancemutua = fem / didt
    print("A indutancia mutua é de ", indutancemutua, "H")

#####################    Calcula a permeabilidade magnetica    #####################
def permeabilidade_mag(Uo, Ur):
    U=Ur*Uo
    return U

#####################    Calcula a relutancia    #####################
def relutancia(l, u, a):
    R=l/(u*a)
    return R

#####################    Calcula o fluxo magnetico    #####################
def fluxo_mag(B, a):
    fluxo=B*a*math.pow(10,-2)
    return fluxo

#####################    Calcula a corrente    #####################
def calc_corrente(n, f, r):
    i=f*r/n
    return i

def f(x):
    return (math.pow(x,2)/3)

def trapezoidal(x0, xn):
    # calculando o tamanho do passo
    n=1000
    h = (xn - x0) / n
    # Encontrando a soma
    integracao = f(x0) + f(xn)
    for i in range(1, n):
        k = x0 + i * h
        integracao = integracao + 2 * f(k)
    # Encontrando o resultado final
    integracao = integracao * h / 2
    return integracao

def integral():
    limit_inf = float(input("Coloque o limite inferior: "))
    limit_sup = float(input("Coloque o limite superior: "))
    # Call trapezoidal() method and get result
    result = trapezoidal(limit_inf, limit_sup)
    print(round(result,3))
    return result

def Menu_Linhas_de_transmissao():
    print("#########################     MENU     #########################")
    print("#                                                              #")
    print("# Digite a opção desejada:                                     #")
    print("# 1 - Força magnética                                          #")
    print("# 2 - Força magnética entre dois condutores                    #")
    print("# 3 - Capacitancia                                             #")
    print("# 4 - Indutores, Indutancia e Indutancia Mútua                 #")
    print("# 5 - Circuitos Magneticos                                     #")
    print("# 6 - Campos Variáveis no tempo                                #")
    print("# 7 - Sair                                                     #")
    print("################################################################")
    resp = int(input("# Número escolhido: "))

    ############################## Força elétrica ###########################
    if resp == 1:

        ######################################### Exemplo 1 ##########################################
        # Suponha que uma carga elétrica de 4 μC seja lançada em um campo magnético uniforme de 8 T. #
        # Sendo de 60ºC o ângulo formado entre v e B, determine a força magnética que atua sobre a   #
        # carga supondo que a mesma foi lançada com velocidade igual a 5x10³ m/s.                    #
        ##############################################################################################

        q=4e-6     #Valor da carga (C)
        B=8        #Valor do campo magnetico (T)
        v=5000     #Velocidade (m/s)
        Teta=60    #Angulo (graus)
        Fm=forca_magnetica(q,B,v,Teta)   #Chamando a formula
        print("A força magnetica que age sobre a carga é de ", Fm)
        input("Pressione Enter para continuar")

    ########################### Força magnética entre dois condutores #############################
    if resp == 2:


        #Definindo valores das variaveis
        i1= 1.5
        i2= 4
        r= 0.03
        l= 0.1
        ForcaM(i1, i2, r, l)
        input("Pressione Enter para continuar")

    ########################### Capacitancia ###############
    if resp == 3:

        ######################################### Exemplo 3 ##########################################
        # Uma linha de tensão nominal 750kV tem 4 condutores por fase, como mostra a Imagem 1("LdT") #
        # Considere que há transposição. O raio de cada condutor é igual a 2,5cm. A partir disso     #
        # determine a capacitancia da linha                                                          #
        ##############################################################################################

        Deq=distancia_equivalente(10,20,10)
        Req=raio_equivalente(20, 2.5)
        print(calculator_capacitancia(Req,Deq))
        input("Pressione Enter para continuar")

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
        input("Pressione Enter para continuar")

    ##########################   Circuitos Magneticos   ##########################
    if resp == 5:

        ######################################### Exemplo 5 ##########################################
        # Uma bobina está enrolada em núcleo com 4cm² de seção reta, material com                    #
        # permeabilidade relativa de 80000, densidade de fluxo magnético B=1T, como mostra a Imagem  #
        # 1 ("LdT") Calcule a relutância, fluxo e a corrente                                         #
        ##############################################################################################

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
        i=calc_corrente(n, f, r)
        print("A corrente encontrada é de ", cientific_format(i)," A")
        input("Pressione Enter para continuar")

    ##########################   Campos Variáveis no tempo   ##########################
    if resp == 6:
        #t = numpy.arange(0, 100, 1)  # tempo
        Ro = 0.15  # variavel P(Ro)
        r = 250  # resistencia
        fi = 2 * math.pi
        #vcos = 120
        B = 0.2  # *math.cos(120*math.pi*t)
        flux = 0.2 * ((Ro * Ro) / 2) * fi  # *math.cos(120*math.pi*t)
        fem = 0.2 * ((Ro * Ro) / 2) * fi * 120 * math.pi  # *math.sin(120*math.pi*t)
        I = (0.2 * ((Ro * Ro) / 2) * fi * 120 * math.pi) / r  # *math.sin(120*math.pi*t)
        Vab = -fem

        print(round(B,3),"* cos(120πt)")
        print(round(flux,3),"* cos(120πt)")
        print(round(fem,3),"* sin(120πt)")
        print(round(I,3),"* sin(120πt)")
        print("DDP = " , Vab)
        input("Pressione Enter para continuar")

    return resp

while Menu_Linhas_de_transmissao()!=7:
    Menu_Linhas_de_transmissao()
