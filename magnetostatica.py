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


#VARIÁVEIS DE AUXILIO

mi0=4*spy.pi*10**(-7)



#...............................MENU DE ÍNICIO.................................


def menu():
    print("Bem-vindo, este é o menu de testes deste programa. Por favor, para cada interação digite apenas números. Obrigada.")
    print("Digite o número referente à operação que deseja realizar:")
    print("1-Correntes de condução e convecção\n2-Lei de Biot-Savart\n3-Lei Circuital de Ampère")
    print("4-Campo gerado por corrente\n5-Corrente em linha infinita\n6-Corrente em lâmina infinita\n7-Densidade e fluxo magnético e Potenciais magnéticos")
    

menu()

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
NECESSITA AREA DIFERENCIAL

#INSERIR VETOR DENSIDADE 
j=(3*spy.Pow(S.R,2)*spy.cos(0,523598))*S.r-(spy.Pow(S.R,2)*spy.sin(S.THETA))*S.theta
display(j)

ds1=(S.R*spy.sin(S.THETA))*S.theta #dr dphi
ds2=(S.R**2*spy.sin(S.THETA))*S.r #dphi dtheta
ds3=(S.R)*S.fi #dtheta dr

#mudar o diferencial conforme j
corrente=spy.integrate(j,(S.FI,0,2*spy.pi),(S.R,0,2))
display(corrente)
'''


#..................CAMPO GERADO POR CORRENTE EM LINHA INFINITA...............................

'''
#NECESSITA PRODUTO VETORIAL

ponto=-3*N.x+4*N.y+5*N.z
linha=1*N.j
aro=-3*N.i+5*N.k
p=spy.sqrt((-3)**2)+5**2)
i=10
vetuni=aro/p
aphi=np.cross(linha,vetuni)
h=(i/(2*spy.pi*p))*aphi
display(h)

'''

#..................CAMPO GERADO POR CORRENTE EM PLANO INFINITO...............................
    
'''
#EXEMPLO QUESTAO 1 ROTEIRO PARA PROVA
k=-10*N.i
ponto=N.x+N.y+N.z
refplano=0 #referencia do plano
an=
h=(k*an)/2

'''


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
'''





