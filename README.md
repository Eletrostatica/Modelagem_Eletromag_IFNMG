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

Recebe um vetor campo elétrico e retorna a intensidade (módulo)

**Linha_inf_de_carga(Carga_linha, eixo1, eixo2, pos_eixo1,pos_eixo2, pos_ref)**

Recebe a Distribuição de carga na linha, os eixos na qual a linha está localizada (strings-> "x", "y" ou "z" , e a posição(escalar) de referência para retornar o vetor campo a partir dessa posição. **obs: não realiza o calculo caso a linha inf tenha 2 ou 3 eixos variando. Para usar a função, deverá ser respeitado a ordem x->y->z de forma que caso a linha esteja no eixo x, eixo1 = "y" e eixo2 = "z", caso a linha esteja no eixo y , eixo1 = "x" e eixo2 = "z", e por último, se estiver no eixo z, eixo1 = "x" e eixo2 = "y". Outra configuração resultará em erro!!!**

**Superficie_de_carga(Carga_Sup, eixo_norm, pos_sup, ponto_ref)**

Recebe a distribuição superficial de carga no plano, eixo da normal sendo "x" ou "y" ou "z", qual a posição neste eixo da normal, e o ponto de referência para calcular o campo. Essa função, retorna o vetor campo no ponto de referência.

**Volume_de_carga(Carga_volum, pos_centro, pos_ref)**

Recebe a distribuição volumétrica de carga, a posição do centro da esfera e qual a posição para calcular o campo. Retorna um vetor campo elétrico no ponto de referência.

**Densidade_de_fluxo_cp(q1, pos1, pos_ref)**

Recebe a carga, sua posição e a posição na qual quer calcular a densidade de fluxo e Retorna o vetor densidade de fluxo.

**Densidade_de_fluxo_sp(vet_campo)**

Recebe um vetor de campo e retorna o vetor densidade de fluxo.

**Campo_esfera(valor_cargesf, raio_gausiana, raio_esfer)**

Essa função recebe valores da carga uniforme da esfera (valor_cargesf), raio da esfera (raio_esfer) e o raio de onde se deseja passar a gaussiana (raio_gausiana). Após receber esses valores do usuario, ela irá retorna o valor do módulo do campo elétrico.

**Fluxo_de_Carga_Pontual(valor_carga)**

Essa função recebe o valor da carga pontual(valor_carga), e retorna o fluxo elétrico de uma superfície, após a divissão pelo E0.

**Pontencial_Eletrico(valor_carga, pos_carga, pos_desejada, pos_refer, ddp_ref)**

Recebe uma carga, a posição da carga, a posição desejada para o potencial elétrico, posição de refêrencia e o potencial elétrico na posição de referência.**Obs: Caso a posição de referência seja o infinito com 0 V, a função entende como pos_refer = "inf" e ddp_ref = 0**

**Diferenca_de_Potencial(V1, V2)**

Recebe o potencial elétrico V1 e V2, e retorna a diferença de potencial V2-V1

**Sobreposicao_de_Potencial_eletrico(vetor)**

Recebe um vetor de potenciais elétricos e retorna a soma desses potencias elétricos contidos no vetor.

**----------------------------------------------------------------------------------------**

### Funções de Leitura

**----------------------------------------------------------------------------------------**

**Ler_unidade()**

Pergunta a Unidade de Medida utilizada sendo preciso digitar: "norm" -> 1 ; "mili" -> 10^-3 ; "micro" -> 10^-6 ; "nano" -> 10^-9 ; "pico" -> 10^-12 . Essa função retorna o escalar respectivo a unidade selecionada.

**Ler_Carga()**

Função para receber a carga pontual, distribuição superfícial e volumétrica

**Ler_Info_Forca()**

Função para receber informações para calcular a força elétrica entre duas cargas. Retorna o vetor força na primeira carga.

**Ler_Info_Campo()**

Função para receber informações para calcular o campo elétrico em determinado ponto. Retorna o vetor campo na posição de referência.

**Ler_Info_linha_Inf_Carga()**

Função para receber informações para calcular o campo elétrico em determinado ponto a partir de um distribuição contínua de carga em uma linha infinita. Retorna o vetor campo elétrico em uma posição.

**Ler_Info_Sup_de_Carga()**

Função para receber informações para calcular o campo elétrico em determinado ponto a partir de uma distribuição contínua de carga em um plano infinito. Retorna o vetor campo elétrico em uma posição.

**Ler_Info_Volume_de_carga()**

Função para receber informações para calcular o campo elétrico em determinado ponto a partir de uma distribuição contínua de carga em uma esfera. Retorna o vetor campo elétrico em uma posição. 

**Ler_Info_Campo_esfera()**

Função para receber informações para calcular o módulo do campo elétrico em uma esfera.

**Ler_Densidade_Fluxo_cp()**

Função para receber parametros do campo elétrico e calcular a densidade de fluxo.

**Ler_Densidade_Fluxo_sp()**

Função para receber as componentes vetoriais do campo elétrico e calcular a densidade de fluxo.

**Ler_Info_Fluxo_de_Carga_Pontual()**

Função para receber informações e calcular o módulo do fluxo de campo de uma carga pontual. 

**Ler_Info_Potencial_eletrico()**

Função para receber informações e calcular o potencial elétrico em um determinado ponto.

**Ler_Info_DDP()**

Função para receber informações e calcular a diferença de potencial V2-V1.

**Menu_eletrostatica()**

Função de Menu para o arquivo Eletrostatica.py, de forma que facilita o uso das funções ao executar o algoritmo

**----------------------------------------------------------------------------------------**

### EXEMPLOS

**----------------------------------------------------------------------------------------**

**Exemplo de Força** :Duas cargas pontuais de 1mC e -2mC, estão localizadas em (3,2,-1) e (-1,-1,4).Calcule a força elétrica sobre uma carga de 10nC, localizada em (0,3,1) e intensidade do campo elétrico nesse ponto.

**Exemplo para carga, linha inf e sup de cargas:** Uma carga pontual 100 pC está localizada em (4,1,-3), enquanto o eixo x está carregado com 2n C/m. Se o plano Z = 3 também estiver carregado com 5 n C/m² . Determine E no ponto (1,1,1).

**Exemplo campo esfera :** Uma esfera maciça, de raio a = 2,00 cm, possui carga uniforme q1 = +5,00 fC. Determine o módulo do campo elétrico (a) em r = a/2,00, (b)r = a e (c) em r = 2,30a.

**Exemplo de Densidade de Fluxo**: "Questão nove da Lista eletrsostática 1" -> Quatro cargas pontuais estão localizadas nos vértices de um quadrado de 4m de lado, sendo q1 = Q, q2 = -2Q , q3 = -Q e q4 = 2Q e posições P1(-2,2,0), P2(-2,-2,0), P3(2,-2,0) e P4(2,2,0), respectivamente. Se Q = 15μC, determine D em (0,0,6).

**Exemplo para fluxo de carga pontual**: Uma carga pontual de 1,8 μC está no centro de uma superfície gaussiana cúbica de 55 cm de aresta. Qual é o fluxo elétrico através da superfície?

**Exemplo1 Potencial Elétrico:** Três cargas pontuais Q1 = 1 mC, Q2 = −2mC, Q3 = 3 mC, estao localizadas, respectivamente, em (0,0,4), (-2,5,1) e (3,-4,6).

a) Determine o potencial V_P em P (-1,1,2)

b) Calcule a diferença de potencial V_PQ se Q (1,2,3)


**Exemplo2 Potencial Elétrico:** Uma carga pontual está localizada na origem. Se V = 2V em (0,6,-8),determine:

a) O potencial em A(-3,2,6)

b) O potencial em B(1,5,7)

c) A diferença de potencial




#  Instruções de Uso da Biblioteca Linhas_de_transmissao.py  #

**----------------------------------------------------------------------------------------**
###                                 Funções Auxiliares
**----------------------------------------------------------------------------------------**

**conv_angulo(T)**

Recebe um angulo em graus e converte para radianos.

**cientific_format(X)**

Recebe um numero real e converte para mostragem cientifica.

**f(x)**

Local para escrever a equação a ser integrada. (Auxiliar a função "trapezoidal(x0, xn)") 

**trapezoidal(x0, xn)**

Passo a passo do metodo trapezoidal. (Auxiliar a função "integral()")

**integral()** 

Retorna o resultado da integração.

**----------------------------------------------------------------------------------------**
###                                  Funções Específicas
**----------------------------------------------------------------------------------------**

**forca_magnetica(q,B,v,Teta)**

Recebe a carga (q), o valor do campo magnetico(B), a velocidade(v) e o angulo(Teta), e retorna o valor da força magnetica atuante sobre aquela carga. 

**ForcaM(i1, i2, r, l)**

Recebe o valor das duas correntes(i1 e i2), oa distancia entre os condutores (r) e o comprimento(l) e retorna o valor da força magnetica Força Magnetica entre os dois condutores. 

**distancia_equivalente(d12,d23,d13)**

Recebe 3 valores das distancias e retorna distancia equivalente para tres fases, de acordo com as distancias de: (1 a 2; 2 a 3; 1 a 3).

**raio_equivalente(d,r)**

Recebe o r e o diametro das fases e calcula o raio equivalente.

**calculator_capacitancia(Req,Deq)**

Calcula a capacitancia entre as fases a partir da Distancia equivalente (Deq) e do Raio equivalente (Req).

**const_a(d)**
Calcula a constante 'a' para o exemplo 6.

**calculator_indutancia(a,b)**
Recebe o valores de a(constante) e b(distancia entre os fios) e apresenta a indutancia calculada.

**calculator_indutanciamutua(fem, I0, If, variatempo)**
Recebe a tensão induzida, a corrente inicial, a corrente final e a variação de tempo e apresenta a indutancia mutua calculada.

**permeabilidade_mag(Uo, Ur)**
Retorna a permeabilidade magnetica a partir da permeabilidade relativa.

**relutancia(l, u, a)**
Retorna a relutancia a partir do comprimento, permeablidade e area

**fluxo_mag(B, a)**
Retorna o fluxo magnetico a partir do valor do campo e area.

def calc_corrente(n, f, r):
Retorna a corrente na linha a patir do numero de expiras, fluxo magnetico e relutancia.

**fluxo(Ro,fi)**
Calcula o fluxo a partir de Ro e fi.

**Fem(Ro,fi)**
Calcula a tensão induzida a partir de Ro e fi.

**corrent(Ro,fi,r)**
Calcula a corrente a partir de Ro, fi e a resistencia(r).
**----------------------------------------------------------------------------------------**
###                                     EXEMPLOS
**----------------------------------------------------------------------------------------**

**Exemplo 1 de Força Magnetica: ** Suponha que uma carga elétrica de 4 μC seja lançada em um campo magnético uniforme de 8 T. Sendo de 60ºC o ângulo formado entre v e B, determine a força magnética que atua sobre a carga supondo que a mesma foi lançada com velocidade igual a 5x10³ m/s.  

**Exemplo 2 para Força magnética entre dois condutores: ** 




**Exemplo 3 Capacitancia: ** Uma linha de tensão nominal 750kV tem 4 condutores por fase, como mostra a Imagem 1("LdT") Considere que há transposição. O raio de cada condutor é igual a 2,5cm. A partir disso determine a capacitancia da linha.

## Exemplo do uso de imagem no repositório#
<img src="img1_LdT.jpg" alt="My cool logo"/>

**Exemplo 4 INDUTANCIA: ** A distância entre os centros dos cabos de uma linha monofásica é de 3,05m. Cada cabo é composto de 7 fios iguais de diâmetro 2,54mm. Determine a indutância por unidade por unidade de comprimento desta linha.

**Exemplo 5 INDUTANCIA MUTUA: ** I1(t) diminui de 6A para zero em um tempo de 2,5 ms.Gerando uma Fem2 induzida de 30 KV; Qual a indutância mútua M ?

**Exemplo 6 Circuitos Magneticos: ** Uma bobina está enrolada em núcleo com 4cm² de seção reta, material com permeabilidade relativa de 80000, densidade de fluxo magnético B=1T, como mostra a Imagem 3 ("LdT") Calcule a relutância, fluxo e a corrente

**Exemplo 7 Campos Variáveis no tempo:**
Quetão se encontra na Imagem 4 ("LdT")

**----------------------------------------------------------------------------------------**
