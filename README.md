# Uma Análise Exploratória de Dados utilizando os microdados públicos da base Pessoa do Cadastro Único (CadÚnico) de 2018

**Processo Seletivo:** Programa de Trainee da consultoria socioeconômica DataBrasil Analytics  
**Candidatos:** Arthur Vieira Silva e Matheus Barbosa Brandão
---

## 1. Resumo

Este repositório apresenta os resultados do processamento e análise dos microdados da base Pessoa do Cadastro Único (CadÚnico) de 2018. O objetivo foi mapear o perfil demográfico, as condições do mercado de trabalho e o nível de vulnerabilidade social das pessoas cadastradas.

---

## 2. Principais insights

### 2.1. Distribuição Demográfica por Sexo e Cor/Raça
A análise da distribuição ida petária dividor sexo/gênero e cor/raça demonstra diferenças marcantes no perfil populacional:
* **População Branca:** Apresenta médias de idade de **27,6** anos (homens) e **31,3** anos (mulheres), com medianas de **20,0** e **29,0** anos, respectivamente, e desvios padrão de **22,1** e **21,5** anos;
* **População Preta:** Apresenta as maiores médias de idade da amostra, alcançando **31,7** anos para o sexo masculino e **34,8** anos para o feminino, com medianas de **28,0** e **34,0** anos, respectivamente, e desvios padrão de **21,0** e **19,1** anos;
  * **População Parda:** Registra médias de idade de **27,3** anos (homens) e **31,0** anos (mulheres), com medianas de **20,0** e **29,0** anos, respectivamente, e desvios padrão de **22,1** e **20,4 anos** anos;
* **População Amarela:** Apresenta médias de idade de **25,6** anos (homens) e **28,6** anos (mulheres), com medianas de **19,0** e **26,0** anos, respectivamente, e desvios padrão de **20,1** e **19,3** anos;
* **População Indígena:** Apresenta-se como o grupo mais jovem da base, registrando média de idade de **21,1 anos** (homens) e **23,3 anos** (mulheres), com medianas de **16,0** e **20,0** anos, respectivamente, e desvios padrão de **17,2** e **16,9** anos.

### 2.2. Mercado de Trabalho e Formalidade (PIA)
Considerando os indivíduos em idade ativa (**PIA - 18 a 65 anos**):
* A taxa proporcional de trabalhadores **formais** (com carteira assinada) na PIA é de **37,09%**.
* A taxa proporcional de trabalhadores **informais** capturados na base é de **1,35%**.
* Dentre o subconjunto da população efetivamente ocupada, **96,50%** encontram-se em postos formais e **3,50%** em condições informais.

### 2.3. Renda Média por Nível de Instrução
Identificou-se uma forte correlação positiva entre o nível educacional e a renda média do trabalho individual:
* **Sem instrução:** R$ 125,97;
* **Fundamental (Incompleto/Completo):** R$ 134,48 a R$ 124,54;
* **Médio Incompleto:** R$ 225,36;
* **Médio Completo / Superior Incompleto:** R$ 319,81;
* **Superior Completo:** R$ 483,80.

### 2.4. Trabalho Remunerado por Faixa Etária
A proporção de cadastrados que declaram possuir trabalho remunerado varia fortemente por faixa etária:
* **Crianças e Adolescentes (0-17):** 0,18%;
* **Jovens (18-29):** 26,98%;
* **Adultos (30-59):** 48,11%;
* **Idosos (60+):** 10,87%.

### 2.5. Pessoas com Deficiência (PCD) por Faixa de Renda Per Capita
O percentual de PCDs reportadas eleva-se proporcionalmente nas faixas de renda ligeiramente superiores dentro do cadastro:
* **Até R$ 109,00:** 2,33%;
* **R$ 109,00 a R$ 218,00:** 2,59%;
* **R$ 218,00 até 1/2 salário mínimo (R$ 477,00):** 8,10%;
* **Acima de 1/2 salário mínimo:** 9,05%.

---

## 3. Respostas Detalhadas às Perguntas Estratégicas

### 1. Desigualdade de Renda e Interseccionalidade (Renda x Gênero x Cor/Raça). 
Qual é a diferença na média e na mediana da renda individual de 
trabalho entre homens e mulheres quando agrupados por cor/raça (branca,
preta, parda, amarela e indígena)?

Em todas as categorias de cor/raça, os homens superam as mulheres em média e mediana de renda individual de trabalho. 

| Cor/Raça | Média (Homens) | Média (Mulheres) | Diferença Média | Mediana (Homens) | Mediana (Mulheres) | Diferença Mediana |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Branca** | R$ 798,27 | R$ 630,06 | + R$ 168,21 | R$ 700,00 | R$ 450,00 | + R$ 250,00 |
| **2. Preta** | R$ 602,08 | R$ 478,53 | + R$ 123,54 | R$ 400,00 | R$ 300,00 | + R$ 100,00 |
| **3. Parda** | R$ 646,90 | R$ 533,13 | + R$ 113,77 | R$ 400,00 | R$ 320,00 | + R$ 80,00 |
| **4. Amarela** | R$ 527,83 | R$ 447,60 | + R$ 80,23 | R$ 300,00 | R$ 280,00 | + R$ 20,00 |
| **5. Indígena** | R$ 421,41 | R$ 347,99 | + R$ 73,43 | R$ 250,00 | R$ 200,00 | + R$ 50,00 |

### 2. Relação entre Nível de Escolaridade e Trabalho Informal
Qual é a taxa percentual de trabalhadores na condição de trabalho 
informal em cada um dos níveis de escolaridade (sem instrução, 
fundamental, médio e superior)?

A informalidade afeta de maneira desigual os trabalhadores conforme sua escolaridade:
* **Sem instrução:** 4,55%;
* **Fundamental:** 4,31%;
* **Médio:** 2,04%;
* **Superior:** 1,46%.

### 3. Perfil de Vulnerabilidade e Acessibilidade de Pessoas com Deficiência (PCD)
Qual é a proporção de Pessoas com Deficiência (PCD) registradas por 
faixa etária (Crianças/Adolescentes: 0-17, Jovens: 18-29, Adultos: 
30-59, Idosos: 60+) e qual a percentagem destas pessoas que vivem em 
famílias classificadas na extrema pobreza (renda per capita familiar de
até R$ 89,00 em 2018)?

* **Proporção de PCD por Faixa Etária:** Crianças/Adolescentes (**2,19%**), Jovens (**3,53%**), Adultos (**6,38%**) e Idosos (**13,47%**).
* **Vulnerabilidade na Extrema Pobreza:** **26,83%** de todas as Pessoas com Deficiência cadastradas vivem em famílias em situação de extrema pobreza (renda familiar per capita de até R$ 89,00 em 2018).

### 4. Impacto da Presença de Crianças na Ocupação das Mães/Responsáveis
Qual é a taxa de ocupação (trabalho remunerado) entre mulheres
responsáveis pelo domicílio que possuem crianças de 0 a 6 anos na 
família, em comparação com aquelas que não possuem crianças nessa faixa 
etária?

* **Mulheres responsáveis sem crianças de 0 a 6 anos:** 36,30% de taxa de ocupação.
* **Mulheres responsáveis com crianças de 0 a 6 anos na família:** 37,20% de taxa de ocupação. 
* Os dados demonstram a necessidade de inserção no mercado de trabalho independentemente dos encargos de cuidado infantil

---

## 4. Como Executar o arquivo main.py
1. Instale o Python e as bibliotecas `pandas` e `numpy`;
2. Adicione o arquivo CSV da amostra (`amostra.csv`) na raiz do diretório;
3. Execução do arquivo `main.py`:

   ```bash
   python main.py
