import math
from trab_eletromag_analisevet import vet_uni,inserir_pv_cart

################### Instruções de Uso ##################

# Dist_p1_p2(ponto1, ponto2)
# retorna a distância entre esses dois pontos, onde
# onde cada ponto é um vetor com (ax, ay, az).


# Vet_resultante(ponto1(vetor),ponto2(vetor))
# retorna o vetor ponto1-ponto2

# Soma_vet((lista de vetores))
# retorna um vetor, que é a soma dos vetores presentes na lista de vetores

# Forca(carga1(escalar), posição da carga1(vetor), carga2(escalar), posição da carga2(vetor))
# Restorna o vetor força, entre a carga1 e a carga 2
# Exemplo :Duas cargas pontuais de 1mC e -2mC, estão localizadas em (3,2,-1) e
# (-1,-1,4).Calcule a força elétrica sobre uma carga de 10nC, localizada em (0,3,1)
# e intensidade do campo elétrico nesse ponto.

# Campo_eletrico(carga1, posição da carga1, posição de referência)
# retorna o vetor campo elétrico, na posição de referência


# Constantes
Eo= 4*math.pi*8.854*math.pow(10,-12)
K= 9*math.pow(10,9)

def Dist_p1_p2(p1,p2):
    dist = math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2)+math.pow(p1[2]-p2[2],2))
    return dist

def Vet_resultante(p1,p2):
    vet_resul = [p1[0]-p2[0], p1[1]-p2[1],p1[2]-p2[2]]
    return vet_resul

def Soma_vet(vetores):
    vet_result = [0, 0, 0]
    for i in range(0, len(vetores), 1):
        n_vet = vetores[i]
        vet_result[0] = vet_result[0]+n_vet[0]
        vet_result[1] = vet_result[1]+n_vet[1]
        vet_result[2] = vet_result[2]+n_vet[2]
    return vet_result

#Lei de Coulomb
def Forca(q1, pos1, q2, pos2):
    dist = Dist_p1_p2(pos1, pos2)
    vet = vet_uni(Vet_resultante(pos1, pos2)[0],Vet_resultante(pos1, pos2)[1],Vet_resultante(pos1, pos2)[2])
    const = K*q1*q2/math.pow(dist, 2)
    Fe = [const*vet[0], const*vet[1], const*vet[2]]
    return Fe

def Campo_eletrico(q1, pos1, pos_ref):
    dist = Dist_p1_p2(pos_ref, pos1)
    vet = vet_uni(Vet_resultante(pos_ref, pos1)[0], Vet_resultante(pos_ref, pos1)[1], Vet_resultante(pos_ref, pos1)[2])
    const = K*q1/math.pow(dist, 2)
    Ce = [const*vet[0], const*vet[1], const*vet[2]]
    return Ce

def Intensidade_Campo(vetc):
    valor = math.pow(vetc[0], 2) + math.pow(vetc[1], 2) + math.pow(vetc[2], 2)
    intensidade = math.sqrt(valor)
    return intensidade

def Linha_inf_de_carga(Carga_linha, eixo, pos_eixo, pos_ref):
    if eixo == "x":
        vet = [pos_eixo, pos_ref[1], pos_ref[2]]
        vetuni = vet_uni(vet[0], vet[1], vet[2])
        const = Carga_linha / (2 * math.pi * Eo * Dist_p1_p2(vet, pos_ref))
        Campo_result1 = [const * vetuni[0], const * vetuni[1], const * vetuni[2]]
        return Campo_result1
    elif eixo == "y":
        vet = [pos_ref[0], pos_eixo, pos_ref[2]]
        vetuni = vet_uni(vet[0], vet[1], vet[2])
        const = Carga_linha / (2 * math.pi * Eo * Dist_p1_p2(vet, pos_ref))
        Campo_result2 = [const * vetuni[0], const * vetuni[1], const * vetuni[2]]
        return Campo_result2
    elif eixo == "z":
        vet = [pos_ref[0], pos_ref[1], pos_eixo]
        vetuni = vet_uni(vet[0], vet[1], vet[2])
        const = Carga_linha / (2 * math.pi * Eo * Dist_p1_p2(vet, pos_ref))
        Campo_result3 = [const * vetuni[0], const * vetuni[1], const * vetuni[2]]
        return Campo_result3

def Menu_eletrostatica():
    print("################################################################")
    print("# Digite a opção desejada:                                     #")
    print("# 1 - Força entre duas cargas                                  #")
    print("# 2 - Campo elétrico em um determinado ponto                   #")
    print("# 3 - Intensidade do Campo elétrico                            #")
    print("# 4 - Sobreposição de Força ou Campo                           #")
    print("################################################################")
    resp = int(input("# Número escolhido: "))

    ############################## Força elétrica ###########################
    if resp == 1:
        q1 = float(input("Valor da carga q1 em Coulomb: "))
        q2 = float(input("Valor da carga q2 em Coulomb: "))
        print("Posição da carga q1: ")
        pos1 = inserir_pv_cart()
        print("Posição da carga q2: ")
        pos2 = inserir_pv_cart()
        F = Forca(q1, pos1, q2, pos2)
        print("A Força entre q1 e q2 é: Fe = {} N\n".format(F))
    ########################### Campo Elétrico #############################
    if resp == 2:
        q1 = float(input("Valor da carga q1 em Coulomb: "))
        print("Posição da carga q1: ")
        pos1 = inserir_pv_cart()
        print("Posição de referência: ")
        pos_ref = inserir_pv_cart()
        Ce = Campo_eletrico(q1, pos1, pos_ref)
        print("O campo elétrico em {} é: Ce = {} V/m\n".format(pos_ref, Ce))
    ########################### Intensidade de Campo elétrico ###############
    if resp == 3:
        print("Digite o vetor do campo elétrico, para saber sua intensidade: ")
        Campo = inserir_pv_cart()
        I = Intensidade_Campo(Campo)
        print("A intensidade do campo elétrico {} V/m é = {} V/m".format(Campo, I))

    ########################## Sobreposição de Força ou Campo ################
    if resp == 4:
        tipo = str(input("Será superposição de Força ou Campo? [N]->Força ou [C]-> Campo ")).upper()
        vetores = []
        while True:
            vet = inserir_pv_cart()
            vetores.append(vet)
            opc = str(input("Você deseja adicionar mais um vetor? [s] ou [n] -> ")).lower()
            if opc == "n":
                break
        vet = Soma_vet(vetores)
        if tipo == "N":
            print("A força Resultante é : {} N\n".format(vet))
        elif tipo == "C":
            print("O Campo Resultante é : {} V/m\n".format(vet))

            
            
            
            
#1. Lei de coulomb, superposição de cargas pontuais (ok)
#2. Intensidade de campo elétrico(ok)
#3. Campo elétrico em distribuição contínua de cargas (linhas de carga, superfície de cargas,
#volume de cargas)(---)
#4. Densidade de fluxo elétrico(----)
#5. Lei de Gauss(---)
#6. Potencial elétrico(---) 
