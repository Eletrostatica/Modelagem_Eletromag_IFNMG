import sympy as spy
import math
import numpy as np

from sympy import diff, sin, cos

from sympy import *
x, y, z = symbols('x y z')

import DAV_Diferencial
from DAV_Diferencial import *


########################################## Integral de linha ##########################################
def IntegLinha_cart(V, A, B):
    # V -> Função vetorial
    # A -> Inicio da linha
    # B -> Final da linha

    a_x = spy.integrate(V[0], (x, A[0], B[0]));
    a_y = spy.integrate(V[1], (y, A[1], B[1]));
    a_z = spy.integrate(V[2], (z, A[2], B[2]));

    r0 = a_x.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_y.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_z.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r = [r0, r1, r2];
    a = [a_x, a_y, a_z];
    print(a);

    return r0+r1+r2

# Cilindrico
def IntegLinha_cilind(V, A, B):
    # V -> Função vetorial
    # A -> Inicio da linha
    # B -> Final da linha

    a_ro = spy.integrate(V[0], (x, A[0], B[0]));
    a_phi = spy.integrate(V[1]*x, (y, A[1], B[1]));
    a_z = spy.integrate(V[2], (z, A[2], B[2]));

    r0 = a_ro.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_phi.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_z.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })
    # print(r0+r1+r2);

    return r0+r1+r2

# Esferica
def IntegLinha_esfer(V, A, B):
    # V -> Função vetorial
    # A -> Inicio da linha
    # B -> Final da linha

    a_r = spy.integrate(V[0], (x, A[0], B[0]));
    a_theta = spy.integrate(V[1]*x, (y, A[1], B[1]));
    a_phi = spy.integrate(V[2]*x*sin(y), (z, A[2], B[2]));

    r0 = a_r.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_theta.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_phi.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })
    # print(r0+r1+r2);

    return r0+r1+r2

#Integral de Area Cilindrica
def IntegA_cart(V, A, B):
    a_x = spy.integrate(V[0], (y, A[1], B[1]), (z, A[2], B[2]));
    a_y = spy.integrate(V[1], (x, A[0], B[0]), (z, A[2], B[2]));
    a_z = spy.integrate(V[2], (x, A[0], B[0]), (y, A[1], B[1]));

    r0 = a_x.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_y.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_z.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    # print(r0);
    # print(r1);
    # print(r2);

    # return [r0, r1, r2]
    return r0 + r1 + r2

#Integral de Area Cilindrica
def IntegA_cilind(V, A, B):
    a_ro =  spy.integrate(V[0]*B[0], (y, A[1], B[1]), (z, A[2], B[2]));
    a_phi = spy.integrate(V[1], (x, A[0], B[0]), (z, A[2], B[2]))*(-1);      # (-1) normal
    a_z =   spy.integrate(V[2]*B[0], (x, A[0], B[0]), (y, A[1], B[1]))*(-1);

    r0 = a_ro.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_phi.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_z.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    return [r0, r1, r2]
    # return r0 + r1 + r2


#Integral de Area Esférica
def IntegA_esfer(V, A, B):
    a_ro =  spy.integrate(V[0]*(x**2)*sin(y), (y, A[1], B[1]), (z, A[2], B[2]));
    a_phi = spy.integrate(V[1]*x*sin(y), (x, A[0], B[0]), (z, A[2], B[2]))*(-1);      # (-1) normal
    a_z =   spy.integrate(V[2]*x, (x, A[0], B[0]), (y, A[1], B[1]));

    r0 = a_ro.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_phi.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_z.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    return [r0, r1, r2]
    # return r0 + r1 + r2


# Integral de Volume Cartesiano
def IntegVol_cart(V, A, B):
    a_x = spy.integrate(V[0], (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));
    a_y = spy.integrate(V[1], (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));
    a_z = spy.integrate(V[2], (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));

    r0 = a_x.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_y.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_z.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    return [r0, r1, r2]
    #return [a_x, a_y, a_y]


# Integral de Volume Cilindrico
# Considere
#           ro = x
#           phi = y
def IntegVol_Cilind(V, A, B):
    a_ro = spy.integrate(V[0]*x, (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));
    a_phi = spy.integrate(V[1]*x, (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));
    a_z = spy.integrate(V[2]*x, (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));

    # print(a_ro);
    # print(a_phi);
    # print(a_z);

    r0 = a_ro.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_phi.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_z.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    return [r0, r1, r2]


# Integral de Volume Esferico
# Considere
#           ro = x
#           phi = y
def IntegVol_Esfer(V, A, B):
    a_r = spy.integrate(V[0]*x*x*sin(y), (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));
    a_theta = spy.integrate(V[1]*x*x*sin(y), (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));
    a_phi = spy.integrate(V[2]*x*x*sin(y), (x, A[0], B[0]), (y, A[1], B[1]), (z, A[2], B[2]));

    r0 = a_r.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r1 = a_theta.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    r2 = a_phi.subs({
        x : B[0],
        y : B[1],
        z : B[2]
    })

    return [r0, r1, r2]






# # Integral de Linha Cartesiana
# def IntegLin_cart(V, A, B):
#     dl = dl_cart(A, B);
    
#     a_x = spy.integrate(V[0]*dl[0], (x, A[0], B[0]));
#     a_y = spy.integrate(V[1]*dl[1], (y, A[1], B[1]));
#     a_z = spy.integrate(V[2]*dl[2], (z, A[2], B[2]));

#     #return [a_x, a_y, a_z]
#     return a_x + a_y + a_z

# def IntegLin_Cilind(V, A, B, ro):
#     # Função vetorial V
#     # Pontos A e B

#     # Use x como ro
#     #     y como phi
#     #     z como z
#     # Ao definir V

#     dl = dl_cilind(A, B, ro);
    
#     a_ro = spy.integrate(V[0]*dl[0], (x, A[0], B[0]));
#     a_phi = spy.integrate(V[1]*dl[1], (y, A[1], B[1]));
#     a_z = spy.integrate(V[2]*dl[2], (z, A[2], B[2]));

#     return [a_ro, a_phi, a_z]

# def IntegLin_esfer(V, A, B, r, theta):
#     # Função vetorial V
#     # Pontos A e B

#     # Use x como r
#     #     y como theta
#     #     z como phi
#     # Ao definir V

#     dl = dl_esfer(A, B, r, theta);
    
#     a_r = spy.integrate(V[0]*dl[0], (x, A[0], B[0]));
#     a_theta = spy.integrate(V[1]*dl[1], (y, A[1], B[1]));
#     a_phi = spy.integrate(V[2]*dl[2], (z, A[2], B[2]));

#     return [a_r, a_theta, a_phi]

# # Integral de Circulação

# ################################### Integral de Fluxo/Superficie ###################################
# def IntegSuperf_cilind(V, A, B, ro):
#     # Função vetorial V
#     # Pontos A e B

#     dl = dl_cart(A, B, ro);
    
#     a_x = spy.integrate(V[0]*dl[0], (x, A[0], B[0]));
#     a_y = spy.integrate(V[1]*dl[1], (y, A[1], B[1]));
#     a_z = spy.integrate(V[2]*dl[2], (z, A[2], B[2]));

#     return [a_x, a_y, a_z]