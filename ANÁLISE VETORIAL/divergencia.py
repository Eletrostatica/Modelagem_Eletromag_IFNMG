from __future__ import division  
import numpy as np  
from numpy import linalg  
def F(rr):
  return(vector(rr.x**2*rr.y,2*rr.x*rr.z,rr.z**2 - 2*rr.y))

def delF(rr):
  return(2*rr.x*rr.y+2*rr.z)
  
N = 1000
R = 1
drr=0.001

n = 0
dV = (4/3)*pi*R**3/N
Rs = (3*dV/(4*pi))**(1/3)

Q = 0
while n<N:
  rt = R*vector(2*random()-1,2*random()-1,2*random()-1)
  if mag(rt)<R:
    n = n + 1
    sphere(pos=rt, radius=Rs,opacity=0.5)
    dQ = delF(rt)*dV
    Q = Q + dQ

print("Q = ",Q)
N = 1000
n = 0
dA = 4*pi*R**2/N
Rc = sqrt(dA/pi)
flux = 0
while n< N:
  rt = R*vector(2*random()-1,2*random()-1,2*random()-1)
  if mag(rt)>R-drr and mag(rt)<R+drr:
    cylinder(pos=rt, axis=drr*norm(rt), radius=Rc,color=color.yellow, opacity=0.5)
    dflux = dot(F(rt), norm(rt))*dA
    flux = flux + dflux
    n = n + 1
print("Flux = ",flux)
  