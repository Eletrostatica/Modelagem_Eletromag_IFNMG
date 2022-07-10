import sympy as spy
import math
import numpy as np

from sympy import diff, sin, cos, pi
from sympy.abc import r, theta, phi, x, y, z
from sympy.vector import CoordSys3D, Del, curl, divergence, express

N= CoordSys3D('N')  # coordenas cartesianas

C= CoordSys3D('C', transformation='cylindrical', vector_names=("ro","phi", "z"),variable_names =("RO","PHI","Z")) # coordenadas cilíndricas
RO = C.RO; PHI = C.PHI; Z = C.Z

S= CoordSys3D('S', transformation='spherical', vector_names=("r","teta", "phi"),variable_names =("R","TETA","PHI")) # coordenadas esféricas
R= S.R; TETA= S.TETA; PHI= S.PHI






#--------------ORIENTAÇÕES-------------------------
# PARA DETERMINAR UM VETOR EM COORDENADA CARTESIANA, DEVE-SE ESCREVÊ-LO DE ACORDO COM AS SEGUINTES ORIENTAÇÕES:
#
# escreve-se a variável 'x' da seguinte maneira: 'N.x'
# 'y' escreve-se 'N.y'
# 'z' escreve-se 'N.z'
#
# por exemplo, para representar o campo escalar V= x^2 * y^2 * z, escreva:
# V= N.x**2 * N.y**2 * N.z
#
# seguindo a mesma lógica, para representar as direções das componentes de um campo vetorial, em vez de usar 'i, j, k', 
# usaremos 'N.i, N.j, N.k', respectivamente. Por exemplo:
#
# para representar o campo vetorial V= x*y*i + x*z*j + y*z*k, escreva:
# V= N.x*N.y*N.i + N.x*N.z*N.j + N.y*N.z*N.k
#
#
# Isso vale também para as coordenadas cilíndricas e esféricas.
# Nas coordenadas cilíndricas:
#
# C.ro = arô
# C.phi = aphi
# C.z = az
# C.RO = rô
# C.PHI = phi
# C.Z = z
#
# exemplo: F= C.RO**2 *spy.cos(C.PHI) *C.ro + C.Z*C.RO**3 *spy.sin(C.PHI) *C.phi + C.Z**2 *C.z
#
#
# Nas coordenadas cilíndricas:
#
# S.r = ar
# S.teta = ateta
# S.phi = aphi
# S.R = r
# S.TETA = teta
# S.PHI = phi
#
# exemplo: F= S.R* spy.sin(S.TETA)* spy.sin(S.PHI) *S.r + S.R**2 *spy.cos(S.PHI) *spy.sin(S.TETA) *S.phi
#

#---------------- FUNÇÕES ------------------------------------------------------------------

#-----CONVERSÃO DE PONTOS ENTRE COORDENADAS----------
def conversao_de_pontos():
    print("A conversão de pontos será entre quais coordenadas?")
    print("Cartesiana --> Cilíndrica               DIGITE 1")
    print("Cilíndrica --> Cartesiana               DIGITE 2")
    print("Cartesiana --> Esférica                 DIGITE 3")
    c1 = int(input("Esférica --> Cartesiana                 DIGITE 4 \n"))

    if c1==1:
        i= inserir_pv_cart()
        print(ponto_cart_cilind(i[0], i[1], i[2]))
    elif c1==2:
        i= inserir_pv_cilind()
        print(ponto_cilind_cart(i[0], i[1], i[2]))   
    elif c1==3:
        i= inserir_pv_cart()
        print(ponto_cart_esfer(i[0], i[1], i[2]))
    elif c1==4:
        i= inserir_pv_esfer()
        print(ponto_esfer_cart(i[0], i[1], i[2]))

#-----VETOR UNITÁRIO-----
def calcular_vetor_unitario(): #calcula o vetor unitário em coordenadas cartesianas, cilíndricas ou esféricas
    print("O ponto a partir do qual deve-se calcular o vetor unitário está em quais coordenadas? \n")
    print("Coordenadas cartesianas               DIGITE 1")
    print("Coordenadas ciliíndricas              DIGITE 2")
    coord= int(input("Coordenada esférica                   DIGITE 3 \n"))
    if coord==1:
        i= inserir_pv_cart()
        print(vet_uni(i[0], i[1], i[2]))
    elif coord==2:
        i= inserir_pv_cilind()
        j= ponto_cilind_cart(i[0], i[1], i[2])
        k= vet_uni(j[0], j[1], j[2])
        print(ponto_cart_cilind(k[0], k[1], k[2]))
    elif coord==3:
        i= inserir_pv_esfer()
        j= ponto_esfer_cart(i[0], i[1], i[2])
        k= vet_uni(j[0], j[1], j[2])
        print(ponto_cart_esfer(k[0], k[1], k[2]))

#-----PRODUTO ESCALAR ENTRE VETORES------------------
'''Exemplo 1 (coordenada cartesiana): Calcule o produto escalar entre os vetores A= 2*x*y*z*i + x**2*j     e      B= 4*x**3*i - z**2*y**2*j + 1*k
>>>prod_esc(2*N.x*N.y*N.z*N.i + N.x**2*N.j, 4*N.x**3*N.i - N.z**2*N.y**2*N.j + 1*N.k)
8*N.x**4*N.y*N.z - N.x**2*N.y**2*N.z**2

Exemplo 2 (coordenada cilíndrica): Calcule o produto escalar entre os vetores F= 2*x*y*z*arô + x**2*aphi     e      G= 4*x**3*arô - z**2*y**2*aphi + 1*az
>>>prod_esc(2*C.RO*C.PHI*C.Z*C.ro + C.RO**2*C.phi, 4*C.RO**3*C.ro - C.Z**2*C.PHI**2*C.phi + 1*C.z)
-C.PHI**2*C.RO**2*C.Z**2 + 8*C.PHI*C.RO**4*C.Z

'''
def prod_esc(vetor1, vetor2):     
    
    return vetor1 & vetor2


#-----PRODUTO VETORIAL--------------------          
'''Exemplo 1 (coordenada cartesiana): Calcule o produto VETORIAL entre os vetores A= 2*x*y*z*i + x**2*j   e    B= 4*x**3*i - z**2*y**2*j + 1*k
>>>prod_vet(2*N.x*N.y*N.z*N.i + N.x**2*N.j, 4*N.x**3*N.i - N.z**2*N.y**2*N.j + 1*N.k)
N.x**2*N.i + (-2*N.x*N.y*N.z)*N.j + (-4*N.x**5 - 2*N.x*N.y**3*N.z**3)*N.k

Exemplo 2 (coordenada cilíndrica): Calcule o produto VETORIAL entre os vetores F= 2*x*y*z*arô + x**2*aphi   e   G= 4*x**3*arô - z**2*y**2*aphi + 1*az
>>>prod_vet(2*C.RO*C.PHI*C.Z*C.ro + C.RO**2*C.phi, 4*C.RO**3*C.ro - C.Z**2*C.PHI**2*C.phi + 1*C.z)
C.RO**2*C.ro + (-2*C.PHI*C.RO*C.Z)*C.phi + (-2*C.PHI**3*C.RO*C.Z**3 - 4*C.RO**5)*C.z

'''
def prod_vet(vetor1, vetor2):

    return vetor1 ^ vetor2


#-----GRADIENTE--------------
'''Ex: calcule o gradiente do campo escalar:
a) U= 4*x*y*z**2 + 3*y*z
>>>gradiente(4*N.x*N.z**2 + 3*N.y*N.z)
4*N.z**2*N.i + 3*N.z*N.j + (8*N.x*N.z + 3*N.y)*N.k

b) H= ro**2*cos(phi)*cos(teta)
>>>gradiente(S.R**2*spy.cos(S.PHI)*spy.cos(S.TETA))
(2*S.R*cos(S.PHI)*cos(S.TETA))*S.r + (-S.R*sin(S.TETA)*cos(S.PHI))*S.teta + (-S.R*sin(S.PHI)*cos(S.TETA)/sin(S.TETA))*S.phi

'''

def gradiente(escalar):
    delop= Del()
    grad= delop(escalar)
    return grad.doit()


#-----ROTACIONAL------------------
'''
Exemplo: calcule o rotacional do vetor H= (rô*z**2*cos(phi) + z*sin^2(phi))*az
>>>rotacional((C.RO*C.Z**2*spy.cos(C.PHI) + C.Z*spy.sin(C.PHI)*spy.sin(C.PHI) )*C.z )
((-C.RO*C.Z**2*sin(C.PHI) + 2*C.Z*sin(C.PHI)*cos(C.PHI))/C.RO)*C.ro + (-C.Z**2*cos(C.PHI))*C.phi

'''
def rotacional(vetor):
    return curl(vetor)


#-----DIVERGENTE-------
'''
Exemplo: calcule o divergente do campo H= (rô*z**2*cos(phi) + z*sin^2(phi))*az
>>>divergente((C.RO*C.Z**2*spy.cos(C.PHI) + C.Z*spy.sin(C.PHI)*spy.sin(C.PHI) )*C.z )
2*C.RO*C.Z*cos(C.PHI) + sin(C.PHI)**2
'''
def divergente(vetor):
    return divergence(vetor)


#-----LAPLACIANO--------
'''
Exemplo: calcule o laplaciano do seguinte vetor. A= x**2*y**2 - 4*y*z**3
>>>laplaciano(N.x**2*N.y**2 - 4*N.y*N.z**3)
2*N.x**2 + 2*N.y**2 - 24*N.y*N.z

'''
def laplaciano(escalar):
    vetor= gradiente(escalar)
    return divergente(vetor)




#--------------- FUNÇÕES AUXILIARES DO TIPO INPUT ----------------------------------

def inserir_pv_cart(): #função input para ler um ponto ou vetor em coordenadas cartesianas
    a= float((input("Valor de x: ")))
    b= float((input("Valor de y: ")))
    c= float((input("Valor de z: ")))  

    return a, b, c

def inserir_pv_cilind(): #função input para ler um ponto ou vetor em coordenadas cilindricas
    ro= float(input("Valor de ro: "))
    phi= float(input("Valor de phi: (em graus) ")) 
    z= float(input("Valor de z: "))

    return [ro, phi, z]

def inserir_pv_esfer(): #função input para ler um ponto ou vetor em coordenadas esféricas
    r= float(input("Valor de r: "))
    teta= float(input("Valor de teta (em graus): ")) 
    phi= float(input("Valor de phi (em graus): ")) 

    return r, teta, phi



#--------------- FUNÇÕES AUXILIARES ----------------------------------

def ponto_cart_cilind(x, y, z): #converte um ponto em coordenadas cartesianas para coordenadas cilíndricas

    ro= round(math.sqrt(x**2 + y**2), 2)
    if x<0 and y>0:
        phi= round(math.degrees(math.atan((y/x)) ), 2) + 90
    elif x<0 and y<0:
        phi= round(math.degrees(math.atan((y/x)) ), 2) + 180
    elif x>0 and y<0:
        phi = 360 + round(math.degrees(math.atan((y/x)) ), 2)
    elif x==0:
        phi= 90.0
    else:
        phi= round(math.degrees(math.atan((y/x))), 2)
    z= round(z, 2)

    return [ro, phi, z]

def ponto_cart_esfer(x, y, z): #converte um ponto em coordenadas cartesianas para coordenadas esféricas
  
    r= round(math.sqrt(x**2 + y**2 + z**2), 2)
    teta= round(math.degrees(math.atan((math.sqrt(x**2 + y**2)/z))), 2)

    if x<0 and y>0:
        phi= round(math.degrees(math.atan((y/x)) ), 2) + 90
    elif x<0 and y<0:
        phi= round(math.degrees(math.atan((y/x)) ), 2) + 180
    elif x>0 and y<0:
        phi = 360 + round(math.degrees(math.atan((y/x)) ), 2)
    elif x==0:
        phi= 90.0
    else:
        phi= round(math.degrees(math.atan((y/x))), 2)

    return[r, teta, phi]

def ponto_cilind_cart(ro, phi, z): #converte um ponto em coordenadas cartesianas para coordenadas cilíndricas

    x= round(ro*math.cos(math.radians(phi)), 2)
    y= round(ro*math.sin(math.radians(phi)), 2)
    z= round(z, 2)

    return [x, y, z]

def ponto_esfer_cart(r, teta, phi): #converte um ponto em coordenadas esféricas para coordenadas cartesianas
    
    x= round(r*math.sin(math.radians(teta))*math.cos(math.radians(phi)), 2) 
    y= round(r*math.sin(math.radians(teta))*math.sin(math.radians(phi)), 2)
    z= round(r*math.cos(math.radians(teta)), 2)

    return [x, y, z]

def ponto_cilind_esfer(ro, phi, z):
    
    i= ponto_cilind_cart(ro, phi, z)
    ponto_cart_esfer(i[0], i[1], i[2])

def vet_uni(a, b, c):
    modulo_vetor= math.sqrt(a**2 + b**2 + c**2)
    
    ax= round(a/modulo_vetor, 2)
    ay= round(b/modulo_vetor, 2)
    az= round(c/modulo_vetor, 2) 

    return [ax, ay, az]

