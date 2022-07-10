import sympy as spy
import math
import numpy as np

from sympy import diff, sin, cos

from sympy import *
x, y, z = symbols('x y z')

#https://edisciplinas.usp.br/pluginfile.php/345436/mod_resource/content/3/Tabela%20com%20operadores%20diferenciais%20em%20diversas%20coordenadas.pdf

# ================================== COORDENADAS CARTESIANAS ==================================
# A e B são vetores de 3 posições
#
# DESLOCAMENTO DIFERENCIAL
def dl_cart(A, B):

    a_x = spy.integrate(1, (x, A[0], B[0]));
    a_y = spy.integrate(1, (y, A[1], B[1]));
    a_z = spy.integrate(1, (z, A[2], B[2]));

    return [a_x, a_y, a_z]

# AREA DIFERENCIAL
def dS_cart(A, B):

    dx = spy.integrate(1, (x, A[0], B[0]));
    dy = spy.integrate(1, (y, A[1], B[1]));
    dz = spy.integrate(1, (z, A[2], B[2]));

    a_x = dy*dz;
    a_y = dx*dz;
    a_z = dx*dy;

    return [a_x, a_y, a_z]

# VOLUME DIFERENCIAL
def dV_cart(A, B):

    dx = spy.integrate(1, (x, A[0], B[0]));
    dy = spy.integrate(1, (y, A[1], B[1]));
    dz = spy.integrate(1, (z, A[2], B[2]));

    return dx*dy*dz


# ========================== COORDENADAS CILINDRICAS ==========================
# DESLOCAMENTO DIFERENCIAL
def dl_cilind(A, B):
    dro = spy.integrate(1, (x, A[0], B[0]));
    dphi = A[0]*spy.integrate(1, (x, A[1], B[1]));
    dz = spy.integrate(1, (x, A[2], B[2]));   
    
    return dro + dphi + dz

# AREA DIFERENCIAL
def dS_cilind(A, B):
    if (A[1] != B[1]) and (A[2] != B[2]):
        dS = A[0]*spy.integrate(1, (x, A[1], B[1]), (y, A[2], B[2]));
    if (A[0] != B[0]) and (A[2] != B[2]):
        dS = spy.integrate(1, (x, A[0], B[0]), (y, A[2], B[2]));
    if (A[0] != B[0]) and (A[1] != B[1]):
        dS = spy.integrate(x, (x, A[0], B[0]), (y, A[1], B[1]));

    return dS

# VOLUME DIFERENCIAL
def dV_cilind(A, B):
    dro = spy.integrate(x, (x, A[0], B[0]));
    dphi = spy.integrate(1, (y, A[1], B[1]));
    dz = spy.integrate(1, (z, A[2], B[2]));

    return dro*dphi*dz

# ========================== COORDENADAS ESFÉRICAS ==========================
# DESLOCAMENTO DIFERENCIAL
def dl_esfer(A, B):    
    dr = spy.integrate(1, (x, A[0], B[0]));
    dtheta = A[0]*spy.integrate(1, (y, A[1], B[1]));
    dphi = A[0]*sin(A[1])*spy.integrate(1, (z, A[2], B[2]));

    return dr + dtheta + dphi

# AREA DIFERENCIAL
def dS_esfer(A, B):

    if (A[1] != B[1]) and (A[2] != B[2]):
        dS = (A[0]**2)*spy.integrate(sin(x), (x, A[1], B[1]), (y, A[2], B[2]));
    if (A[0] != B[0]) and (A[2] != B[2]):
        dS = sin(abs(A[1]-B[1]))*spy.integrate(x, (x, A[0], B[0]), (y, A[2], B[2]));
    if (A[0] != B[0]) and (A[1] != B[1]):
        dS = spy.integrate(x, (x, A[0], B[0]), (y, A[1], B[1]));

    return dS

# VOLUME DIFERENCIAL
def dV_esfer(A, B):
    dr = spy.integrate(x**2, (x, A[0], B[0]));
    dtheta = spy.integrate(sin(y), (y, A[1], B[1]));
    dphi = spy.integrate(1, (z, A[2], B[2]));

    return dr*dtheta*dphi