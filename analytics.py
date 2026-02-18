import pandas as pd
from database import conectar

def carregar_dataframe():
    conn = conectar()

    df = pd.read_sql("""
        SELECT s.*, j.nome AS nome_jogo
        FROM sessoes s
        JOIN jogos j ON s.jogo_id = j.id
    """, conn)

    conn.close()
    return df

def analise_pandas():
    df = carregar_dataframe()

    if df.empty:
        print("Nenhum dado encontrado.")
        return

    print("\n=== RESUMO GERAL ===")
    print(df[['fps_medio','horas_jogadas','nivel_foco']].mean().round(2))

    print("\n=== FPS MÉDIO POR JOGO ===")
    print(df.groupby('nome_jogo')['fps_medio'].mean().round(2))

    print("\n=== STUTTER POR CONFIG ===")
    print(df.groupby('config_grafica')['stutter'].mean().round(2))

    print("\n=== SESSÕES DE RISCO ===")
    risco = df[(df['horas_sono'] < 6) & (df['nivel_foco'] == 1)]
    print(risco[['nome_jogo','fps_medio','horas_sono','nivel_foco']])