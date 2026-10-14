""""
=================================================================================================================================================
    RELATÓRIO: Uma Análise Exploratória de Dados utilizando os microdados públicos da base Pessoa do Cadastro Único (CadÚnico) de 2018.
    PROCESSO SELETIVO: Programa de Trainee da consultoria socioeconômica DataBrasil Analytics
    Candidatos: Arthur Vieira Silva e Matheus Barbosa Brandão
=================================================================================================================================================

1. Introdução:

    Este relatório apresenta os resultados do processamento e análise dos 
    microdados da base Pessoa do Cadastro Único (CadÚnico) de 2018. O objetivo
    foi mapear o perfil demográfico, as condições do mercado de trabalho e o
    nível de vulnerabilidade social das pessoas cadastradas.

2. Principais insights:

    - Análise Demográfica e Mercado de Trabalho:
        1. A análise da distribuição etária por sexo/gênero e cor/raça revela
        que a população indígena apresenta a menor média de idade da base
        (aproximadamente 21 anos para homens e 23,2 anos para mulheres), com 
        mediana de 16 e 20 anos, respectivamente. A população preta apresenta 
        as maiores médias de idade, alcançando 31,7 anos para o sexo masculino 
        e 34,8 anos para o feminino;

        2. Entre os indivíduos em idade ativa (PIA - 18 a 65 anos), a taxa
        proporcional de trabalhadores formais (com carteira assinada) é de 
        37,09%, enquanto a taxa de trabalhadores informais capturados na base 
        atinge 1.35%. Considerando apenas a população efetivamente ocupada,
        96,50% encontram-se em postos formais e 3,50% em condições informais;

        3. Identificou-se uma forte correlação positiva entre o nível de
        instrução e a renda média do trabalho individual. Indivíduos sem 
        instrução recebem uma renda média de R$ 125,97, ao passo que aqueles 
        com ensino superior alcançam uma média de R$ 483,80.

    - Análise do Perfil de Trabalho e Escolaridade:
        1. A proporção de cadastrados que declaram possuir trabalho remunerado
        varia fortemente por faixa etária: é praticamente nula entre Crianças e
        Adolescentes (0,18%), sobe para 26,98% entre os Jovens (18-29 anos),
        atinge o pico de 48,11% entre os Adultos (30-59 anos) e recua para
        10,87% entre os Idosos (60+ anos);

        2. O percentual de Pessoas com Deficiência (PCD) reportadas cresce 
        conforme aumenta a faixa de renda familiar per capita, variando de 
        2,33% na faixa de até R$ 109,00 até 9,05% na faixa de renda superior a 
        meio salário mínimo.
    
    - Perguntas:
        1. Desigualdade de Renda e Interseccionalidade (Renda x Gênero x 
        Cor/Raça). 
        Qual é a diferença na média e na mediana da renda individual de 
        trabalho entre homens e mulheres quando agrupados por cor/raça (branca,
        preta, parda, amarelae indígena)?

        Em todas as categorias de cor/raça, os homens apresentam médias e 
        medianas de renda superiores às mulheres. A maior disparidade na média 
        salarial ocorre na população branca, onde os homens ganham em média 
        R$ 798,27 contra R$ 630,06 das mulheres (uma diferença de R$ 168,21). 
        Sobre a mediana, a maior diferença também se concentra na população 
        branca, com uma diferença de R$ 250,00.

        2. Relação entre Nível de Escolaridade e Trabalho Informal
        Qual é a taxa percentual de trabalhadores na condiçãoo de trabalho 
        informal em cada um dos níveis de escolaridade (sem instrução, 
        fundamental, médio e superior)?

        A taxa de informalidade é altamente sensível ao nível de escolaridade:
        atinge 4,55% entre os trabalhadores sem instrução e 4,31% no ensino
        fundamental, caindo de maneira acentuada para 2,04% no ensino médio e 
        chegando a 1,46% entre aqueles com nível superior.

        3. Perfil de Vulnerabilidade e Acessibilidade de Pessoas com
        Deficiência (PCD)
        Qual é a proporção de Pessoas com Deficiência (PCD) registradas por 
        faixa etária (Crianças/Adolescentes: 0-17, Jovens: 18-29, Adultos: 
        30-59, Idosos: 60+) e qual a percentagem destas pessoas que vivem em 
        famílias classificadas na extrema pobreza (renda per capita familiar de
        até R$ 89,00 em 2018)?

        A proporção de PCDs registradas cresce com a idade, passando de 2,19%
        entre crianças e adolescentes para 13,47% entre os idosos. Além disso, 
        constatou-se que 26,83% de todas as Pessoas com Deficiência cadastradas 
        vivem em famílias classificadas em situação de extrema pobreza (renda
        familiar per capita de até R$ 89,00).

        4. Impacto da Presença de Crianças na Ocupação das Mães/Responsáveis
        Qual é a taxa de ocupação (trabalho remunerado) entre mulheres
        responsáveis pelo domicílio que possuem crianças de 0 a 6 anos na 
        família, em comparação com aquelas que não possuem crianças nessa faixa 
        etária?

        A taxa de ocupação (trabalho remunerado) entre mulheres responsáveis
        pelo domicílio que possuem crianças de 0 a 6 anos na família é de
        37,20%, valor muito próximo ao observado entre aquelas que não possuem 
        crianças nessa faixa etária (36,30%), demonstrando a necessidade de 
        inserção no mercado de trabalho independentemente dos encargos de 
        cuidado infantil.

3. Proposta de Enriquecimento de Dados (Cruzamento de Bases):

    - Perguntas:
        5.1 Pergunta 1: A proporção de PCDs em extrema pobreza é
        maior em municípios de baixo IDEB?
        Resposta. A direção esperada é positiva: municípios com IDEB baixo tendem a apre-
        sentar percentual mais elevado de PCDs em extrema pobreza, em razão da pobreza ge-
        neralizada e da oferta insuficiente de serviços de reabilitação e educação inclusiva. A
        política pública decorrente é focalizar o BPC e a Rede de Cuidados à Pessoa com
        Deficiência nos municípios de IDEB baixo, onde a sobreposição de vulnerabilidades
        é mais intensa.
                
        5.2 Pergunta 2: A taxa de ocupação de mulheres responsáveis por
        domicílio com crianças de 0 a 6 anos é maior em municípios
        de IDEB alto?
        Resposta. Espera-se uma correlação positiva entre IDEB e taxa de ocupação femi-
        nina: municípios com IDEB alto tendem a reduzir o custo de oportunidade do trabalho
        feminino por meio de creches, escolas em tempo integral e mercado formal mais denso. A
        política pública decorrente é priorizar a expansão de creches e programas de qua-
        lificação profissional.
"""


import pandas as pd
import numpy as np
import glob
import os
import re

import matplotlib
matplotlib.use("Agg")   # backend sem interface gráfica (para salvar em arquivo)
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================================================
# FUNÇÕES ORIGINAIS - CADASTRO ÚNICO
# =============================================================================

def add_age_and_group_columns(df_cad: pd.DataFrame):
    df_cad_modified = df_cad.copy()
    df_cad_modified['DT_NASC_PESSOA'] = pd.to_datetime(
        df_cad['DT_NASC_PESSOA'], format="%Y-%m-%d", errors="coerce"
    )
    df_cad_modified['IDADE'] = (
        (pd.to_datetime("2018-12-31") - df_cad_modified['DT_NASC_PESSOA']).dt.days // 365
    )
    bins = [-1, 17, 29, 59, 150]
    labels = ["Crianças e Adolescentes", "Jovens", "Adultos", "Idosos"]
    df_cad_modified['FAIXA_ETARIA'] = pd.cut(
        df_cad_modified['IDADE'], bins=bins, labels=labels, include_lowest=True
    )
    return df_cad_modified


def calculate_age_distribution_by_sex_and_race(df_cad: pd.DataFrame):
    df_cad_modified = add_age_and_group_columns(df_cad)
    df_cad_modified = df_cad_modified.groupby(['CO_SEXO_PESSOA', 'CO_RACA_COR_PESSOA'])
    mean_age_by_sex_and_race = df_cad_modified['IDADE'].mean()
    median_age_by_sex_and_race = df_cad_modified['IDADE'].median()
    std_age_by_sex_and_race = df_cad_modified['IDADE'].std()
    return {"media": mean_age_by_sex_and_race,
            "mediana": median_age_by_sex_and_race,
            "desvio_padrao": std_age_by_sex_and_race}


def get_informal_and_formal_employment_rates(df_cad: pd.DataFrame):
    df_cad_modified = add_age_and_group_columns(df_cad)
    df_cad_modified = df_cad_modified[(df_cad_modified['IDADE'] >= 18) &
                                      (df_cad_modified['IDADE'] <= 65)].copy()
    df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'], errors='coerce')
    df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] = pd.to_numeric(
        df_cad_modified['VL_REMUNER_EMPREGO_MEMB'], errors='coerce')

    total_working_age_population = len(df_cad_modified)
    if total_working_age_population == 0:
        print("O total de pessoas em idade ativa vale 0!")
        return None

    total_informal_workers = len(df_cad_modified[
        (df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'] == 1) &
        (df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] == 0)])
    total_formal_workers = len(df_cad_modified[
        (df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'] == 1) &
        (df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] > 0)])
    total_workers = total_informal_workers + total_formal_workers

    informal_workers_rate = (total_informal_workers / total_working_age_population) * 100.0
    formal_workers_rate = (total_formal_workers / total_working_age_population) * 100.0

    if total_workers == 0:
        informal_occupied_workers_rate = 0.0
        formal_occupied_workers_rate = 0.0
    else:
        informal_occupied_workers_rate = (total_informal_workers / total_workers) * 100.0
        formal_occupied_workers_rate = (total_formal_workers / total_workers) * 100.0

    return {"taxa_informal_pia": informal_workers_rate,
            "taxa_formal_pia": formal_workers_rate,
            "taxa_informal_ocupados": informal_occupied_workers_rate,
            "taxa_formal_ocupados": formal_occupied_workers_rate}


def classify_level_of_education(row):
    course_attended = row['CO_CURSO_FREQ_PESSOA_MEMB']
    course_attending = row['CO_CURSO_FREQUENTA_MEMB']
    completed = row['CO_CONCLUIU_FREQUENTOU_MEMB']

    if pd.isna(course_attended) and pd.isna(course_attending) and pd.isna(completed):
        return np.nan

    course_attended = None if pd.isna(course_attended) else int(row['CO_CURSO_FREQ_PESSOA_MEMB'])
    course_attending = None if pd.isna(course_attending) else int(row['CO_CURSO_FREQUENTA_MEMB'])
    completed = None if pd.isna(completed) else int(row['CO_CONCLUIU_FREQUENTOU_MEMB'])

    if (course_attended is not None) and (completed is None):
        if course_attended not in [13, 14]:
            return np.nan
        else:
            return 5

    if course_attended == 13 and completed == 2:
        return 6

    if (course_attended in [8, 9, 12] and completed == 1) or (course_attending in [13, 14]):
        return 5

    if (course_attended in [8, 9, 12] and completed == 2):
        return 4

    if (course_attended in [5, 6, 7, 11] and completed == 1) or (course_attending in [7, 8, 11]):
        return 3

    if ((course_attended == 4 and completed == 1)
        or (course_attended in [4, 5, 6, 7, 10, 11] and completed == 2)
        or (course_attending in [1, 2, 3, 4, 5, 6, 9, 10])):
        return 2

    if course_attended == 15 or course_attending == 12:
        return 1

    return 0


def add_level_of_education_column(df_cad: pd.DataFrame):
    df_cad_modified = df_cad.copy()
    df_cad_modified['CO_CURSO_FREQUENTA_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_CURSO_FREQUENTA_MEMB'], errors='coerce')
    df_cad_modified['CO_CURSO_FREQ_PESSOA_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_CURSO_FREQ_PESSOA_MEMB'], errors='coerce')
    df_cad_modified['CO_CONCLUIU_FREQUENTOU_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_CONCLUIU_FREQUENTOU_MEMB'], errors='coerce')
    df_cad_modified['GRAU_INSTRUCAO'] = df_cad_modified.apply(
        classify_level_of_education, axis=1)
    return df_cad_modified


def calculate_mean_income_by_education_level(df_cad: pd.DataFrame):
    df_cad_modified = add_level_of_education_column(df_cad)
    df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] = pd.to_numeric(
        df_cad_modified['VL_REMUNER_EMPREGO_MEMB'], errors='coerce')
    df_cad_modified = df_cad_modified.groupby('GRAU_INSTRUCAO')
    return df_cad_modified['VL_REMUNER_EMPREGO_MEMB'].mean()


def get_proportion_of_paid_employment_by_age_group(df_cad: pd.DataFrame):
    df_cad_modified = add_age_and_group_columns(df_cad)
    df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] = pd.to_numeric(
        df_cad_modified['VL_REMUNER_EMPREGO_MEMB'], errors='coerce')
    df_cad_modified['TEM_REMUNER_EMPREGO_MEMB'] = df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] > 0
    return df_cad_modified.groupby('FAIXA_ETARIA')['TEM_REMUNER_EMPREGO_MEMB'].mean()


def add_per_capita_income_column(df_cad: pd.DataFrame):
    df_cad_modified = df_cad.copy()
    income_columns = ["VL_REMUNER_EMPREGO_MEMB", "VL_RENDA_BRUTA_12_MESES_MEMB",
                      "VL_RENDA_DOACAO_MEMB", "VL_RENDA_APOSENT_MEMB",
                      "VL_RENDA_SEGURO_DESEMP_MEMB",
                      "VL_RENDA_PENSAO_ALIMEN_MEMB", "VL_RENDA_OUTRAS_MEMB"]
    for income_column in income_columns:
        df_cad_modified[income_column] = pd.to_numeric(
            df_cad_modified[income_column], errors='coerce')
    df_cad_modified['VL_RENDA_TOTAL_MEMB'] = df_cad_modified[income_columns].sum(axis=1)
    total_family_income = df_cad_modified.groupby('CO_FAMILIAR_FAM')['VL_RENDA_TOTAL_MEMB'].transform('sum')
    family_size = df_cad_modified.groupby('CO_FAMILIAR_FAM')['CO_FAMILIAR_FAM'].transform('size')
    df_cad_modified['VL_RENDA_PER_CAPITA_FAMILIA'] = total_family_income / family_size
    return df_cad_modified


def calculate_pwd_percentage_by_per_capita_income_group(df_cad: pd.DataFrame):
    df_cad_modified = add_per_capita_income_column(df_cad)
    bins = [-np.inf, 109, 218, 477, np.inf]
    labels = ["1- Renda familiar per capita de até R$109,00",
              "2- Renda familiar per capita de R$109,00 até R$218,00",
              "3- Renda familiar per capita de R$218,00 até 1/2 (R$477,00) salário mínimo (s.m.)",
              "4- Renda familiar per capita acima de 1/2 (R$477,00) s.m."]
    df_cad_modified['FX_RFPC'] = pd.cut(
        df_cad_modified['VL_RENDA_PER_CAPITA_FAMILIA'],
        bins=bins, labels=labels, include_lowest=True)
    df_cad_modified['CO_DEFICIENCIA_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_DEFICIENCIA_MEMB'], errors='coerce')
    df_cad_modified['CO_DEFICIENCIA_MEMB'] = df_cad_modified['CO_DEFICIENCIA_MEMB'] == 1
    return df_cad_modified.groupby('FX_RFPC')['CO_DEFICIENCIA_MEMB'].mean()


def calculate_mean_and_median_income_difference_by_sex_and_race(df_cad: pd.DataFrame):
    df_cad_modified = df_cad.copy()
    df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] = pd.to_numeric(
        df_cad_modified['VL_REMUNER_EMPREGO_MEMB'], errors='coerce')
    df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'], errors='coerce')
    df_cad_modified = df_cad_modified[df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] > 0]
    groups = df_cad_modified.groupby(['CO_SEXO_PESSOA', 'CO_RACA_COR_PESSOA'])['VL_REMUNER_EMPREGO_MEMB']

    mean_income = groups.mean().unstack(level='CO_SEXO_PESSOA')
    mean_income['DIFERENCA_MEDIA_RENDA'] = mean_income[1] - mean_income[2]

    median_income = groups.median().unstack(level='CO_SEXO_PESSOA')
    median_income['DIFERENCA_MEDIANA_RENDA'] = median_income[1] - median_income[2]

    return {"media_renda": mean_income, "mediana_renda": median_income}


def calculate_informal_employment_percentage_rate_by_education_level(df_cad: pd.DataFrame):
    df_cad_modified = add_level_of_education_column(df_cad)
    df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'], errors='coerce')
    df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] = pd.to_numeric(
        df_cad_modified['VL_REMUNER_EMPREGO_MEMB'], errors='coerce')
    df_cad_modified = df_cad_modified[df_cad_modified['CO_TRABALHOU_SEMANA_MEMB'] == 1]

    education_groups = {1: "Sem instrução", 2: "Fundamental", 3: "Fundamental",
                        4: "Médio", 5: "Médio", 6: "Superior"}
    df_cad_modified['GRAU_INSTRUCAO'] = df_cad_modified['GRAU_INSTRUCAO'].map(education_groups)
    df_cad_modified = df_cad_modified.dropna(subset=['VL_REMUNER_EMPREGO_MEMB', 'GRAU_INSTRUCAO'])
    groups = df_cad_modified.groupby('GRAU_INSTRUCAO')

    rates = {}
    for level, group in groups:
        total_workers = len(group)
        if total_workers == 0:
            rates[level] = 0.0
            continue
        total_informal_workers = (group['VL_REMUNER_EMPREGO_MEMB'] == 0).sum()
        rates[level] = (total_informal_workers / total_workers) * 100.0
    return rates


def get_proportion_of_pwd_by_age_and_group_and_pwd_percentage_in_extreme_poverty(df_cad: pd.DataFrame):
    df_cad_modified = add_age_and_group_columns(df_cad)
    df_cad_modified = df_cad_modified.dropna(subset=['FAIXA_ETARIA'])
    df_cad_modified['CO_DEFICIENCIA_MEMB'] = pd.to_numeric(
        df_cad_modified['CO_DEFICIENCIA_MEMB'], errors='coerce')
    df_cad_modified['CO_DEFICIENCIA_MEMB'] = df_cad_modified['CO_DEFICIENCIA_MEMB'] == 1
    proportion = df_cad_modified.groupby('FAIXA_ETARIA')['CO_DEFICIENCIA_MEMB'].mean()

    df_cad_modified = add_per_capita_income_column(df_cad_modified)
    df_cad_modified = df_cad_modified[df_cad_modified['CO_DEFICIENCIA_MEMB'] == True]
    total_pwd = len(df_cad_modified)

    if total_pwd > 0:
        pwd_extreme_poverty = (df_cad_modified['VL_RENDA_PER_CAPITA_FAMILIA'] <= 89).sum()
        pwd_percentage_in_extreme_poverty = (pwd_extreme_poverty / total_pwd) * 100.0
    else:
        pwd_percentage_in_extreme_poverty = 0.0

    return {"proporcao_pcd_por_faixa_etaria": proportion,
            "percentagem_pcd_na_extrema_pobreza": pwd_percentage_in_extreme_poverty}


def calculate_employment_rate_by_female_heads_with_young_children(df_cad: pd.DataFrame):
    df_cad_modified = add_age_and_group_columns(df_cad)
    df_cad_modified['CO_SEXO_PESSOA'] = pd.to_numeric(
        df_cad_modified['CO_SEXO_PESSOA'], errors='coerce')
    df_cad_modified['CO_PARENTESCO_RF_PESSOA'] = pd.to_numeric(
        df_cad_modified['CO_PARENTESCO_RF_PESSOA'], errors='coerce')
    df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] = pd.to_numeric(
        df_cad_modified['VL_REMUNER_EMPREGO_MEMB'], errors='coerce')

    df_cad_modified['E_MULHER_RESPONSAVEL'] = (
        (df_cad_modified['CO_SEXO_PESSOA'] == 2) &
        (df_cad_modified['CO_PARENTESCO_RF_PESSOA'] == 1))

    df_cad_modified['E_CRIANCA_0_A_6_ANOS'] = (
        (df_cad_modified['IDADE'] >= 0) & (df_cad_modified['IDADE'] <= 6))

    has_young_children = df_cad_modified.groupby('CO_FAMILIAR_FAM')['E_CRIANCA_0_A_6_ANOS'].transform('any')
    df_cad_modified['TEM_CRIANCA_0_A_6_ANOS'] = has_young_children
    df_cad_modified = df_cad_modified[df_cad_modified['E_MULHER_RESPONSAVEL'] == True]
    df_cad_modified['TEM_TRABALHO_REMUNERADO'] = df_cad_modified['VL_REMUNER_EMPREGO_MEMB'] > 0
    return df_cad_modified.groupby('TEM_CRIANCA_0_A_6_ANOS')['TEM_TRABALHO_REMUNERADO'].mean()


# =============================================================================
# ETAPA 3: INTEGRAÇÃO DO ARQUIVO DE DIVULGAÇÃO DO ENSINO MÉDIO (IDEB)
# =============================================================================

def load_ideb_data(file_path: str = "divulgacao_ensino_medio_municipios_2025.xlsx") -> pd.DataFrame:
    if not os.path.exists(file_path):
        print(f"Arquivo '{file_path}' não encontrado!")
        return None
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    print(f"Abas encontradas no arquivo IDEB: {sheet_names}")
    target_sheet = None
    for name in sheet_names:
        up = name.upper()
        if "IDEB" in up and ("MÉDIO" in up or "MEDIO" in up):
            target_sheet = name
            break
    if target_sheet is None:
        target_sheet = sheet_names[0]
    print(f"Usando aba: '{target_sheet}'")

    raw = pd.read_excel(file_path, sheet_name=target_sheet, header=None, dtype=str)

    def _norm(s):
        if pd.isna(s):
            return ""
        return re.sub(r"\s+", "", str(s)).lower()

    marc_tec = {"sg_uf", "no_municipio", "rede"}
    marc_hum = {"siglada uf".replace(" ", ""), "nomedomunicipio", "rede"}

    header_row = None
    header_format = None
    for i in range(min(30, len(raw))):
        valores = set(_norm(v) for v in raw.iloc[i].tolist() if pd.notna(v))
        if marc_tec.issubset(valores):
            header_row = i; header_format = "tecnico"; break
        if marc_hum.issubset(valores):
            header_row = i; header_format = "humano"; break

    if header_row is None:
        header_row = 8; header_format = "tecnico"
        print(f"[AVISO] Linha de cabeçalho não detectada; usando fallback header={header_row}")
    else:
        print(f"Linha de cabeçalho detectada no índice {header_row} "
              f"(linha {header_row + 1} do Excel) — formato: {header_format}")

    df_ideb = pd.read_excel(file_path, sheet_name=target_sheet, header=header_row)
    df_ideb.columns = [re.sub(r"\s+", " ", str(c)).strip() for c in df_ideb.columns]
    df_ideb = df_ideb.loc[:, ~df_ideb.columns.str.startswith("Unnamed")]

    rename_map = {}
    for col in df_ideb.columns:
        c_norm = re.sub(r"\s+", "", col).lower()
        if c_norm in ("sg_uf", "siglada uf".replace(" ", "")):
            rename_map[col] = "SG_UF"
        elif c_norm in ("co_municipio", "codigodomunicipio"):
            rename_map[col] = "CO_MUNICIPIO"
        elif c_norm in ("no_municipio", "nomedomunicipio"):
            rename_map[col] = "NO_MUNICIPIO"
        elif c_norm == "rede":
            rename_map[col] = "REDE"
        elif c_norm.startswith("vl_observado_"):
            ano = c_norm.replace("vl_observado_", "")
            if ano in ("2017", "2019", "2021", "2023", "2025"):
                rename_map[col] = f"IDEB_{ano}"
        elif c_norm.startswith("ideb"):
            m = re.search(r"(\d{4})", c_norm)
            if m:
                ano = m.group(1)
                if ano == "20211": ano = "2021"
                if ano in ("2017", "2019", "2021", "2023", "2025"):
                    rename_map[col] = f"IDEB_{ano}"

    df_ideb = df_ideb.rename(columns=rename_map)
    obrigatorias = ["SG_UF", "CO_MUNICIPIO", "NO_MUNICIPIO", "REDE", "IDEB_2017", "IDEB_2025"]
    faltantes = [c for c in obrigatorias if c not in df_ideb.columns]
    if faltantes:
        print(f"[ERRO] Colunas obrigatórias ausentes: {faltantes}")
        print(f"Colunas disponíveis: {list(df_ideb.columns)}")
        return None

    df_ideb = df_ideb[df_ideb["NO_MUNICIPIO"].notna()].copy()
    df_ideb["SG_UF"] = df_ideb["SG_UF"].astype(str).str.strip().str.upper()
    df_ideb["NO_MUNICIPIO"] = df_ideb["NO_MUNICIPIO"].astype(str).str.strip()
    df_ideb["REDE"] = df_ideb["REDE"].astype(str).str.strip()
    for col in ["IDEB_2017", "IDEB_2019", "IDEB_2021", "IDEB_2023", "IDEB_2025"]:
        if col in df_ideb.columns:
            df_ideb[col] = pd.to_numeric(df_ideb[col], errors="coerce")
    return df_ideb


def ideb_mean_by_uf_and_public_network(df_ideb: pd.DataFrame) -> pd.DataFrame:
    if df_ideb is None or df_ideb.empty:
        print("DataFrame do IDEB vazio ou inválido!")
        return pd.DataFrame()
    df_publico = df_ideb[df_ideb["REDE"].str.lower() == "pública"].copy()
    if df_publico.empty:
        print("Nenhum registro encontrado para a rede 'Pública'.")
        return pd.DataFrame()
    agrupado = df_publico.groupby("SG_UF").agg(
        media_ideb_2025=("IDEB_2025", "mean"),
        media_ideb_2017=("IDEB_2017", "mean"),
        n_municipios=("NO_MUNICIPIO", "nunique")).reset_index()
    agrupado["variacao_percentual_2017_2025"] = (
        (agrupado["media_ideb_2025"] - agrupado["media_ideb_2017"])
        / agrupado["media_ideb_2017"] * 100.0)
    agrupado = agrupado.sort_values("media_ideb_2025", ascending=False).reset_index(drop=True)
    return agrupado


def top10_municipios_ideb_2025_e_evolucao_alta_floresta(df_ideb: pd.DataFrame) -> dict:
    if df_ideb is None or df_ideb.empty:
        print("DataFrame do IDEB vazio ou inválido!")
        return {}
    df_publico = df_ideb[df_ideb["REDE"].str.lower() == "pública"].copy()
    if df_publico.empty:
        print("Nenhum registro encontrado para a rede 'Pública'.")
        return {}
    por_municipio = df_publico.groupby(
        ["SG_UF", "CO_MUNICIPIO", "NO_MUNICIPIO"], as_index=False
    ).agg(ideb_2025=("IDEB_2025", "mean"), ideb_2017=("IDEB_2017", "mean"))
    por_municipio["variacao_percentual_2017_2025"] = (
        (por_municipio["ideb_2025"] - por_municipio["ideb_2017"])
        / por_municipio["ideb_2017"] * 100.0)
    top10 = por_municipio.sort_values("ideb_2025", ascending=False).head(10).reset_index(drop=True)
    mask_alta_floresta = por_municipio["NO_MUNICIPIO"].str.contains(
        "Alta Floresta", case=False, na=False)
    df_alta_floresta = por_municipio[mask_alta_floresta]
    df_demais = por_municipio[~mask_alta_floresta]
    comparacao = {
        "Alta Floresta": {
            "n_municipios": len(df_alta_floresta),
            "variacao_media_percentual": df_alta_floresta["variacao_percentual_2017_2025"].mean(),
            "ideb_2025_medio": df_alta_floresta["ideb_2025"].mean(),
            "ideb_2017_medio": df_alta_floresta["ideb_2017"].mean()},
        "Demais municípios": {
            "n_municipios": len(df_demais),
            "variacao_media_percentual": df_demais["variacao_percentual_2017_2025"].mean(),
            "ideb_2025_medio": df_demais["ideb_2025"].mean(),
            "ideb_2017_medio": df_demais["ideb_2017"].mean()}}
    return {"top10_municipios_ideb_2025": top10,
            "comparacao_alta_floresta_vs_demais": comparacao}


# =============================================================================
# ETAPA 4: VISUALIZAÇÃO GRÁFICA COM MATPLOTLIB / SEABORN
# =============================================================================

FIGURAS_DIR = "figuras"


def _configurar_estilo():
    sns.set_theme(style="whitegrid", palette="viridis")
    plt.rcParams.update({
        "figure.figsize": (12, 6),
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.autolayout": True,
        "savefig.dpi": 150})
    os.makedirs(FIGURAS_DIR, exist_ok=True)


def _salvar(fig, nome_arquivo: str):
    caminho = os.path.join(FIGURAS_DIR, nome_arquivo)
    fig.savefig(caminho, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] Figura salva em: {caminho}")


def plot_media_idade_por_sexo_e_raca(stats: dict):
    media = stats["media"]
    df_plot = media.reset_index()
    df_plot.columns = ["SEXO", "RACA", "MEDIA_IDADE"]
    mapa_sexo = {1: "Masculino", 2: "Feminino"}
    mapa_raca = {1: "Branca", 2: "Preta", 3: "Parda", 4: "Amarela", 5: "Indígena"}
    df_plot["SEXO_LABEL"] = df_plot["SEXO"].map(mapa_sexo).fillna("Outro")
    df_plot["RACA_LABEL"] = df_plot["RACA"].map(mapa_raca).fillna("Outra")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_plot, x="RACA_LABEL", y="MEDIA_IDADE",
                hue="SEXO_LABEL", ax=ax, palette="Set2")
    ax.set_title("Média de Idade por Cor/Raça e Sexo/Gênero — CadÚnico 2018")
    ax.set_xlabel("Cor/Raça"); ax.set_ylabel("Idade média (anos)")
    ax.legend(title="Sexo/Gênero", loc="upper right")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", fontsize=8, padding=2)
    _salvar(fig, "etapa4_01_media_idade_por_sexo_raca.png")


def plot_mediana_idade_por_sexo_e_raca(stats: dict):
    """ETAPA 1.1 (complementar) — Gráfico da MEDIANA de idade por
    sexo/gênero e cor/raça."""
    mediana = stats["mediana"]
    df_plot = mediana.reset_index()
    df_plot.columns = ["SEXO", "RACA", "MEDIANA_IDADE"]
    mapa_sexo = {1: "Masculino", 2: "Feminino"}
    mapa_raca = {1: "Branca", 2: "Preta", 3: "Parda", 4: "Amarela", 5: "Indígena"}
    df_plot["SEXO_LABEL"] = df_plot["SEXO"].map(mapa_sexo).fillna("Outro")
    df_plot["RACA_LABEL"] = df_plot["RACA"].map(mapa_raca).fillna("Outra")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_plot, x="RACA_LABEL", y="MEDIANA_IDADE",
                hue="SEXO_LABEL", ax=ax, palette="Set2")
    ax.set_title("Mediana de Idade por Cor/Raça e Sexo/Gênero — CadÚnico 2018")
    ax.set_xlabel("Cor/Raça"); ax.set_ylabel("Idade mediana (anos)")
    ax.legend(title="Sexo/Gênero", loc="upper right")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", fontsize=8, padding=2)
    _salvar(fig, "etapa4_01b_mediana_idade_por_sexo_raca.png")


def plot_desvio_padrao_idade_por_sexo_e_raca(stats: dict):
    """ETAPA 1.1 (complementar) — Gráfico do DESVIO PADRÃO de idade por
    sexo/gênero e cor/raça."""
    desvio = stats["desvio_padrao"]
    df_plot = desvio.reset_index()
    df_plot.columns = ["SEXO", "RACA", "DESVIO_PADRAO_IDADE"]
    mapa_sexo = {1: "Masculino", 2: "Feminino"}
    mapa_raca = {1: "Branca", 2: "Preta", 3: "Parda", 4: "Amarela", 5: "Indígena"}
    df_plot["SEXO_LABEL"] = df_plot["SEXO"].map(mapa_sexo).fillna("Outro")
    df_plot["RACA_LABEL"] = df_plot["RACA"].map(mapa_raca).fillna("Outra")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_plot, x="RACA_LABEL", y="DESVIO_PADRAO_IDADE",
                hue="SEXO_LABEL", ax=ax, palette="Set2")
    ax.set_title("Desvio Padrão da Idade por Cor/Raça e Sexo/Gênero — CadÚnico 2018")
    ax.set_xlabel("Cor/Raça"); ax.set_ylabel("Desvio padrão da idade (anos)")
    ax.legend(title="Sexo/Gênero", loc="upper right")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", fontsize=8, padding=2)
    _salvar(fig, "etapa4_01c_desvio_padrao_idade_por_sexo_raca.png")


def plot_taxas_informal_formal_pia(rates: dict):
    categorias = ["Informal (PIA)", "Formal (PIA)",
                  "Informal (ocupados)", "Formal (ocupados)"]
    valores = [rates["taxa_informal_pia"], rates["taxa_formal_pia"],
               rates["taxa_informal_ocupados"], rates["taxa_formal_ocupados"]]
    cores = ["#E76F51", "#2A9D8F", "#E76F51", "#2A9D8F"]
    fig, ax = plt.subplots(figsize=(10, 6))
    barras = ax.bar(categorias, valores, color=cores)
    ax.set_title("Taxas de Trabalho Informal e Formal — PIA (18-65 anos)")
    ax.set_ylabel("Taxa (%)"); ax.set_xlabel("")
    ax.set_ylim(0, max(valores) * 1.2 if max(valores) > 0 else 1)
    for b, v in zip(barras, valores):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.5, f"{v:.2f}%",
                ha="center", fontsize=10)
    _salvar(fig, "etapa4_02_taxas_informal_formal.png")


def plot_renda_media_por_escolaridade(mean_income: pd.Series):
    mapa_grau = {0: "Outros", 1: "Sem instrução", 2: "Fundamental incompleto",
                 3: "Fundamental completo", 4: "Médio incompleto",
                 5: "Médio completo", 6: "Superior incompleto"}
    df_plot = mean_income.reset_index()
    df_plot.columns = ["GRAU", "RENDA_MEDIA"]
    df_plot["GRAU_LABEL"] = df_plot["GRAU"].map(mapa_grau).fillna("Desconhecido")
    df_plot = df_plot.dropna(subset=["RENDA_MEDIA"]).sort_values("RENDA_MEDIA")
    fig, ax = plt.subplots(figsize=(11, 6))
    sns.barplot(data=df_plot, x="RENDA_MEDIA", y="GRAU_LABEL", ax=ax, palette="rocket")
    ax.set_title("Renda Média do Trabalho Individual por Nível de Escolaridade")
    ax.set_xlabel("Renda média (R$)"); ax.set_ylabel("Nível de instrução")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f", fontsize=9, padding=3)
    _salvar(fig, "etapa4_03_renda_por_escolaridade.png")


def plot_proporcao_trabalho_remunerado_por_faixa(proportions: pd.Series):
    df_plot = proportions.reset_index()
    df_plot.columns = ["FAIXA", "PROPORCAO"]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_plot, x="FAIXA", y="PROPORCAO", ax=ax, palette="crest")
    ax.set_title("Proporção de Pessoas com Trabalho Remunerado por Faixa Etária")
    ax.set_ylabel("Proporção (0 a 1)"); ax.set_xlabel("Faixa etária")
    ax.set_ylim(0, max(df_plot["PROPORCAO"]) * 1.2 if len(df_plot) else 1)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.3f", fontsize=10, padding=3)
    _salvar(fig, "etapa4_04_trabalho_por_faixa_etaria.png")


def plot_pcd_por_faixa_renda(pwd_percentages: pd.Series):
    df_plot = pwd_percentages.reset_index()
    df_plot.columns = ["FAIXA_RENDA", "PCT_PCD"]
    df_plot["FAIXA_RENDA"] = df_plot["FAIXA_RENDA"].astype(str)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df_plot, x="FAIXA_RENDA", y="PCT_PCD", ax=ax, palette="flare")
    ax.set_title("Percentual de Pessoas com Deficiência por Faixa de Renda Familiar per capita")
    ax.set_ylabel("Percentual de PCD (%)"); ax.set_xlabel("Faixa de renda familiar per capita")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f%%", fontsize=9, padding=3)
    plt.setp(ax.get_xticklabels(), rotation=15, ha="right")
    _salvar(fig, "etapa4_05_pcd_por_faixa_renda.png")


def plot_diferenca_renda_por_sexo_e_raca(stats_income: dict):
    mapa_sexo = {1: "Masculino", 2: "Feminino"}
    mapa_raca = {1: "Branca", 2: "Preta", 3: "Parda", 4: "Amarela", 5: "Indígena"}
    media = stats_income["media_renda"].copy()
    mediana = stats_income["mediana_renda"].copy()

    def _preparar(df):
        df = df.reset_index()
        col_raca = df.columns[0]
        df = df.rename(columns={col_raca: "RACA"})
        df["RACA_LABEL"] = df["RACA"].map(mapa_raca).fillna("Outra")
        return df

    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharex=True)
    for ax, df, titulo in zip(
        axes,
        [_preparar(media), _preparar(mediana)],
        ["Média da renda individual", "Mediana da renda individual"]):
        cols_sexo = [c for c in df.columns if c in (1, 2, "1", "2")]
        df_melt = df.melt(id_vars=["RACA_LABEL"], value_vars=cols_sexo,
                          var_name="SEXO", value_name="RENDA")
        df_melt["SEXO_LABEL"] = pd.to_numeric(
            df_melt["SEXO"], errors="coerce").map(mapa_sexo)
        sns.barplot(data=df_melt, x="RACA_LABEL", y="RENDA",
                    hue="SEXO_LABEL", ax=ax, palette="Set1")
        ax.set_title(titulo + " — por Cor/Raça e Sexo/Gênero")
        ax.set_xlabel("Cor/Raça"); ax.set_ylabel("Renda (R$)")
        ax.legend(title="Sexo/Gênero")
    _salvar(fig, "etapa4_06_renda_por_sexo_raca.png")


def plot_taxa_informal_por_escolaridade(rates: dict):
    df_plot = pd.DataFrame(list(rates.items()),
                           columns=["ESCOLARIDADE", "TAXA_INFORMAL"]
                           ).sort_values("TAXA_INFORMAL")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_plot, x="TAXA_INFORMAL", y="ESCOLARIDADE", ax=ax, palette="mako")
    ax.set_title("Taxa de Trabalho Informal por Nível de Escolaridade")
    ax.set_xlabel("Taxa de informalidade (%)"); ax.set_ylabel("Nível de escolaridade")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f%%", fontsize=10, padding=3)
    _salvar(fig, "etapa4_07_informal_por_escolaridade.png")


def plot_pcd_por_faixa_etaria_e_extrema_pobreza(stats_pwd: dict):
    proporcao = stats_pwd["proporcao_pcd_por_faixa_etaria"]
    pct_extrema = stats_pwd["percentagem_pcd_na_extrema_pobreza"]
    df_plot = proporcao.reset_index()
    df_plot.columns = ["FAIXA", "PROPORCAO"]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df_plot, x="FAIXA", y="PROPORCAO", ax=ax, palette="viridis")
    ax.set_title(f"Proporção de Pessoas com Deficiência por Faixa Etária\n"
                 f"({pct_extrema:.2f}% das PCDs estão em extrema pobreza)")
    ax.set_ylabel("Proporção de PCD"); ax.set_xlabel("Faixa etária")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.4f", fontsize=10, padding=3)
    _salvar(fig, "etapa4_08_pcd_por_faixa_etaria.png")


def plot_ocupacao_mulheres_com_e_sem_criancas(employment_rates: pd.Series):
    df_plot = employment_rates.reset_index()
    df_plot.columns = ["TEM_CRIANCA", "TAXA_OCUPACAO"]
    df_plot["GRUPO"] = df_plot["TEM_CRIANCA"].map({
        True: "Com crianças 0-6 anos",
        False: "Sem crianças 0-6 anos"})
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.barplot(data=df_plot, x="GRUPO", y="TAXA_OCUPACAO", ax=ax, palette="coolwarm")
    ax.set_title("Taxa de Ocupação de Mulheres Responsáveis pelo Domicílio\n"
                 "(com e sem crianças de 0 a 6 anos)")
    ax.set_ylabel("Taxa de ocupação (trabalho remunerado)"); ax.set_xlabel("")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.4f", fontsize=11, padding=3)
    _salvar(fig, "etapa4_09_ocupacao_mulheres.png")


def plot_ideb_por_uf(pergunta1: pd.DataFrame):
    if pergunta1 is None or pergunta1.empty:
        print("[AVISO] DataFrame da Pergunta 1 vazio; pulando gráfico.")
        return
    df_plot = pergunta1.sort_values("media_ideb_2025", ascending=False)
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.barplot(data=df_plot, x="SG_UF", y="media_ideb_2025", ax=ax, palette="viridis")
    ax.set_title("IDEB Médio 2025 por UF — Rede Pública (Ensino Médio)")
    ax.set_xlabel("UF"); ax.set_ylabel("IDEB médio 2025")
    ax.axhline(df_plot["media_ideb_2025"].mean(), color="red",
               linestyle="--", linewidth=1,
               label=f"Média nacional = {df_plot['media_ideb_2025'].mean():.2f}")
    ax.legend()
    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f", fontsize=8, padding=2)
    plt.setp(ax.get_xticklabels(), rotation=0)
    _salvar(fig, "etapa4_10_ideb_por_uf.png")


def plot_top10_municipios_ideb(top10: pd.DataFrame):
    if top10 is None or top10.empty:
        print("[AVISO] DataFrame do Top 10 vazio; pulando gráfico.")
        return
    df_plot = top10.copy()
    df_plot["LABEL"] = df_plot["NO_MUNICIPIO"] + " (" + df_plot["SG_UF"] + ")"
    df_plot = df_plot.sort_values("ideb_2025", ascending=True)
    fig, ax = plt.subplots(figsize=(11, 7))
    sns.barplot(data=df_plot, x="ideb_2025", y="LABEL", ax=ax, palette="magma")
    ax.set_title("Top 10 Municípios com Maior IDEB 2025 — Rede Pública")
    ax.set_xlabel("IDEB 2025"); ax.set_ylabel("Município (UF)")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", fontsize=10, padding=3)
    _salvar(fig, "etapa4_11_top10_municipios_ideb.png")


def run_etapa4(df_cad: pd.DataFrame, df_ideb: pd.DataFrame | None = None):
    print("\n" + "=" * 70)
    print("ETAPA 4: VISUALIZAÇÃO GRÁFICA DOS RESULTADOS")
    print("=" * 70)

    _configurar_estilo()

    # ---- Etapa 1 ----
    print("\n[1/13] Média de idade por sexo/gênero e cor/raça...")
    stats_idade = calculate_age_distribution_by_sex_and_race(df_cad)
    plot_media_idade_por_sexo_e_raca(stats_idade)

    print("\n[2/13] Mediana de idade por sexo/gênero e cor/raça...")
    plot_mediana_idade_por_sexo_e_raca(stats_idade)

    print("\n[3/13] Desvio padrão da idade por sexo/gênero e cor/raça...")
    plot_desvio_padrao_idade_por_sexo_e_raca(stats_idade)

    print("\n[4/13] Taxas de trabalho informal e formal...")
    taxas = get_informal_and_formal_employment_rates(df_cad)
    if taxas:
        plot_taxas_informal_formal_pia(taxas)

    print("\n[5/13] Renda média por nível de escolaridade...")
    renda_escol = calculate_mean_income_by_education_level(df_cad)
    plot_renda_media_por_escolaridade(renda_escol)

    # ---- Etapa 2 ----
    print("\n[6/13] Trabalho remunerado por faixa etária...")
    prop_trabalho = get_proportion_of_paid_employment_by_age_group(df_cad)
    plot_proporcao_trabalho_remunerado_por_faixa(prop_trabalho)

    print("\n[7/13] PCD por faixa de renda familiar per capita...")
    pcd_renda = calculate_pwd_percentage_by_per_capita_income_group(df_cad)
    plot_pcd_por_faixa_renda(pcd_renda)

    # ---- Perguntas complementares ----
    print("\n[8/13] Diferença de renda por sexo/gênero e cor/raça...")
    stats_renda = calculate_mean_and_median_income_difference_by_sex_and_race(df_cad)
    plot_diferenca_renda_por_sexo_e_raca(stats_renda)

    print("\n[9/13] Taxa de informalidade por nível de escolaridade...")
    taxas_informal = calculate_informal_employment_percentage_rate_by_education_level(df_cad)
    plot_taxa_informal_por_escolaridade(taxas_informal)

    print("\n[10/13] PCD por faixa etária e extrema pobreza...")
    stats_pcd = get_proportion_of_pwd_by_age_and_group_and_pwd_percentage_in_extreme_poverty(df_cad)
    plot_pcd_por_faixa_etaria_e_extrema_pobreza(stats_pcd)

    print("\n[11/13] Ocupação de mulheres responsáveis por domicílio...")
    ocupacao_mulheres = calculate_employment_rate_by_female_heads_with_young_children(df_cad)
    plot_ocupacao_mulheres_com_e_sem_criancas(ocupacao_mulheres)

    # ---- Etapa 3 (gráficos do IDEB) ----
    if df_ideb is not None and not df_ideb.empty:
        print("\n[12/13] IDEB médio 2025 por UF (rede Pública)...")
        pergunta1 = ideb_mean_by_uf_and_public_network(df_ideb)
        plot_ideb_por_uf(pergunta1)

        print("\n[13/13] Top 10 municípios com maior IDEB 2025...")
        pergunta2 = top10_municipios_ideb_2025_e_evolucao_alta_floresta(df_ideb)
        if pergunta2:
            plot_top10_municipios_ideb(pergunta2["top10_municipios_ideb_2025"])

    print(f"\n[FIM] Todas as figuras foram salvas em '{FIGURAS_DIR}/'.")


# =============================================================================
# RESPOSTAS EXPLÍCITAS ÀS 4 PERGUNTAS
# =============================================================================

def _formatar_moeda(valor: float) -> str:
    if pd.isna(valor):
        return "N/D"
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def responder_pergunta_1(df_cad: pd.DataFrame) -> None:
    print("\n" + "=" * 78)
    print("PERGUNTA 1 — Desigualdade de Renda e Interseccionalidade")
    print("(Renda x Gênero x Cor/Raça)")
    print("=" * 78)
    print("Pergunta: Qual é a diferença na média e na mediana da renda "
          "individual de trabalho\nentre homens e mulheres quando agrupados "
          "por cor/raça (branca, preta, parda,\namarela e indígena)?\n")

    mapa_sexo = {1: "Masculino", 2: "Feminino"}
    mapa_raca = {1: "Branca", 2: "Preta", 3: "Parda", 4: "Amarela", 5: "Indígena"}

    stats = calculate_mean_and_median_income_difference_by_sex_and_race(df_cad)
    media = stats["media_renda"].copy()
    mediana = stats["mediana_renda"].copy()
    media = media.rename(columns=mapa_sexo)
    mediana = mediana.rename(columns=mapa_sexo)
    media.index = media.index.map(lambda c: mapa_raca.get(c, f"Código {c}"))
    mediana.index = mediana.index.map(lambda c: mapa_raca.get(c, f"Código {c}"))
    media.index.name = "Cor/Raça"
    mediana.index.name = "Cor/Raça"

    print(">>> MÉDIA da renda individual de trabalho (R$):")
    print(media.round(2).to_string())
    print()
    print(">>> MEDIANA da renda individual de trabalho (R$):")
    print(mediana.round(2).to_string())
    print()
    print(">>> Diferença (Homens − Mulheres):")
    for raca in media.index:
        dif_media = media.loc[raca].get("DIFERENCA_MEDIA_RENDA", np.nan)
        dif_mediana = mediana.loc[raca].get("DIFERENCA_MEDIANA_RENDA", np.nan)
        m_h = media.loc[raca].get("Masculino", np.nan)
        m_m = media.loc[raca].get("Feminino", np.nan)
        md_h = mediana.loc[raca].get("Masculino", np.nan)
        md_m = mediana.loc[raca].get("Feminino", np.nan)
        print(f"  • Cor/Raça: {raca}\n"
              f"      Média   → Homens: {_formatar_moeda(m_h)} | "
              f"Mulheres: {_formatar_moeda(m_m)} | "
              f"Diferença: {_formatar_moeda(dif_media)}\n"
              f"      Mediana → Homens: {_formatar_moeda(md_h)} | "
              f"Mulheres: {_formatar_moeda(md_m)} | "
              f"Diferença: {_formatar_moeda(dif_mediana)}")
    print()


def responder_pergunta_2(df_cad: pd.DataFrame) -> None:
    print("\n" + "=" * 78)
    print("PERGUNTA 2 — Relação entre Nível de Escolaridade e Trabalho Informal")
    print("=" * 78)
    print("Pergunta: Qual é a taxa percentual de trabalhadores na condição de "
          "trabalho informal\nem cada um dos níveis de escolaridade "
          "(sem instrução, fundamental, médio e superior)?\n")

    taxas = calculate_informal_employment_percentage_rate_by_education_level(df_cad)
    ordem = ["Sem instrução", "Fundamental", "Médio", "Superior"]
    print(">>> Taxa de trabalho informal por nível de escolaridade:")
    for nivel in ordem:
        taxa = taxas.get(nivel, np.nan)
        if pd.isna(taxa):
            print(f"  • {nivel:<14}: N/D")
        else:
            print(f"  • {nivel:<14}: {taxa:6.2f}%")
    extras = {k: v for k, v in taxas.items() if k not in ordem}
    if extras:
        print("\n  (Níveis adicionais encontrados:)")
        for nivel, taxa in extras.items():
            print(f"  • {nivel:<14}: {taxa:6.2f}%")
    print()


def responder_pergunta_3(df_cad: pd.DataFrame) -> None:
    print("\n" + "=" * 78)
    print("PERGUNTA 3 — Perfil de Vulnerabilidade e Acessibilidade de PCD")
    print("=" * 78)
    print("Pergunta: Qual é a proporção de Pessoas com Deficiência (PCD) "
          "registradas por faixa\netária (Crianças/Adolescentes: 0-17, "
          "Jovens: 18-29, Adultos: 30-59, Idosos: 60+)\ne qual a percentagem "
          "destas pessoas que vivem em famílias classificadas na extrema\n"
          "pobreza (renda per capita familiar de até R$ 89,00 em 2018)?\n")

    stats = get_proportion_of_pwd_by_age_and_group_and_pwd_percentage_in_extreme_poverty(df_cad)
    proporcao = stats["proporcao_pcd_por_faixa_etaria"]
    pct_extrema = stats["percentagem_pcd_na_extrema_pobreza"]
    ordem = ["Crianças e Adolescentes", "Jovens", "Adultos", "Idosos"]

    print(">>> Proporção de Pessoas com Deficiência (PCD) por faixa etária:")
    for faixa in ordem:
        prop = proporcao.get(faixa, np.nan)
        if pd.isna(prop):
            print(f"  • {faixa:<26}: N/D")
        else:
            print(f"  • {faixa:<26}: {prop * 100:6.4f}% "
                  f"(proporção = {prop:.4f})")
    extras = {k: v for k, v in proporcao.items() if k not in ordem}
    if extras:
        print("\n  (Faixas adicionais encontradas:)")
        for faixa, prop in extras.items():
            print(f"  • {str(faixa):<26}: {prop * 100:6.4f}%")
    print()
    print(f">>> Percentagem de PCDs em extrema pobreza "
          f"(renda per capita ≤ R$ 89,00 em 2018): {pct_extrema:.4f}%")
    print()


def responder_pergunta_4(df_cad: pd.DataFrame) -> None:
    print("\n" + "=" * 78)
    print("PERGUNTA 4 — Impacto da Presença de Crianças na Ocupação das Mães")
    print("=" * 78)
    print("Pergunta: Qual é a taxa de ocupação (trabalho remunerado) entre "
          "mulheres responsáveis\npelo domicílio que possuem crianças de 0 a "
          "6 anos na família, em comparação com\naquelas que não possuem "
          "crianças nessa faixa etária?\n")

    taxas = calculate_employment_rate_by_female_heads_with_young_children(df_cad)
    com_criancas = taxas.get(True, np.nan)
    sem_criancas = taxas.get(False, np.nan)

    print(">>> Taxa de ocupação (trabalho remunerado) entre mulheres "
          "responsáveis pelo domicílio:")
    if pd.isna(com_criancas):
        print("  • Com crianças de 0 a 6 anos : N/D")
    else:
        print(f"  • Com crianças de 0 a 6 anos : {com_criancas * 100:6.4f}% "
              f"(proporção = {com_criancas:.4f})")
    if pd.isna(sem_criancas):
        print("  • Sem crianças de 0 a 6 anos: N/D")
    else:
        print(f"  • Sem crianças de 0 a 6 anos: {sem_criancas * 100:6.4f}% "
              f"(proporção = {sem_criancas:.4f})")
    if not pd.isna(com_criancas) and not pd.isna(sem_criancas):
        diferenca_pp = (com_criancas - sem_criancas) * 100.0
        print()
        print(f">>> Diferença (Com − Sem): {diferenca_pp:+.4f} pontos "
              f"percentuais")
    print()


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

def run():
    input_path = 'amostra.csv/*.csv'
    files = glob.glob(input_path)

    if not files:
        print("Os arquivos .csv não foram encontrados!")
        return

    dfs = []
    for file in files:
        dfs.append(pd.read_csv(file))
    df_cad = pd.concat(dfs, ignore_index=True)

    # Respostas explícitas
    responder_pergunta_1(df_cad)
    responder_pergunta_2(df_cad)
    responder_pergunta_3(df_cad)
    responder_pergunta_4(df_cad)

    # Etapa 3 — IDEB
    print("\n" + "=" * 78)
    print("ETAPA 3: ANÁLISES DO ARQUIVO DE DIVULGAÇÃO DO ENSINO MÉDIO (IDEB)")
    print("=" * 78)
    df_ideb = load_ideb_data("divulgacao_ensino_medio_municipios_2025.xlsx")
    if df_ideb is not None and not df_ideb.empty:
        print("\n--- PERGUNTA 1 (IDEB): Média do IDEB 2025 por UF (rede "
              "Pública) e variação percentual 2017→2025 ---")
        pergunta1 = ideb_mean_by_uf_and_public_network(df_ideb)
        if not pergunta1.empty:
            print(pergunta1.to_string(index=False))
        else:
            print("Não foi possível calcular a Pergunta 1 (IDEB).")

        print("\n--- PERGUNTA 2 (IDEB): Top 10 municípios com maior IDEB 2025 "
              "(rede Pública) e comparação Alta Floresta vs Demais ---")
        pergunta2 = top10_municipios_ideb_2025_e_evolucao_alta_floresta(df_ideb)
        if pergunta2:
            print("\nTop 10 municípios com maior IDEB 2025 (rede Pública):")
            print(pergunta2["top10_municipios_ideb_2025"].to_string(index=False))
            print("\nComparação da evolução do IDEB (2017 → 2025):")
            for grupo, info in pergunta2["comparacao_alta_floresta_vs_demais"].items():
                print(f"\n  Grupo: {grupo}")
                for k, v in info.items():
                    if isinstance(v, float):
                        print(f"    {k}: {v:.4f}")
                    else:
                        print(f"    {k}: {v}")
        else:
            print("Não foi possível calcular a Pergunta 2 (IDEB).")

    # Etapa 4 — gráficos (inclui agora mediana e desvio padrão)
    run_etapa4(df_cad, df_ideb)


if __name__ == '__main__':
    run()
