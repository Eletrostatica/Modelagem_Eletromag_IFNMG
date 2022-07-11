import sympy as spy #módulo par trabalhar com cálculos mais complexos no python
import numpy as np
from sympy import init_printing #Deixa o prnt melhor apresentavel 
from sympy.interactive import printing #Deixa o prnt melhor apresentavel
printing.init_printing(use_latex=True) #Deixa o prnt melhor apresentavel
init_printing() #Deixa o prnt melhor apresentavel
from sympy.vector import CoordSys3D, divergence, gradient, curl # Chama funções gradiente, divergência, rotacional e sistemas de coordenadas

from scipy import integrate
from sympy import *
'''

#........................OBSERVAÇÕES E RECOMENDAÇÕES........................

PARA USAR AS FUNÇÕES DENTRO DESTE CÓDIGO LEIA PREVIAMENTE AS INSTRUÇÕES EM CADA UMA DELAS
ALGUMAS DELAS ESTÃO FINALIZADAS E PODEM SER TRATADAS A PARTIR DO CONSOLE COM MAIOR FACILIDADE DE MANUSEIO
OUTRAS, POR QUESTÃO DE COMPLEXIDADE, DEVEM SER TRATADAS INTERNAMENTE
POR ISSO, NÃO ESTÃO PRESENTES DENTRO DO MENU E ***PRECISAM SER CHAMADAS***
HÁ EXEMPLOS PARA FACILITAR COMPREENSÃO

OBRIGADA


UTILIZE ESSA NOMENCLATURA PARA DECLARAR AS VARIÁVEIS
APENAS POR QUESTÃO DE SINTAXE A COMPONENTE PHI DO SISTEMA DE COORDENADAS ESFÉRICO FOI TRATADA COMO FI

N.i = ax               PARA COORDENADAS ESCALARES
N.j = ay
N.k = az
N.x = x
N.y = y
N.z = z

C.p = arô               PARA COORDENADAS CILINDRICAS
C.phi = aphi
C.z = az
C.P = rô
C.PHI = phi
C.Z = z

S.r=ar               PARA COORDENADAS ESFÉRICAS
S.theta=atheta
S.fi=aphi
S.R=r
S.THETA=theta
S.FI=phi


'''

#VARIÁVEIS DE AUXILIO

mi0=4*spy.pi*10**(-7)

# ......................DEFINIÇÃO DOS SISTEMAS DE COORDENADAS..................


N = CoordSys3D('N') #escalar
#coornadas cilindricas
C = CoordSys3D('C', transformation='cylindrical', vector_names=("p","phi", "z"),variable_names =("P","PHI","Z"))
P = C.P #variáveis esfericas
PHI = C.PHI
Z = C.Z
#coordenadas esfericas
S = CoordSys3D('S', transformation='spherical', vector_names=("r","theta", "fi"),variable_names =("R","THETA","FI"))
R=S.R #variaveis esfericas
THETA=S.THETA
FI=S.FI


#.....................CORRENTES DE CONDUÇÃO E CONVECÇÃO........................

'''
#É PRECISO REVISAR OS VALORES DE AUX E CC
'''
#EXEMPLO 5.1 PAG 188
def corrente():    #MODELO MODIFICÁVEL MODIFICAR O AUX CONFORME NECESSARIO
    
    #MODIFICAR O AUX PARA INDICAR A QUAL SISTEMA PERTENCE J 1-CARTESIANA 2-CILÍNDRICA 3-ESFÉRICA
    aux= 3
    
    if aux==1:
        cc=3        #MODIFICAR CC EM QUAL COORDENADA J VARIA 1-ax 2-ay 3-az
        if cc==1:
            d1=N.y
            d2=N.z
        if cc==2:
            d1=N.x
            d2=N.z
        if cc==3:
            d1=N.x
            d2=N.y
        jacob=1 #MATRIX JACOBIANA PARA COMPOSIÇÃO DA INTEGRAL 
    
    if aux==2:
        cc=2        #MODIFICAR CC EM QUAL COORDENADA J VARIA 1-ap 2-aphi 3-az
        if cc==1:
            d1=C.PHI
            d2=C.Z
            jacob=C.P
        if cc==2:
            d1=C.P
            d2=C.Z
            jacob=1
        if cc==3:
            d1=C.P
            d2=C.PHI
            jacob=C.P

    if aux==3:
        cc=2   #MODIFICAR CC EM QUAL COORDENADA J VARIA 1-ar 2-atheta 3-aphi
        if cc==1:
            d1=S.THETA
            d2=S.FI
            jacob=S.R**2*spy.sin(S.THETA)
        if cc==2:
            d1=S.R
            d2=S.FI 
            jacob=S.R*spy.sin(S.THETA)
        if cc==3:
            d1=S.R
            d2=S.THETA
            jacob=S.R

    '''
    #VETOR    
    '''
    j=-(S.R**2*spy.sin(S.THETA))*S.theta #INSERÇÃO DA VARIAÇÃO J 

    '''    
    #POR FAVOR ATENTE-SE À ORDEM INDICADA DE VARIAÇÃO D1 E D2 ANTES DE INSERIR OS VALORES DE LIMITE****************
    '''  
    ls1=2   #LIMITE SUPERIOR DA PRIMEIRA INTEGRAL
    li1=0   #LIMITE INFERIOR DA PRIMEIRA INTEGRAL
    ls2=2*np.pi   #LIMITE SUPERIOR DA SEGUNDA INTEGRAL
    li2=0     #LIMITE INFERIOR DA SEGUNDA INTEGRAL

    j=j*jacob
    
    '''  
    #CASO HAJA ALGUMA INCÓGNITA NÃO VARIÁVEL DENTRO DO J, SEU VALOR DEVE SER EXPLÍCITO
    '''
    j=j.subs(S.THETA, np.pi/6)  #EXEMPLO: SUBSTITUINDO O THETA POR 30°

    I=spy.integrate(j, (d1, li1,ls1))
    I=spy.integrate(I, (d2, li2,ls2))
    
    return display(I)

#............................LEI DE BIOT-SAVART...............................

#EXEMPLO EXEMPLO 7.3 PAG 250

def biotsavart():
    
    p=3 #raio do circulo
    dl=p*C.phi
    ponto=[0,0,4]  #ponto para medição do campo
    I=10
    
    modr=spy.sqrt(ponto[2]**2+p**2)
    r=-p*C.p+ponto[2]*C.z #modificável
    
    a=dl^r
    
    dh=(I*a)/(4*np.pi*modr**3)
    
    h=spy.integrate(dh, (C.PHI, 0,2*np.pi))
    
    return display(h,"A/m")
    
    
biotsavart()
    


#........................LEI CIRCUITAL DE AMPERE...............................

#DETERMINAÇÃO DA DENSIDADE DE CORRENTE

def ampere():
    
    '''
    #INDICAR O PONTO DAS COORDENADAS EM SEQUÊNCIA E INDICAR O CAMPO
    '''
    p=[0,2,5] #ponto de análise 
    h=(N.y*N.z*(N.x**2+N.y**2))*N.i-(N.y**2*N.x*N.z)*N.j+(4*N.x**2*N.y**2)*N.k  #MODIFICAR O VETOR CAMPO

    j=curl(h)
    
    '''
    #MODIFICAR O AUX PARA CADA SISTEMA DE COORDENADAS 1-CARTESIANA 2-CILÍNDRICA 3-ESFÉRICA
    '''
    aux=1  
    
    if aux==1:   
        j=j.subs({N.x:ponto[0], N.y:ponto[1], N.z:ponto[2]})
    if aux==2:
        j=j.subs({C.P:ponto[0], C.PHI:ponto[1], C.Z:ponto[2]})
    if aux==3:
        j=j.subs({S.R:ponto[0], S.THETA:ponto[1], S.FI:ponto[2]})
        
    return display(j)


#..................CAMPO GERADO POR CORRENTE EM LINHA INFINITA...............................


def hlinha():

    print("Insira o vetor linha:") #recebendo os valores em vetor
    vlinha=np.zeros([3])
    for i in range(3):
        vlinha[i] = int(input('n{}: '.format(i)))
    print("insira o ponto de análise:")
    ponto=np.zeros([3])
    for i in range(3):
        ponto[i] = int(input('n{}: '.format(i)))
    print("insira o valor da corrente que percorre a linha(A):")
    I=float(input())
   
    linha=vlinha[0]*N.i+vlinha[1]*N.j+vlinha[2]*N.k
    
    print(vlinha)
    print(ponto)

    for aux in range(3): #para tratameto do p
        if vlinha[aux]!=0:
            vlinha[aux]=0
        else:
            vlinha[aux]=1

    p=spy.sqrt(ponto[0]**2*vlinha[0]+ponto[1]**2*vlinha[1]+ponto[2]**2*vlinha[2])
    print(p)
    aro=(ponto[0]*vlinha[0]*N.i+ponto[1]*vlinha[1]*N.j+ponto[2]*vlinha[2]*N.k)/p
    aphi=linha^aro
    h=(I/(2*np.pi*p))*aphi

    return display(h,"A/m") #unidade


#..................CAMPO GERADO POR CORRENTE EM PLANO INFINITO...............................
    

def hplano():
    
    print("Em qual coordenada está o plano de análise?:\n0-x\n1-y\n2-z")
    a=int(input())
    print("Qual o valor do plano?")
    vplano=int(input())
    print("insira o ponto de análise:")
    ponto=np.zeros([3])
    for i in range(3):
        ponto[i] = int(input('n{}: '.format(i)))
    print("insira o vetor densidade de corrente que percorre o plano(A/m^2):")
    kk=np.zeros([3])
    for i in range(3):
        kk[i] = int(input('n{}: '.format(i)))    
   
    
    aux=np.zeros([3]) #para tratamento do an
    aux[a]=1

    if ponto[a]<vplano:
        an=-aux[0]*N.i-aux[1]*N.j-aux[2]*N.k
    if ponto[a]>vplano:
        an=aux[0]*N.i+aux[1]*N.j+aux[2]*N.k
    else:
        print("***Esse ponto não recebe influência do campo magnético, por favor, tente novamente.***")
        hplano()
        
    k=kk[0]*N.i+kk[1]*N.j+kk[2]*N.k

    h=(k^an)/2
    
    return display(h,"A/m") #unidade


#........................DENSIDADE E FLUXO MAGNETICO...........................

'''
#É PRECISO REVISAR OS VALORES DE AUX E CC
'''
#EXEMPLO QUESTÃO 7.28 B LIVRO PAG 277
def fluxo():
    #MODIFICAR O AUX PARA INDICAR A QUAL SISTEMA PERTENCE B 1-CARTESIANA 2-CILÍNDRICA 3-ESFÉRICA
    aux= 1
    
    if aux==1:
        cc=1        #MODIFICAR CC EM QUAL COORDENADA B VARIA 1-ax 2-ay 3-az
        if cc==1:
            d1=N.y
            d2=N.z
        if cc==2:
            d1=N.x
            d2=N.z
        if cc==3:
            d1=N.x
            d2=N.y
        jacob=1 #MATRIX JACOBIANA PARA COMPOSIÇÃO DA INTEGRAL 
    
    if aux==2:
        cc=2        #MODIFICAR CC EM QUAL COORDENADA B VARIA 1-ap 2-aphi 3-az
        if cc==1:
            d1=C.PHI
            d2=C.Z
            jacob=C.P
        if cc==2:
            d1=C.P
            d2=C.Z
            jacob=1
        if cc==3:
            d1=C.P
            d2=C.PHI
            jacob=C.P

    if aux==3:
        cc=2   #MODIFICAR CC EM QUAL COORDENADA B VARIA 1-ar 2-atheta 3-aphi
        if cc==1:
            d1=S.THETA
            d2=S.FI
            jacob=S.R**2*spy.sin(S.THETA)
        if cc==2:
            d1=S.R
            d2=S.FI 
            jacob=S.R*spy.sin(S.THETA)
        if cc==3:
            d1=S.R
            d2=S.THETA
            jacob=S.R

    
    '''
    #VETOR 
    '''
    b=(-6*N.x*N.z+4*N.z**2*N.y+2*N.x*N.z**2)*N.i  #INSERÇÃO DA VARIAÇÃO B

    '''    
    #POR FAVOR ATENTE-SE À ORDEM INDICADA DE VARIAÇÃO D1 E D2 ANTES DE INSERIR OS VALORES DE LIMITE****************
    '''  
    ls1=2   #LIMITE SUPERIOR DA PRIMEIRA INTEGRAL
    li1=0   #LIMITE INFERIOR DA PRIMEIRA INTEGRAL
    ls2=2   #LIMITE SUPERIOR DA SEGUNDA INTEGRAL
    li2=0   #LIMITE INFERIOR DA SEGUNDA INTEGRAL

    b=b*jacob
    
    '''  
    #CASO HAJA ALGUMA INCÓGNITA NÃO VARIÁVEL DENTRO DO B, SEU VALOR DEVE SER EXPLÍCITO
    '''
    b=b.subs(N.x, 1)  #EXEMPLO: SUBSTITUINDO O THETA POR 30°

    fluxo=spy.integrate(b, (d1, li1,ls1))
    fluxo=spy.integrate(fluxo, (d2, li2,ls2))
    
    return display(fluxo)



#......................POTENCIAl MAGNÉTICO ESCALAR............................

'''
#INSERIR TODO O VETOR
'''
def potmagesc():
    
    vm=C.P**2*spy.cos(C.Z)-3*C.PHI
    h=-gradient(vm)
    
    return display(h,"A/m")
    

#.......................POTENCIAl MAGNÉTICO VETORIAL............................

#EXEMPPLO QUESTÃO 7.28 a LIVRO PAG 277
'''
#INSERIR TODO O VETOR
'''
def potmagvet():
    
    a=(2*N.x**2*N.y+N.y*N.z)*N.i+(N.x*N.y**2-N.x*N.z**3)*N.j-(6*N.x*N.y*N.z-2*N.x**2*N.y**2)*N.k
    b=curl(a)

    return display(b,"T")
    

    
#...............................MENU DE ÍNICIO.................................


def menu():
    print("Bem-vindo, este é o menu de testes deste programa. Por favor, para cada interação digite apenas números. Obrigada.")
    print("Digite o número referente à operação que deseja realizar:")
    print("1-Corrente em linha infinita\n2-Corrente em um plano infinito")
    print("Para o uso dos outros tópicos vide instruções de uso")
    a=int(input())
    
    if a==1:
        hlinha()
    if a==2:
        hplano()

    return()

#menu()     



