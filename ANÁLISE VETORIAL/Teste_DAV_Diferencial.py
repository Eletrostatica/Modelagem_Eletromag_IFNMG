##################################################################################################################
################################################### INSTRUÇÕES ###################################################

# As variaveis A e B utilizadas nas funções para calcular o DESLOCAMENTO DIFERENCIAL, AREA DIFERENCIAL E VOLUME 
# DIFERENCIAL, são os pontos de onde o diferencial será calculado, assim A e B são vetores de 3 posições cada.
# Assim o input desses pontos ou as variações em cada eixo pode ser feito dessa maneira:
#                                             A = [valor, valor, valor];
#                                             B = [valor, valor, valor];
# Caso a variavel do eixo seja constante basta colocar o mesmo valor no dois vetores

# Além disso nos coordenadas cilintricas e esfericas, o valor de theta ou phi deve estar em radianos

##################################################################################################################
############################################### FIM DAS INSTRUÇÕES ###############################################


import DAV_Diferencial
from DAV_Diferencial import *

# ################################### TESTES ###################################
# # Questões 3.1 até 3.3 - 3 ed

# =========================== COORDENADAS CARTESIANAS ==========================
# --------------------------- DESLOCAMENTO DIFERENCIAL -------------------------
# A = [1, 2, 3];
# B = [4, 5, 6];
# print(dl_cart(A, B));

# --------------------------- DESLOCAMENTO DIFERENCIAL -------------------------
# A = [1, 2, 3];
# B = [4, 5, 6];
# print(dS_cart(A, B));

# ------------------------------ VOLUME DIFERENCIAL ----------------------------
# A = [1, 2, 3];
# B = [4, 5, 6];
# print(dV_cart(A, B));

######################################################################################

# --------------------------- DESLOCAMENTO DIFERENCIAL CILINDRICO -------------------------
# A = [3, pi/4, 0];
# B = [3, pi/2, 0];
# print(dl_cilind(A, B));

# --------------------------- DESLOCAMENTO DIFERENCIAL ESFERICO -------------------------
# A = [1, 30*pi/180, 0];
# B = [1, 30*pi/180, 60*pi/180];
# print(dl_esfer(A, B));

# A = [4, 30*pi/180, 0];
# B = [4, 90*pi/180, 0];
# print(dl_esfer(A, B));

# ------------------------------ AREA DIFERENCIAL CILINDRICO ----------------------------
# A = [2, pi/3, 0];
# B = [2, pi/2, 5];
# print(dS_cilind(A, B));

# A = [1, 0, 1];
# B = [3, pi/4, 1];
# print(dS_cilind(A, B));

# ------------------------------ AREA DIFERENCIAL ESFERICO ----------------------------
# A = [10, pi/4, 0];
# B = [10, 2*pi/3, 2*pi];
# print(dS_esfer(A, B));

# A = [0, 60*pi/180, 0];
# B = [4, 90*pi/180, 0];
# print(dS_esfer(A, B));

# ------------------------------ VOLUME DIFERENCIAL CARTESIANO ----------------------------
# A = [0, 1, -3];
# B = [1, 2, 3];
# print(dV_cart(A, B));

# ------------------------------ VOLUME DIFERENCIAL CARTESIANO ----------------------------
# A = [2, pi/3, -1];
# B = [5, pi, 4];
# print(dV_cilind(A, B));

# ------------------------------ VOLUME DIFERENCIAL CARTESIANO ----------------------------
# A = [1, pi/2, pi/6];
# B = [3, 2*pi/3, pi/2];
# print(dV_esfer(A, B));