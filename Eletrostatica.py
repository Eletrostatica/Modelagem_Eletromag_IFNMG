import math
from trab_eletromag_analisevet import vet_uni,inserir_pv_cart
#from numpy import format_float_scientific



# Constantes
Eo= (math.pow(10,-9))/(36*math.pi)
K= 9*math.pow(10,9)

# Variáveis Globais
Vet_info = []
Vet_esc = []


def add_info(info):
    op = str(input("Deseja guardar essa informação? [s] ou [n] ")).lower()
    if op == "s":
        Vet_info.append(info)
        print("Informação amazenada com sucesso!!!")
    elif op == "n":
        print("A informação não foi armazenada")

def add_info_escalar(info):
    op = str(input("Deseja guardar essa informação? [s] ou [n] ")).lower()
    if op == "s":
        Vet_esc.append(info)
        print("Informação amazenada com sucesso!!!")
    elif op == "n":
        print("A informação não foi armazenada")

def print_Vet_info(vet):
    for i in vet:
        print(" Na posição {} temos: {}\n".format(i, Vet_info[i]))

def clear_Vet_info_and_esc():
    Vet_esc.clear()
    Vet_info.clear()
    print("A lista está limpa!!!!")

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

def Linha_inf_de_carga(Carga_linha, eixo1, eixo2, pos_eixo1,pos_eixo2, pos_ref):
    if eixo1 == "x" and eixo2 == "y":
        ponto_linha = [pos_eixo1, pos_eixo2, pos_ref[2]]
        vet = Vet_resultante(pos_ref, ponto_linha)
        vetuni = vet_uni(vet[0], vet[1], vet[2])
        const = Carga_linha / (2 * math.pi * Eo * Dist_p1_p2(pos_ref, ponto_linha))
        Campo_result = [const * vetuni[0], const * vetuni[1], const * vetuni[2]]
        return Campo_result
    elif eixo1 == "x" and eixo2 == "z":
        ponto_linha = [pos_eixo1, pos_ref[1], pos_eixo2]
        vet = Vet_resultante(pos_ref, ponto_linha)
        vetuni = vet_uni(vet[0], vet[1], vet[2])
        const = Carga_linha / (2 * math.pi * Eo * Dist_p1_p2(pos_ref, ponto_linha))
        Campo_result = [const * vetuni[0], const * vetuni[1], const * vetuni[2]]
        return Campo_result
    elif eixo1 == "y" and eixo2 == "z":
        ponto_linha = [pos_ref[0], pos_eixo1, pos_eixo2]
        vet = Vet_resultante(pos_ref, ponto_linha)
        vetuni = vet_uni(vet[0], vet[1], vet[2])
        const = Carga_linha / (2 * math.pi * Eo * Dist_p1_p2(pos_ref, ponto_linha))
        Campo_result = [const * vetuni[0], const * vetuni[1], const * vetuni[2]]
        return Campo_result

def Superficie_de_carga(Carga_Sup, eixo_norm, pos_sup, ponto_ref):
    if eixo_norm == "x":
        if ponto_ref[0] > pos_sup:
            const = (Carga_Sup)/(2*Eo)
            Campo_result = [const, 0, 0]
            return Campo_result
        elif ponto_ref[0] < pos_sup:
            const = (Carga_Sup) / (2 * Eo)
            Campo_result = [-1*const, 0, 0]
            return Campo_result
    if eixo_norm == "y":
        if ponto_ref[1] > pos_sup:
            const = (Carga_Sup)/(2*Eo)
            Campo_result = [0, const, 0]
            return Campo_result
        elif ponto_ref['0'] < pos_sup:
            const = (Carga_Sup) / (2 * Eo)
            Campo_result = [0, -1*const, 0]
            return Campo_result
    if eixo_norm == "z":
        if ponto_ref[2] > pos_sup:
            const = (Carga_Sup)/(2*Eo)
            Campo_result = [0, 0, const]
            return Campo_result
        elif ponto_ref[2] < pos_sup:
            const = (Carga_Sup) / (2 * Eo)
            Campo_result = [0, 0, -1*const]
            return Campo_result

def Volume_de_carga(Carga_volum, pos_centro, pos_ref):
    dist = Dist_p1_p2(pos_ref, pos_centro)
    vet = vet_uni(Vet_resultante(pos_ref, pos_centro)[0], Vet_resultante(pos_ref, pos_centro)[1], Vet_resultante(pos_ref, pos_centro)[2])
    const = K*Carga_volum/math.pow(dist, 2)
    Ces = [const*vet[0], const*vet[1], const*vet[2]]
    return Ces

def Densidade_de_fluxo_cp(q1, pos1, pos_ref):
    vet = Campo_eletrico(q1, pos1, pos_ref)
    D = [Eo*vet[0], Eo*vet[1], Eo*vet[2]]
    return D

def Densidade_de_fluxo_sp(vet_campo):
    D = [Eo*vet_campo[0], Eo*vet_campo[1], Eo*vet_campo[2]]
    return D

def Campo_esfera_Conc_Casca(valor_cargesf, raio_gausiana, raio_esfer,raioext_cas,raioint_cas):
    if (raio_gausiana >= 0) and (raio_gausiana <= raio_esfer):
        E=((1/(4*math.pi*Eo))*(valor_cargesf/(math.pow(raio_esfer,3)))*raio_gausiana)
        return E
    elif(raio_esfer<=raio_gausiana) and (raio_gausiana<=raioint_cas):
        E=((1/(4*math.pi*Eo))*(valor_cargesf/math.pow(raio_gausiana,2)))
        return E
    elif (raio_gausiana >= raioint_cas and raio_gausiana <= raioext_cas):
        E = 0
        return E

def Fluxo_de_Carga_Pontual(valor_carga):
    Fluxo = valor_carga/Eo
    return Fluxo

def Pontencial_Eletrico(valor_carga, pos_carga, pos_desejada, pos_refer, ddp_ref):
    if (pos_refer == "inf") and (ddp_ref) == 0:
        Tensao = valor_carga/(4*math.pi*Eo*Dist_p1_p2(pos_desejada, pos_carga))
        return Tensao
    else:
        C = ddp_ref-((4*math.pi*Eo*Dist_p1_p2(pos_refer, pos_carga))/valor_carga)
        Tensao = (valor_carga / (4 * math.pi * Eo * Dist_p1_p2(pos_desejada, pos_carga))) + C
        return Tensao

def Diferenca_de_Potencial(V1, V2):
    ddp = V2 - V1
    return ddp

def Sobreposicao_de_Potencial_eletrico(vetor):
    soma = 0
    for i in range(0, len(vetor), 1):
        soma = soma + vetor[i]
    return soma

##################### Funções de Leitura ######################
def Ler_unidade():

    unidade = str(input("Qual a unidade? : ")).lower().strip()

    if unidade == "norm": #(normal sem potencia)
        v = 1
        return v
    if unidade == "mili":
        v = math.pow(10,-3)
        return v
    if unidade == "micro":
        v = math.pow(10, -6)
        return v
    if unidade == "nano":
        v = math.pow(10, -9)
        return v
    if unidade == "pico":
        v = math.pow(10, -12)
        return v

def Ler_Carga():
    q = float(input("Carga: "))
    unidade = Ler_unidade()
    return q*unidade

def Ler_Info_Forca():
    print("Valor da carga q1 em Coulomb: ")
    q1 = Ler_Carga()
    print("Valor da carga q2 em Coulomb: ")
    q2 = Ler_Carga()
    print("Posição da carga q1: ")
    pos1 = inserir_pv_cart()
    print("Posição da carga q2: ")
    pos2 = inserir_pv_cart()
    vet = [q1, pos1, q2, pos2]
    return vet

def Ler_Info_Campo():
    print("Valor da carga q1 em Coulomb: ")
    q1 = Ler_Carga()
    print("Posição da carga q1: ")
    pos1 = inserir_pv_cart()
    print("Posição de referência: ")
    pos_ref = inserir_pv_cart()
    vet = [q1, pos1, pos_ref]
    return vet

def Ler_Info_linha_Inf_Carga():
    print("Qual a carga presente na Linha infinita? : ")
    carga = Ler_Carga()
    eixo1 = str(input("Qual o primeiro Eixo da Linha? : ")).lower().strip()
    pos_eixo1 = float(input("Qual a posição do eixo? : "))
    eixo2 = str(input("Qual o segundo Eixo da Linha? : ")).lower().strip()
    pos_eixo2 = float(input("Qual a posição do eixo? : "))
    print("Ponto em que deseja calcular o campo: ")
    pos_ref = inserir_pv_cart()
    vet = Linha_inf_de_carga(carga, eixo1, eixo2, pos_eixo1, pos_eixo2, pos_ref)
    return vet

def Ler_Info_Sup_de_Carga():#(Carga_Sup, eixo_norm, pos_eixo, pos_ref)
    print("Qual a carga presente na Superfície? ")
    carga = Ler_Carga()
    eixo_norm = str(input("Qual o eixo da Normal? : ")).lower().strip()
    pos_eixo = float(input("Qual a posição do plano no eixo {}?  : ".format(eixo_norm)))
    print("Qual a posição de Referencia? ")
    pos_ref = inserir_pv_cart()
    vet = Superficie_de_carga(carga, eixo_norm, pos_eixo, pos_ref)
    return vet

def Ler_Info_Volume_de_carga():
    print("Valor da distribuição volumétrica de carga: ")
    q1 = Ler_Carga()
    print("Posição do centro da esfera: ")
    pos1 = inserir_pv_cart()
    print("Posição de referência: ")
    pos_ref = inserir_pv_cart()
    vet = Volume_de_carga(q1, pos1, pos_ref)
    return vet

def Ler_Info_Campo_esfera_Conc_Casca():
    print("Qual o valor da carga uniforme da esfera? ")
    q = Ler_Carga()
    a = float(input('Qual o valor do raio da esfera?'))
    b = float(input('Qual o valor do raio interno da casca esférica?'))
    c = float(input('Qual o valor do raio externo da casca esférica?'))
    r = float(input('Qual o valor do raio que deseja calcular o campo elétrico?'))
    modulo = Campo_esfera_Conc_Casca(q, r, a, b, c)
    return modulo

def Ler_Info_Fluxo_de_Carga_Pontual():
    q = Ler_Carga()
    valor = Fluxo_de_Carga_Pontual(q)
    return valor

def Ler_Info_Potencial_eletrico():
    print("Digite o Valor da carga 'q': ")
    carga = Ler_Carga()
    print("Qual a posição da sua carga? ")
    pos_carga = inserir_pv_cart()
    print("Qual a Posição que deseja calcular o Potencial Elétrico? ")
    pos_desejada = inserir_pv_cart()
    perg_referencia = str(input("Sua Referência é o Infinito com 0V? [s] ou [n] : ")).lower().strip()
    if perg_referencia == "s":
        return Pontencial_Eletrico(carga, pos_carga, pos_desejada, "inf", 0)
    else:
        print("Digite o ponto da Referência: ")
        pos_ref = inserir_pv_cart()
        ddp_ref = float(input("Qual o Potencial Elétrico neste ponto: "))
        return Pontencial_Eletrico(carga, pos_carga, pos_desejada, pos_ref, ddp_ref)

def Ler_Info_DDP():
    V1 = float(input("Potencial Elétrico V1: "))
    V2 = float(input("Potencial Elétrico V2: "))
    return V2-V1



def Menu_eletrostatica():
    while True:
        print("################################################################")
        print("# Digite a opção desejada:                                     #")
        print("# 1 - Força entre duas cargas                                  #")
        print("# 2 - Campo elétrico em um determinado ponto                   #")
        print("# 3 - Intensidade do Campo elétrico                            #")
        print("# 4 - Sobreposição de Força ou Campo                           #")
        print("# 5 - Campo de Linha Infinita de Cargas                        #")
        print("# 6 - Campo de Superfície de Cargas (plano)                    #")
        print("# 7 - Campo de Volume de Cargas (esfera)                       #")
        print("# 8 - Módulo de campo elétrico concêntrica a uma casca         #")
        print("# 9 - Densidade de Fluxo                                       #")
        print("#10 - Fluxo de campo Elétrico de uma carga pontual             #")
        print("#11 - Potencial Elétrico                                       #")
        print("#12 - Diferença de Potencial Elétrico                          #")
        print("#13 = Sobreposição de Potencial Elétrico                       #")
        print("#14 - Mostrar Lista                                            #")
        print("#15 - limpar Lista                                             #")
        print("#16- Sair                                                      #")
        print("################################################################")
        resp = int(input("# Número escolhido: "))

        ############################## Força elétrica ###########################
        if resp == 1:
            vet = Ler_Info_Forca()
            F = Forca(vet[0], vet[1], vet[2], vet[3])
            print("A Força entre q1 e q2 é: Fe = {} N\n".format(F))
            add_info(F)
        ########################### Campo Elétrico #############################
        if resp == 2:
            vet = Ler_Info_Campo()
            Ce = Campo_eletrico(vet[0], vet[1], vet[2])
            print("O campo elétrico em {} é: Ce = {} V/m\n".format(vet[2], Ce))
            add_info(Ce)
        ########################### Intensidade de Campo elétrico ###############
        if resp == 3:
            print("Digite o vetor do campo elétrico, para saber sua intensidade: ")
            Campo = inserir_pv_cart()
            I = Intensidade_Campo(Campo)
            print("A intensidade do campo elétrico {} V/m é = {} V/m".format(Campo, I))

        ########################## Sobreposição de Força ou Campo ################
        if resp == 4:
            tipo = str(input("Será superposição de Força ou Campo? [N]->Força ou [C]-> Campo ")).upper()
            perg = str(input("Deseja usar as informações armazenadas? [N] ou [S] ")).upper().strip()
            vetores = []
            if perg == "S":
                vet = Soma_vet(Vet_info)
                if tipo == "N":
                    print("A força Resultante é : {} N\n".format(vet))
                elif tipo == "C":
                    print("O Campo Resultante é : {} V/m\n".format(vet))
            elif perg == "N":
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
        if resp == 5:
            Cl = Ler_Info_linha_Inf_Carga()
            print("O campo gerado pela linha inf é: {} V/m\n".format(Cl))
            add_info(Cl)
        if resp == 6:
            Cs = Ler_Info_Sup_de_Carga()
            print("O campo gerado pela superficie inf é: {} V/m\n".format(Cs))
            add_info(Cs)
        if resp == 7:
            print("Volume de Campo")
        if resp == 8:
            modulo = Ler_Info_Campo_esfera_Conc_Casca()
            print(" O modulo do campo elétrico nesse raio é {} V/m\n".format(modulo))
        if resp == 10:
            valor = Ler_Info_Fluxo_de_Carga_Pontual()
            print("O fluxo elétrico da carga sobre a gaussiana é {} Nm²/c".format(valor))
        if resp == 11:
            Pot = Ler_Info_Potencial_eletrico()
            print("O Potencial elétrico a partir da carga informada é: {} V".format(Pot))
            add_info(Pot)
        if resp == 12:
            DDP = Ler_Info_DDP()
            print("A diferença de Potencial é: {} V".format(DDP))
        if resp == 13:
            soma = Sobreposicao_de_Potencial_eletrico(Vet_info)
            print("A soma dos Potenciais é: {} V".format(soma))

        if resp == 14:
            print_Vet_info(Vet_info)
        if resp == 15:
            print("A lista foi Limpa")
            clear_Vet_info_and_esc()
        if resp == 16:
            break
        else:
            print("Não existe essa Opção!!!\n")



Menu_eletrostatica()
            
# As funções já estão funcionando !!!       
            
            
#1. Lei de coulomb, superposição de cargas pontuais (ok)
#2. Intensidade de campo elétrico(ok)
#3. Campo elétrico em distribuição contínua de cargas (linhas de carga, superfície de cargas,
#volume de cargas)(ok)
#4. Densidade de fluxo elétrico(ok)
#5. Lei de Gauss(ok)
#6. Potencial elétrico(ok) 
