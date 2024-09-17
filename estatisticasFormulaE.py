import random

# Dados fictícios atualizados com pilotos reais
corridas = [
    ["São Paulo", "2024-09-28", "14:00"],
    ["Paris", "2024-10-12", "16:00"]
]

pilotos = [
    ["Jake Dennis", "Avalanche Andretti", 50],
    ["António Félix da Costa", "DS PENSKE", 40],
    ["Pascal Wehrlein", "TAG Heuer Porsche", 70],
    ["Jean-Éric Vergne", "DS PENSKE", 60],
    ["Mitch Evans", "Jaguar TCS Racing", 55],
    ["Lucas di Grassi", "Mahindra Racing", 45],
    ["Oliver Rowland", "Mahindra Racing", 35],
    ["Edoardo Mortara", "ROKiT Venturi Racing", 50],
    ["Nick Cassidy", "Envision Racing", 60],
    ["Sacha Fenestraz", "Nissan Formula E Team", 42],
    ["Robin Frijns", "Envision Racing", 48],
    ["Stoffel Vandoorne", "Mercedes-Benz EQ Formula E Team", 68],
    ["Nyck de Vries", "Mercedes-Benz EQ Formula E Team", 63],
    ["Sebastien Buemi", "Nissan Formula E Team", 39],
    ["Maximilian Günther", "Avalanche Andretti", 43],
    ["Antonio Giovinazzi", "Dragon/Penske Autosport", 30],
    ["Maro Engel", "ROKiT Venturi Racing", 32],
    ["Dan Ticktum", "NIO 333 FE Team", 38],
    ["Oliver Turvey", "NIO 333 FE Team", 36],
    ["Jake Hughes", "McLaren Racing", 33],
    ["Felipe Massa", "Venturi Racing", 37],
    ["Zhou Guanyu", "McLaren Racing", 41]
]


def mostrar_corridas():
    """Exibe a lista de próximas corridas."""
    print("Próximas Corridas:")
    for corrida in corridas:
        print(f"Local: {corrida[0]}, Data: {corrida[1]}, Horário: {corrida[2]}")


def mostrar_pilotos():
    """Exibe a lista de pilotos e suas pontuações."""
    print("Pilotos:")
    for piloto in pilotos:
        print(f"Nome: {piloto[0]}, Equipe: {piloto[1]}, Pontos: {piloto[2]}")


def atualizar_pontuacao(nome_piloto, pontos):
    """Atualiza a pontuação de um piloto."""
    for piloto in pilotos:
        if piloto[0] == nome_piloto:
            piloto[2] += pontos
            print(f"Pontos atualizados para {nome_piloto}. Nova pontuação: {piloto[2]}")
            return
    print("Piloto não encontrado.")


def simular_corrida(piloto1, piloto2):
    """Simula uma corrida entre dois pilotos e exibe o resultado."""
    resultado = {
        piloto1: random.randint(0, 100),
        piloto2: random.randint(0, 100)
    }
    print("Resultado da corrida:")
    for piloto, pontos in resultado.items():
        print(f"{piloto}: {pontos} pontos")
    if resultado[piloto1] > resultado[piloto2]:
        print(f"{piloto1} venceu a corrida!")
    elif resultado[piloto1] < resultado[piloto2]:
        print(f"{piloto2} venceu a corrida!")
    else:
        print("A corrida terminou em empate!")


def gerar_relatorio():
    """Gera um relatório com as estatísticas atuais, ordenando os pilotos por pontuação e formatando a saída."""
    print("\nRelatório da Fórmula E")
    print("----------------------")
    mostrar_corridas()

    print("\nPilotos Ordenados por Pontuação:")
    # Ordenar pilotos por pontuação (em ordem decrescente)
    pilotos_ordenados = sorted(pilotos, key=lambda x: x[2], reverse=True)

    # Encontrar a pontuação máxima para dimensionar as barras
    pontuacao_maxima = max(piloto[2] for piloto in pilotos_ordenados)

    # Imprimir cabeçalho da tabela
    print(f"{'Nome':<25} | {'Equipe':<20} | {'Pontos':<7}")
    print("-" * 60)

    # Imprimir a tabela com barras horizontais e linhas quebradas
    for piloto in pilotos_ordenados:
        nome = piloto[0]
        equipe = piloto[1]
        pontos = piloto[2]
        barra = '#' * int((pontos / pontuacao_maxima) * 30)  # Barra proporcional à pontuação máxima
        print(f"{nome:<25} | {equipe:<20} | {pontos:<7}")



def menu():
    """Exibe o menu principal e lida com as opções do usuário."""
    while True:
        print("\nMenu:")
        print("1. Mostrar Próximas Corridas")
        print("2. Mostrar Pilotos")
        print("3. Atualizar Pontuação do Piloto")
        print("4. Simular Corrida")
        print("5. Gerar Relatório")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            mostrar_corridas()
        elif escolha == '2':
            mostrar_pilotos()
        elif escolha == '3':
            nome_piloto = input("Nome do piloto: ")
            pontos = int(input("Número de pontos a adicionar: "))
            atualizar_pontuacao(nome_piloto, pontos)
        elif escolha == '4':
            piloto1 = input("Nome do primeiro piloto: ")
            piloto2 = input("Nome do segundo piloto: ")
            simular_corrida(piloto1, piloto2)
        elif escolha == '5':
            gerar_relatorio()
        elif escolha == '6':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
