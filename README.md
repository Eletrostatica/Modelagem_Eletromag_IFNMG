# Modelagem_Eletromag_IFNMG
Modelagem em Python - Eletromagnetismo
## Exemplo do uso de imagem no repositório#
<img src="imgteste.jpg" alt="My cool logo"/>


#  Instruções de Uso da Biblioteca Eletrostatica.py  #

**Dist_p1_p2(ponto1, ponto2)** 

retorna a distância entre esses dois pontos, onde cada ponto é um vetor com (ax, ay, az).


**Vet_resultante(ponto1(vetor),ponto2(vetor))**

retorna o vetor ponto1-ponto2

->  Soma_vet((lista de vetores)); 
retorna um vetor, que é a soma dos vetores presentes na lista de vetores

->  Forca(carga1(escalar), posição da carga1(vetor), carga2(escalar), posição da carga2(vetor)); 
Retorna o vetor força, entre a carga1 e a carga 2 
Exemplo :Duas cargas pontuais de 1mC e -2mC, estão localizadas em (3,2,-1) e (-1,-1,4).Calcule a força elétrica sobre uma carga de 10nC, localizada em (0,3,1) e intensidade do campo elétrico nesse ponto.

-> Campo_eletrico(carga1, posição da carga1, posição de referência); 
retorna o vetor campo elétrico, na posição de referência

**exemplo para carga, linha inf e sup de cargas: Uma carga pontual 100 pC está localizada em (4,1,-3), enquanto o eixo x está carregado com 2n C/m. Se o plano Z = 3 também estiver carregado com 5 n C/m² . Determine E no ponto (1,1,1).

-> Fluxo_de_Carga_Pontual(valor_carga)

Exemplo: 
Uma carga pontual de 1,8 μC está no centro de uma superfície gaussiana cúbica de 55 cm de aresta.Qual é o fluxo elétrico através da superfície?


-> Campo_esfera_Conc_Casca(valor_cargesf, raio_gausiana, raio_esfer,raioext_cas,raioint_cas)

Exemplo: Uma esfera maciça, de raio a = 2,00 cm, é concêntrica com uma casca esférica condutora de raio interno b = 2,00a e raio externo c = 2,40a. A esfera possui carga uniforme q1 = +5,00 fC, e a casca, uma carga q2 = –q1. Determine o módulo do campo elétrico (a) em r = a/2,00, (b), (c) em r = 2,30a  e (d) em r = 3,50a.

-> Potencial Elétrico():

Exemplo Potencial Elétrico: Uma carga pontual está localizada na origem. Se V = 2V em (0,6,-8),determine:

#a) O potencial em A(-3,2,6)
#b) O potencial em B(1,5,7)
#c) A diferença de potencial

INCOMPLETO !!!!!!!!!
# -------------------------------------------------------- #
