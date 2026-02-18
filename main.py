from crud import *
from analytics import analise_pandas
from graficos import *

def menu():
    while True:
        print("\n=== Performance Analytics ===")
        print("1 - Nova sessão")
        print("2 - Listar sessões")
        print("3 - Editar sessão")
        print("4 - Apagar sessão")
        print("5 - Análise Pandas")
        print("6 - Gráfico FPS por jogo")
        print("7 - Gráfico Sono vs Foco")
        print("8 - Gráfico Stutter por Config")
        print("9 - Sair")

        op = input("Opção: ")

        if op == "1":
            adicionar_sessao()
        elif op == "2":
            listar_sessoes()
        elif op == "3":
            editar_sessao()
        elif op == "4":
            apagar_sessao()
        elif op == "5":
            analise_pandas()
        elif op == "6":
            grafico_fps_por_jogo()
        elif op == "7":
            grafico_sono_vs_foco()
        elif op == "8":
            grafico_stutter_por_config()
        elif op == "9":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()