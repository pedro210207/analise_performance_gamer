import mysql.connector
import random
from datetime import datetime, timedelta
from database import conectar

def gerar_dados_fakes(qtd_sessoes=500):
    conn = conectar()
    cursor = conn.cursor()

    jogos_fakes = [
        {"nome": "VALORANT", "peso": "leve"},
        {"nome": "CS:GO 2", "peso": "leve"},
        {"nome": "CYBERPUNK 2077", "peso": "pesado"},
        {"nome": "ELDEN RING", "peso": "pesado"},
        {"nome": "THE WITCHER 3", "peso": "medio"}
    ]

    print("Inserindo jogos...")
    jogos_ids = []
    for jogo in jogos_fakes:
        cursor.execute("SELECT id FROM jogos WHERE nome=%s", (jogo["nome"],))
        resultado = cursor.fetchone()
        if resultado:
            jogo_id = resultado[0]
        else:
            cursor.execute("INSERT INTO jogos(nome) VALUES(%s)", (jogo["nome"],))
            conn.commit()
            jogo_id = cursor.lastrowid

        jogos_ids.append({"id": jogo_id, "peso": jogo["peso"]})

    print(f"Gerando {qtd_sessoes} sessões falsas.")

    configs = ["baixa", "media", "alta", "ultra"]
    hoje = datetime.now()

    for _ in range(qtd_sessoes):
        jogo_escolhido = random.choice(jogos_ids)

        horas = round(random.uniform(0.5, 5.0), 1)

        config = random.choice(configs)

        if jogo_escolhido["peso"] == "pesado" and config in ["alta", "ultra"]:
            fps = random.randint(30, 75)
            stutter = True if random.random() > 0.4 else False
        elif jogo_escolhido["peso"] == "leve":
            fps = random.randint(120, 300)
            stutter = False
        else:
            fps = random.randint(60, 144)
            stutter = True if random.random() > 0.8 else False

        sono = round(random.uniform(3.0, 10.0), 1)
        if sono < 5.5:
            foco = random.randint(1, 2)
            desempenho = random.randint(1, 2)
        elif sono > 7.5:
            foco = random.randint(2, 3)
            desempenho = random.randint(2, 3)
        else:
            foco = random.randint(1, 3)
            desempenho = random.randint(1, 3)

        dias_atras = random.randint(0, 180)
        data_sessao = hoje - timedelta(days=dias_atras)

        cursor.execute("""
            INSERT INTO sessoes
            (jogo_id, horas_jogadas, fps_medio, stutter, config_grafica,
            horas_sono, nivel_foco, desempenho_percebido, data_sessao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            jogo_escolhido["id"], horas, fps, stutter, config,
            sono, foco, desempenho, data_sessao.strftime('%Y-%m-%d %H:%M:%S')
        ))

    conn.commit()
    conn.close()
    print("Boa! 500 partidas foram injetadas no seu banco de dados.")

if __name__ == "__main__":
    gerar_dados_fakes()