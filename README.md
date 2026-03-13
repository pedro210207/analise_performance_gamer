# Análise de Performance Gamer

Projeto em Python para registrar e analisar sessões de jogos, armazenando dados em um banco MySQL e gerando análises estatísticas e gráficos.

A ideia é entender como fatores como sono, foco e configuração gráfica impactam o desempenho no jogo.

---

## O que o sistema faz

- Permite cadastrar sessões de jogo
- Salva os dados em banco de dados
- Lista, edita e remove sessões
- Calcula médias de desempenho
- Gera gráficos automáticos
- Identifica sessões de risco (pouco sono + baixo foco)

---

## Tecnologias utilizadas

- Python
- MySQL
- Pandas
- Matplotlib
- Git

---

## Como rodar o projeto

### 1. Instalar dependências

```bash
pip install pandas matplotlib mysql-connector-python
```

### 2. Criar o banco de dados

Executar o arquivo `database.sql` no MySQL.

### 3. Configurar acesso ao banco

Editar o arquivo `database.py` com seu usuário, senha e porta do MySQL.

### 4. Executar o sistema

```bash
python main.py
```

---

## Objetivo

Projeto desenvolvido para praticar:

- CRUD com banco de dados
- Modelagem relacional (com chave estrangeira)
- Análise de dados com Pandas
- Visualização com Matplotlib
- Organização de código em módulos