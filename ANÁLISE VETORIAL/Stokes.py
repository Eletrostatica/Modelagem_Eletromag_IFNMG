import math
N = 1000
R = 1
dr = 0.001
dA = 2*pi*R**2/N

def F(rr):
  return(vector(3*rr.y*rr.x,4*rr.z*rr.x,-6*rr.x))

def curlF(rr):
  return(vector(-4*rr.x,6,4*rr.z-3*rr.x))
phi = 0
n = 0

while n < N:
  rt = R*vector(2*random()-1,2*random()-1,2*random()-1)
  if mag(rt)>R-dr and mag(rt)<R+dr and rt.y>0:
    cylinder(pos=rt, axis=dr*norm(rt), radius=sqrt(dA/pi), opacity=0.5)
    dphi = dot(curlF(rt),norm(rt))*dA
    phi = phi + dphi
    n = n + 1

print("Flux = ",phi)

ball=sphere(pos=vector(R,0,0), radius=0.04, color=color.yellow, make_trail=True)
theta = 0
Np = 100
dtheta = pi/(2*Np)

W = 0
drarrow=arrow(pos=ball.pos,axis=.9*vector(0,-1,0))
while theta>-2*pi:
  rate(5000)
  dr = -vector(-sin(theta),0,cos(theta))*pi*R/(2*Np)
  drarrow.pos=ball.pos
  drarrow.axis=10*dr
  dW = dot(F(ball.pos),dr)
  W = W + dW
  ball.pos = R*vector(cos(theta),0,sin(theta))
  theta = theta - dtheta

print("W = ",W)
n = 0
phi2 = 0
drr = 0.001
dA = pi*R**2/N
while n<N:
  rt = R*vector(2*random()-1,0,2*random()-1)
  if mag(rt)<R:
    n = n + 1
    cylinder(pos=rt, axis = drr*vector(0,1,0), radius=sqrt(dA/pi),color=color.yellow)
    dphi2 = dot(curlF(rt),vector(0,1,0))*dA
    phi2 = phi2 + dphi2
    
print("Flux 2 = ",phi2)

center = vector(0,1/2,0)
rt = 1.5*R*vector(2*random()-1,2*random()-1,2*random()-1)+center

n = 0
N = 2000
drr = 0.01
dA = R*2*pi*R/N
phi3 = 0
while n<N:
  rt = R*vector(2*random()-1,2*random()-1,2*random()-1)+center
  rtxz = vector(rt.x,0,rt.z)
  if mag(rtxz)>R-drr and mag(rtxz)<R+drr and rt.y>0 and rt.y<R:
    cylinder(pos=rt, axis=drr*norm(rtxz),radius=sqrt(dA/pi),color=color.cyan)
    dphi3 = dot(curlF(rt),norm(rtxz))*dA
    phi3 = phi3 + dphi3
    n = n + 1

n = 0
N = 2000
dA = pi*R**2/N

while n<N:
  rt = R*vector(2*random()-1,R,2*random()-1)
  rty = vector(rt.x,0,rt.z)

  if mag(rty)<R:
    
    cylinder(pos=rt, axis = drr*vector(0,1,0), radius=sqrt(dA/pi),color=color.cyan)
    dphi3 = dot(curlF(rt),vector(0,1,0))*dA
    phi3 = phi3 + dphi3
    n = n + 1

print("Flux 3 = ",phi3)
  
