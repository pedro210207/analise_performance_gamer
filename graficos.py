import matplotlib.pyplot as plt
from analytics import carregar_dataframe

def grafico_fps_por_jogo():
    df = carregar_dataframe()
    dados = df.groupby("nome_jogo")["fps_medio"].mean()

    plt.figure()
    dados.plot(kind="bar")
    plt.title("FPS Médio por Jogo")
    plt.ylabel("FPS Médio")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def grafico_sono_vs_foco():
    df = carregar_dataframe()

    plt.figure()
    plt.scatter(df["horas_sono"], df["nivel_foco"])
    plt.title("Horas de Sono vs Nível de Foco")
    plt.xlabel("Horas de Sono")
    plt.ylabel("Nível de Foco")
    plt.tight_layout()
    plt.show()

def grafico_stutter_por_config():
    df = carregar_dataframe()
    dados = df.groupby("config_grafica")["stutter"].mean()

    plt.figure()
    dados.plot(kind="bar")
    plt.title("Taxa de Stutter por Configuração")
    plt.ylabel("Proporção de Stutter")
    plt.tight_layout()
    plt.show()