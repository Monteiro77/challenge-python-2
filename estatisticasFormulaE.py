import random

# Dados fictícios atualizados com pilotos reais em formato de dicionário
corridas = [
    {"local": "São Paulo", "data": "2024-09-28", "horario": "14:00"},
    {"local": "Paris", "data": "2024-10-12", "horario": "16:00"}
]

pilotos = {
    "Jake Dennis": {"equipe": "Avalanche Andretti", "pontos": 50},
    "António Félix da Costa": {"equipe": "DS PENSKE", "pontos": 40},
    "Pascal Wehrlein": {"equipe": "TAG Heuer Porsche", "pontos": 70},
    "Jean-Éric Vergne": {"equipe": "DS PENSKE", "pontos": 60},
    "Mitch Evans": {"equipe": "Jaguar TCS Racing", "pontos": 55},
    "Lucas di Grassi": {"equipe": "Mahindra Racing", "pontos": 45},
    "Oliver Rowland": {"equipe": "Mahindra Racing", "pontos": 35},
    "Edoardo Mortara": {"equipe": "ROKiT Venturi Racing", "pontos": 50},
    "Nick Cassidy": {"equipe": "Envision Racing", "pontos": 60},
    "Sacha Fenestraz": {"equipe": "Nissan Formula E Team", "pontos": 42},
    "Robin Frijns": {"equipe": "Envision Racing", "pontos": 48},
    "Stoffel Vandoorne": {"equipe": "Mercedes-Benz EQ Formula E Team", "pontos": 68},
    "Nyck de Vries": {"equipe": "Mercedes-Benz EQ Formula E Team", "pontos": 63},
    "Sebastien Buemi": {"equipe": "Nissan Formula E Team", "pontos": 39},
    "Maximilian Günther": {"equipe": "Avalanche Andretti", "pontos": 43},
    "Antonio Giovinazzi": {"equipe": "Dragon/Penske Autosport", "pontos": 30},
    "Maro Engel": {"equipe": "ROKiT Venturi Racing", "pontos": 32},
    "Dan Ticktum": {"equipe": "NIO 333 FE Team", "pontos": 38},
    "Oliver Turvey": {"equipe": "NIO 333 FE Team", "pontos": 36},
    "Jake Hughes": {"equipe": "McLaren Racing", "pontos": 33},
    "Felipe Massa": {"equipe": "Venturi Racing", "pontos": 37},
    "Zhou Guanyu": {"equipe": "McLaren Racing", "pontos": 41}
}

def mostrar_corridas():
    """Exibe a lista de próximas corridas."""
    print("Próximas Corridas:")
    for corrida in corridas:
        print(f"Local: {corrida['local']}, Data: {corrida['data']}, Horário: {corrida['horario']}")

def mostrar_pilotos():
    """Exibe a lista de pilotos e suas pontuações."""
    print("Pilotos:")
    for i, (nome, info) in enumerate(pilotos.items(), start=1):
        print(f"{i}. Nome: {nome}, Equipe: {info['equipe']}, Pontos: {info['pontos']}")

def atualizar_pontuacao(indice_piloto, pontos):
    """Atualiza a pontuação de um piloto com base no índice fornecido."""
    piloto_nomes = list(pilotos.keys())
    if 0 < indice_piloto <= len(piloto_nomes):
        nome_piloto = piloto_nomes[indice_piloto - 1]
        pilotos[nome_piloto]['pontos'] += pontos
        print(f"Pontos atualizados para {nome_piloto}. Nova pontuação: {pilotos[nome_piloto]['pontos']}")
    else:
        print("Índice do piloto inválido.")

def simular_corrida(piloto1, piloto2):
    """Simula uma corrida entre dois pilotos e exibe o resultado."""
    if piloto1 in pilotos and piloto2 in pilotos:
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
    else:
        print("Um ou ambos os pilotos não foram encontrados.")

def gerar_relatorio():
    """Gera um relatório com as estatísticas atuais, ordenando os pilotos por pontuação e formatando a saída."""
    print("\nRelatório da Fórmula E")
    print("----------------------")
    mostrar_corridas()

    print("\nPilotos Ordenados por Pontuação:")
    # Ordenar pilotos por pontuação (em ordem decrescente)
    pilotos_ordenados = sorted(pilotos.items(), key=lambda x: x[1]['pontos'], reverse=True)

    # Encontrar a pontuação máxima para dimensionar as barras
    pontuacao_maxima = max(info['pontos'] for _, info in pilotos_ordenados)

    # Imprimir cabeçalho da tabela
    print(f"{'Nome':<25} | {'Equipe':<20} | {'Pontos':<7} | {'Barra':<30}")
    print("-" * 85)

    # Imprimir a tabela com barras horizontais e linhas quebradas
    for nome, info in pilotos_ordenados:
        equipe = info['equipe']
        pontos = info['pontos']
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
            try:
                mostrar_pilotos()  # Mostra a lista numerada de pilotos
                indice_piloto = int(input("Número do piloto: "))
                pontos = int(input("Número de pontos a adicionar: "))
                atualizar_pontuacao(indice_piloto, pontos)
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir números válidos.")
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
