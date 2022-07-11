##########################################################################################################################
####################################################### INSTRUÇÕES #######################################################
#
# As variaveis A e B utilizadas nas funções para calcular as INTEGRAIS, tanto de LINHA, como de ÁREA, como também 
# de VOLUME, assim A e B são vetores de 3 posições cada.
# Assim o input desses pontos ou as variações em cada eixo pode ser feito dessa maneira:
#                                             A = [valor, valor, valor];
#                                             B = [valor, valor, valor];
# Caso a variavel do eixo seja constante, como o raio na coordenada esferica, colocar o valor de r no vetor A,
# a primeira possição do vetor A, como 0 e colocar o valor na constante em B.
#
# V é a função que será integrada, ela é um vetor de 3 posições, uma posição para cada dimensão, seja ela cartesiana,
# cilintricas ou esfericas.
# Independente da coordenada os valores para as variaves utilizadas em V, serão x, y e z, ou seja:
#                                           Cilintrica       ρ (rô)  = x
#                                                            ϕ (phi) = z
#                                                                  z = z
#                                         
#                                           Esférica         r       = x
#                                                            θ       = y
#                                                            ϕ (phi) = z
#              
# Além disso, nos coordenadas cilintricas e esfericas, o valor de theta ou phi deve estar em radianos. Ainda, cada função
# deve ser alimentada com sua respectiva coordenada
#
# Por fim, para calcular a INTEGRAL CIRCULAÇÃO, basta utilizar a integral de linha, de sua respectiva coordenada e, 
# para cada caminho utilizado e somar o resuldo de cada caminho integrado, que teremos o valor da integral de circulação
#
##########################################################################################################################
################################################### FIM DAS INSTRUÇÕES ###################################################


import Integral_LCFV
from Integral_LCFV import *
import sympy
from sympy.functions import *
from sympy import *

from time import process_time_ns
import mpmath

import AnaliseVetorial
from AnaliseVetorial import *

from math import e

################################ Integral de Linha ################################
# # Cartesiano
# # Probrlma 3.7 - 3 ed - pg 98
# # Letra a
# # (0, 0, 0) -> (0, 1, 0) -> (2, 1, 0) -> (2, 1, 3) 

# V = [2*x*y, x**2 - z**2, -3*x*z**2];

# # (0, 0, 0) -> (0, 1, 0)
# A0 = [0, 0, 0];
# B0 = [0, 1, 0];
# r0 = IntegLinha_cart(V,A0,B0);

# # (0, 1, 0) -> (2, 1, 0)
# A1 = [0, 1, 0];
# B1 = [2, 1, 0];
# r1 = IntegLinha_cart(V,A1,B1);

# # (0, 1, 0) -> (2, 1, 3)
# A2 = [2, 1, 0];
# B2 = [2, 1, 3];
# r2 = IntegLinha_cart(V,A2,B2);

# print(r0 + r1 + r2);


################################ Integral de Circulação ################################
# Cartesiano
# Basta dividir os caminhos e usar a integral de linha
# Exemplo 3.3 - 5ed - pg 57
# (1, 0, 0) -> (0, 0, 0) -> (0, 1, 0) -> (1, 1, 1) -> (1, 0, 0)

# V = [x**2, -x*z, -y**2];

# # (1, 0, 0) -> (0, 0, 0)
# A0 = [1, 0, 0];
# B0 = [0, 0, 0];
# r0 = IntegLinha_cart(V,A0,B0);

# # (0, 0, 0) -> (0, 1, 0)
# A1 = [0, 0, 0];
# B1 = [0, 1, 0];
# r1 = IntegLinha_cart(V,A1,B1);

# # (0, 1, 0) -> (1, 1, 1)
# A2 = [0, 1, 0];
# B2 = [1, 1, 1];
# r2 = IntegLinha_cart(V,A2,B2);

# # (1, 1, 1) -> (1, 0, 0)
# A3 = [1, 1, 1];
# B3 = [1, 0, 0];
# r3 = IntegLinha_cart(V,A3,B3);

# r = r0 + r1 + r2 + r3;
# # r = [r0, r1, r2, r3];

# print(r);


# # Cilindrico
# # Basta dividir os caminhos e usar a integral de linha
# # Exercicio Prático 3.2 - 5ed - pg 58
# # (0, 0, 0) -> (2, 0, 0) -> (2, 60*pi/180, 0) -> (0, 0, 0)

# V = [x*cos(y), 0, z*sin(y)];

# # (0, 0, 0) -> (2, 0, 0)
# A0 = [0, 0, 0];
# B0 = [2, 0, 0];
# r0 = IntegLinha_cilind(V,A0,B0);

# # (2, 0, 0) -> (2, 60*pi/180, 0)
# A1 = [2, 0, 0];
# B1 = [2, 60*pi/180, 0];
# r1 = IntegLinha_cilind(V,A1,B1);

# # (2, 60*pi/180, 0) -> (0, 0, 0)
# A2 = [2, 60*pi/180, 0];
# B2 = [0, 0, 0];
# r2 = IntegLinha_cilind(V,A2,B2);

# print(r0 + r1 + r2);


############################### Integral de Fluxo/Área #################################
# Problema 3.8 - 5ed - pg 86
# Cartesiana
# V = [10*x*e**(-2), 10*x*e**(0), 1*e**(-2*z)];
# V = [4*x*z, -y**2, y*z];
# A = [0, 0, 0];
# B = [1, 1, 1];

# print(IntegA_cart(V,A,B));

# Exemplo 3.7 - 5ed - pg 67 - R.: pg 60
# Cartesiana
# V = [10*x*e**(-2*x), 0, 10*e**(-2*z)];
# A = [0, 0, 0];
# B = [1, 2*pi, 1];

# print(IntegA_cilind(V,A,B));


################################# Integral de Volume ###################################
# Problema 3.10 - 3ed - pg 99

# Letra a
# Carteisiano
# V0 = [2*x*y, x*z, -y];
# C1 = [0, 0, 0];
# C2 = [2, 2, 2];
# print(IntegVol_cart(V0, C1, C2));

# # Letra b
# # Cilintrico
# a_ro =   2*(x**2)*(cos(y)**2)*sin(y) + x*z*cos(y)*sin(y);
# a_phi = -2*(x**2)*(sin(y)**2)*cos(y) + x*z*(cos(y)**2);
# a_z = -x*sin(y);

# V1 = [a_ro, a_phi, a_z];
# Cil1 = [0, 0, 0];
# Cil2 = [3, 2*pi, 5];
# print(IntegVol_Cilind(V1, Cil1, Cil2));
# Resposta do livro está está errada | a integral de cos^2(phi) foi feita errada

# Letra c
# Esférico
# a_r =     2*(x*sin(y)*cos(z))*(x*sin(y)*sin(z))*sin(y)*cos(z) + (x*sin(y)*cos(z))*(x*cos(y))*cos(y)*cos(z) + (x*sin(y)*sin(z))*sin(y);
# a_theta = 2*(x*sin(y)*cos(z))*(x*sin(y)*sin(z))*sin(y)*sin(z) + (x*sin(y)*cos(z))*(x*cos(y))*cos(y)*sin(z) - (x*sin(y)*sin(z))*cos(z);
# a_phi =   2*(x*sin(y)*cos(z))*(x*sin(y)*sin(z))*cos(y)        - (x*sin(y)*cos(z))*(x*cos(y))*sin(y);

# V2 = [a_r, a_theta, a_phi];
# Esf1 = [0, 0, 0];
# Esf2 = [4, pi, 2*pi];
# print(IntegVol_Esfer(V2, Esf1, Esf2));
# Resposta do livro está está errada | a integral de cos^2(phi) foi feita errada [De novo]
