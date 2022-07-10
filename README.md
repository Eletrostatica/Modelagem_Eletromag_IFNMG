# Modelagem_Eletromag_IFNMG
Modelagem em Python - Eletromagnetismo
## Exemplo do uso de imagem no repositório#
<img src="imgteste.jpg" alt="My cool logo"/>


#  Instruções de Uso da Biblioteca Eletrostatica.py  #

**----------------------------------------------------------------------------------------**

### Funções Auxiliares

**----------------------------------------------------------------------------------------**

**add_info(info)**

Recebe uma Informação e Adiciona no vetor global Vet_info (usado para guardar informações vetoriais).

**add_info_escalar(info)**

Recebe uma Informação e Adiciona no vetor global Vet_esc (usado para guardar informações escalares).

**print_Vet_info()**

Exibe as informações no vetor global Vet_info.

**clear_Vet_info_and_esc()**

Exclui dados armazenados nos Vetores Globais.

**Dist_p1_p2(p1, p2)** 

Recebe dois pontos e retorna a distância entre eles, onde cada ponto é um vetor com (ax, ay, az).

**Vet_resultante(p1,p2)**

Recebe dois Pontos e retorna o vetor ponto1-ponto2.

**Soma_vet(vetores)** 

Recebe um vetor de "vetores" e retorna um vetor que é a soma dos vetores presentes na lista de vetores

**----------------------------------------------------------------------------------------**

### Funções Específicas

**----------------------------------------------------------------------------------------**

**Forca(q1, pos1, q2, pos2);**

Recebe duas Cargas e suas respectivas posições, e retorna o vetor força na carga q1 que é um vetor (F_ax, F_ay, F_az). 

**Campo_eletrico(q1, pos1, pos_ref)**

Recebe a carga(q1) responsável pelo campo e sua respectiva posicão (pos1), e a posição (pos_ref) para calcular o campo. Retorna o vetor campo elétrico, na posição de referência.

**Intensidade_Campo(vetc)**

**Fluxo_de_Carga_Pontual(valor_carga)**

Recebe um vetor campo elétrico e retorna a intensidade (módulo)

**Campo_esfera_Conc_Casca(valor_cargesf, raio_gausiana, raio_esfer,raioext_cas,raioint_cas)**

**Potencial Elétrico():**

**INCOMPLETO !!!!!!!!!**

**----------------------------------------------------------------------------------------**

### EXEMPLOS

**----------------------------------------------------------------------------------------**

**Exemplo de Força** :Duas cargas pontuais de 1mC e -2mC, estão localizadas em (3,2,-1) e (-1,-1,4).Calcule a força elétrica sobre uma carga de 10nC, localizada em (0,3,1) e intensidade do campo elétrico nesse ponto.

**Exemplo para carga, linha inf e sup de cargas:** Uma carga pontual 100 pC está localizada em (4,1,-3), enquanto o eixo x está carregado com 2n C/m. Se o plano Z = 3 também estiver carregado com 5 n C/m² . Determine E no ponto (1,1,1).

**Exemplo esfera concentrica:** Uma esfera maciça, de raio a = 2,00 cm, é concêntrica com uma casca esférica condutora de raio interno b = 2,00a e raio externo c = 2,40a. A esfera possui carga uniforme q1 = +5,00 fC, e a casca, uma carga q2 = –q1. Determine o módulo do campo elétrico (a) em r = a/2,00, (b), (c) em r = 2,30a  e (d) em r = 3,50a.

**Exemplo1 Potencial Elétrico:** Três cargas pontuais Q1 = 1 mC, Q2 = −2mC, Q3 = 3 mC, estao localizadas, respectivamente, em (0,0,4), (-2,5,1) e (3,-4,6).

a) Determine o potencial V_P em P (-1,1,2)

b) Calcule a diferença de potencial V_PQ se Q (1,2,3)


**Exemplo2 Potencial Elétrico:** Uma carga pontual está localizada na origem. Se V = 2V em (0,6,-8),determine:

a) O potencial em A(-3,2,6)

b) O potencial em B(1,5,7)

c) A diferença de potencial

**----------------------------------------------------------------------------------------**


# -------------------------------------------------------- #
