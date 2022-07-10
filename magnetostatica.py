import sympy as spy #módulo par trabalhar com cálculos mais complexos no python
import numpy as np
from sympy import init_printing #Deixa o prnt melhor apresentavel 
from sympy.interactive import printing #Deixa o prnt melhor apresentavel
printing.init_printing(use_latex=True) #Deixa o prnt melhor apresentavel
init_printing() #Deixa o prnt melhor apresentavel
from sympy.vector import CoordSys3D, divergence, gradient, curl # Chama funções gradiente, divergência, rotacional e sistemas de coordenadas

#...................................OBSERVAÇÕES........................

# APENAS POR QUESTÃO DE SINTAXE A COMPONENTE PHI DO SISTEMA DE COORDENADAS ESFÉRICO FOI TRATADA COMO FI

#N.i = ax               PARA COORDENADAS ESCALARES
#N.j = ay
#N.k = az
#N.x = x
#N.y = y
#N.z = z

#C.p = arô               PARA COORDENADAS CILINDRICAS
#C.phi = aphi
#C.z = az
#C.P = rô
#C.PHI = phi
#C.Z = z

#S.r=ar               PARA COORDENADAS ESFÉRICAS
#S.theta=atheta
#S.fi=aphi
#S.R=r
#S.THETA=theta
#S.FI=phi

#OS DOIS TÓPICOS"DENSIDADE E FLUXO MAGNETICO E POTENCIAIS MAGNÉTICOS" FORAM ORGANIZADOS NUMA MESMA FUNÇÃO-
#POIS AS QUESTÕES SÃO DEPENDENTES

#ATÉ O MOMENTO OS TÓPICOS DE CAMPO EM LINHA INFINITA E PLANO INFINITO RECEBEM APENAS VALORES INTEIROS


#VARIÁVEIS DE AUXILIO

mi0=4*spy.pi*10**(-7)



#...............................MENU DE ÍNICIO.................................


def menu():
    print("Bem-vindo, este é o menu de testes deste programa. Por favor, para cada interação digite apenas números. Obrigada.")
    print("Digite o número referente à operação que deseja realizar:")
    print("1-Correntes de condução e convecção\n2-Lei de Biot-Savart\n3-Lei Circuital de Ampère")
    print("4-Campo gerado por corrente\n5-Corrente em linha infinita\n6-Corrente em um plano infinito\n7-Densidade e Fluxo magnético e Potenciais magnéticos")
    a=int(input())
'''    
    if a=1:
        corrente()
    if a=2:
        biotsavart()
    if a=3:
        ampere()
    if a=4:
        campo()
    if a=5:
        hlinha()
    if a=6:
        hplano()
    if a=7:
        fluxo()
        

def back():

print("Deseja realizar outra operação?\nDigite o número referente:\n1-SIM\n2-NÂO)
a=int(input())
if a=1
menu()
if a=2:
exit()
'''
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
#NECESSITA AREA DIFERENCIAL

#INSERIR VETOR DENSIDADE 

j=(3*spy.Pow(S.R,2)*spy.cos(0,523598))*S.r-(spy.Pow(S.R,2)*spy.sin(S.THETA))*S.theta
display(j)

ds1=(S.R*spy.sin(S.THETA))*S.theta #dr dphi


#mudar o diferencial conforme j
corrente=spy.integrate(j,(S.FI,0,2*spy.pi),(S.R,0,2))
display(corrente)


back()
'''
#............................LEI DE BIOT-SAVART...............................



#........................LEI CIRCUITAL DE AMPERE...............................

#DETERMINAÇÃO DA DENSIDADE DE CORRENTE

    
h=(N.y*N.z*(N.x**2+N.y**2))*N.i-(N.y**2*N.x*N.z)*N.j+(4*N.x**2*N.y**2)*N.k
j=curl(h)
j=append



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

    return display(h,"A/m")


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
    
    return display(h,"A/m")


#...............DENSIDADE E FLUXO MAGNETICO E POTENCIAIS MAGNÉTICOS............................

#EXEMPLO 7.7 LIVRO PAG 264
'''
#NECESSITA DE ÁREA DIFERENCIAL

a=(-C.P**2/4)*C.z
b=curl(a)
display(b)

fluxo=


'''

#..........................................................
'''

h=-divergence(v)
h=b/mi0


back()

'''





