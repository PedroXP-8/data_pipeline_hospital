Pipeline de dados - hospital

SOBRE O PROJETO:

 - Este projeto consiste na construção de uma pipeline de dados completa utilizando dados hospitalares. O objetivo é demonstrar na prática           conceitos fundamentais de engenharia de dados, incluindo ingestão, transformação, modelagem e carga de dados em um banco relacional.
 - A pipeline segue o padrão ETL (Extract, Transform, Load) e utiliza Python e SQLite para processamento e armazenamento dos dados.

ARQUITETURA DA PIPELINE:

 Extract → Transform → Load → SQL Analysis
 
  - Extract: leitura de dados brutos (CSV)
  - Transform: limpeza e tratamento dos dados com Pandas
  - Load: inserção dos dados no banco SQLite
  - SQL Analysis: consultas analíticas com SQL
  - 
TECNOLOGIAS UTILIZADAS:
  - Python
  - Pandas
  - NumPy
  - SQLite
  - SQL


ESTRUTURA DO PORJETO:

proejto_pipeline_hospital/
│
├── data/
│   ├── Processed/    # Dados tratados
│   └── Raw/          # Dados brutos
│
├── Database/
│   └── hospital.db         # Banco de dados SQLite
│
├── Pipeline/
│   ├── extract.py          # Extração dos dados
│   ├── transform.py        # Transformação dos dados
│   ├── load.py             # Carga no banco
│   └── tables.py           # Criação das tabelas
│
├── sql/
│   ├── model.png           # Modelo Relacional do banco de dados
│   ├── queries.py          # queries com Sql/Python
│
├── main.py                 # Orquestração da pipeline
│
├── requirements.txt
└── README.md

MODELAGEM DE DAODS:

 O banco de dados foi estruturado de forma relacional, contendo as seguintes tabelas:

   - doctors
   - patients
   - appointments
   - treatments
   - billings

 A modelagem inclui:

   - Chaves primárias (PRIMARY KEY)
   - Relacionamentos (FOREIGN KEY)
   - Normalização dos dados


PIPELINE:

  1. Extract
  - Leitura dos dados brutos a partir de arquivos CSV.

  2. Transform
  - Remoção de valores nulos
  - Padronização de colunas
  - Conversão de tipos de dados
  - Criação de novas variáveis
    
  3. Load
  - Inserção dos dados no banco SQLite
  - Separação em múltiplas tabelas
  - Preservação da integridade relacional

    
COMO EXECUTAR O PROJETO:

  1. Clonar o repositório
    git clone <seu-repositorio>
    cd hospital-data-pipeline

  2. Instalar dependências
    pip install -r requirements.txt

  3. Executar a pipeline
    python main.py


OBJETIVO DO PROJETO:

  - Praticar construção de pipelines de dados
  - Aplicar conceitos de modelagem relacional
  - Utilizar SQL para análise de dados
  - Simular um fluxo real de engenharia de dados

POSSÍVEIS MELHORIAS:

  - Adicionar orquestração com Airflow
  - Utilizar banco de dados em nuvem
  - Implementar testes de qualidade de dados
  - Criar dashboards (Power BI ou Python)

AUTOR: PEDRO HENRIQUE SILVA DIAS

  - Desenvolvido como projeto de estudo em Engenharia de Dados.

CONTATO:

  - Linkedin: www.linkedin.com/in/pedro-henrique-s-8257923b3
  - email: phsdias8@hotmail.com
    
