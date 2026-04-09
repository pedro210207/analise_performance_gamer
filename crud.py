from database import conectar
import traceback

def categoria_fps(fps):
    if fps <= 30:
        return "0-30"
    elif fps <= 60:
        return "30-60"
    elif fps <= 100:
        return "60-100"
    elif fps <= 150:
        return "100-150"
    else:
        return "150+"

def coletar_dados_sessao():
    horas = float(input("Horas jogadas: "))
    fps = int(input("FPS médio: "))
    stutter = input("Teve stutter? (s/n): ").lower() == "s"
    config = input("Config gráfica: ").strip().lower()
    sono = float(input("Horas de sono: "))
    foco = int(input("Nivel de foco (1-3): "))
    desempenho = int(input("Desempenho percebido (1-3): "))

    return horas, fps, stutter, config, sono, foco, desempenho

def adicionar_sessao():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        nome_jogo = input("Nome do jogo: ").strip().upper()

        cursor.execute("SELECT id FROM jogos WHERE nome=%s", (nome_jogo,))
        resultado = cursor.fetchone()

        if resultado:
            jogo_id = resultado[0]
        else:
            cursor.execute("INSERT INTO jogos(nome) VALUES(%s)", (nome_jogo,))
            conn.commit()
            jogo_id = cursor.lastrowid

        horas, fps, stutter, config, sono, foco, desempenho = coletar_dados_sessao()

        cursor.execute("""
            INSERT INTO sessoes
            (jogo_id, horas_jogadas, fps_medio,
            stutter, config_grafica, horas_sono,
            nivel_foco, desempenho_percebido)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            jogo_id, horas, fps,
            stutter, config, sono,
            foco, desempenho
        ))

        conn.commit()
        print("Sessão adicionada.")

    except Exception:
        traceback.print_exc()

    finally:
        if conn and conn.is_connected():
            conn.close()

def listar_sessoes():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT s.id, j.nome, s.data_sessao, s.fps_medio
            FROM sessoes s
            JOIN jogos j ON s.jogo_id = j.id
            ORDER BY s.id
        """)

        for s in cursor.fetchall():
            print(
                f"ID:{s[0]} | Jogo:{s[1]} | Data:{s[2]} "
                f"| FPS:{s[3]} ({categoria_fps(s[3])})"
            )

    except Exception:
        traceback.print_exc()

    finally:
        if conn and conn.is_connected():
            conn.close()

def editar_sessao():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        listar_sessoes()
        id_editar = int(input("\nID da sessão para editar: "))

        horas, fps, stutter, config, sono, foco, desempenho = coletar_dados_sessao()

        cursor.execute("""
            UPDATE sessoes
            SET horas_jogadas=%s,
                fps_medio=%s,
                stutter=%s,
                config_grafica=%s,
                horas_sono=%s,
                nivel_foco=%s,
                desempenho_percebido=%s
            WHERE id=%s
        """, (
            horas, fps, stutter,
            config, sono, foco,
            desempenho, id_editar
        ))

        conn.commit()
        print("Sessão editada.")

    except Exception:
        traceback.print_exc()

    finally:
        if conn and conn.is_connected():
            conn.close()

def apagar_sessao():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        listar_sessoes()
        id_apagar = int(input("\nID da sessão para apagar: "))

        cursor.execute("DELETE FROM sessoes WHERE id=%s", (id_apagar,))
        conn.commit()

        print("Sessão apagada.")

    except Exception:
        traceback.print_exc()

    finally:
        if conn and conn.is_connected():
            conn.close()