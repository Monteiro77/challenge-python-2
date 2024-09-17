# Gerenciamento da Fórmula E em Python

## Visão Geral

Este projeto em Python é um sistema simples para gerenciar e promover a Fórmula E, uma popular categoria de corridas de carros elétricos. O sistema permite visualizar informações sobre corridas e pilotos, simular corridas entre pilotos, atualizar pontuações e gerar relatórios detalhados sobre o desempenho dos pilotos.

## Funcionalidades

- **Mostrar Próximas Corridas**: Exibe uma lista de próximas corridas com local, data e horário.
- **Mostrar Pilotos**: Exibe uma lista de pilotos com seus respectivos times e pontuações.
- **Atualizar Pontuação do Piloto**: Permite atualizar a pontuação de um piloto específico.
- **Simular Corrida**: Simula uma corrida entre dois pilotos e exibe o resultado.
- **Gerar Relatório**: Gera um relatório com as estatísticas atuais dos pilotos, ordenando-os por pontuação e exibindo gráficos de barras horizontais para visualização.

## Estrutura do Projeto

O projeto é composto por um único arquivo Python que inclui todas as funcionalidades. A estrutura do código é a seguinte:

- **Dados Fictícios**: Contém listas de corridas e pilotos.
- **Funções**:
  - `mostrar_corridas()`: Exibe a lista de próximas corridas.
  - `mostrar_pilotos()`: Exibe a lista de pilotos e suas pontuações.
  - `atualizar_pontuacao(nome_piloto, pontos)`: Atualiza a pontuação de um piloto.
  - `simular_corrida(piloto1, piloto2)`: Simula uma corrida entre dois pilotos e exibe o resultado.
  - `gerar_relatorio()`: Gera um relatório detalhado com os pilotos ordenados por pontuação e exibe gráficos de barras horizontais.
  - `menu()`: Exibe o menu principal e gerencia a interação do usuário.

## Detalhamento das Funções

### `mostrar_corridas()`

Exibe as próximas corridas com local, data e horário.

### `mostrar_pilotos()`

Exibe a lista de pilotos, suas equipes e pontuações.

### `atualizar_pontuacao(nome_piloto, pontos)`

Atualiza a pontuação de um piloto específico. Verifica se o piloto está na lista antes de atualizar.

**Parâmetros:**
- `nome_piloto` (str): Nome do piloto a ser atualizado.
- `pontos` (int): Número de pontos a ser adicionado.

### `simular_corrida(piloto1, piloto2)`

Simula uma corrida entre dois pilotos e exibe o resultado. A pontuação da corrida é gerada aleatoriamente.

**Parâmetros:**
- `piloto1` (str): Nome do primeiro piloto.
- `piloto2` (str): Nome do segundo piloto.

### `gerar_relatorio()`

Gera um relatório com as estatísticas atuais dos pilotos. Ordena os pilotos por pontuação e exibe gráficos de barras horizontais para visualização.

### `menu()`

Exibe o menu principal e lida com as opções do usuário. Permite navegar entre as funcionalidades do sistema.


### Testes e Validação
Verificação Manual: Execute cada opção do menu e verifique se as saídas correspondem ao esperado.
Testes de Pontuação: Teste a atualização de pontuações e simulação de corridas com diferentes entradas para garantir a precisão.

## Licença

Este projeto é licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.****

### Explicação

1. **Visão Geral**: Descreve o propósito e a utilidade do projeto.
2. **Funcionalidades**: Lista as principais funcionalidades do sistema.
3. **Estrutura do Projeto**: Explica a organização do código.
4. **Detalhamento das Funções**: Fornece uma descrição detalhada de cada função, incluindo parâmetros e comportamento.
5. **Como Executar**: Instruções sobre como configurar e executar o projeto.
6. **Exemplos de Uso**: Exemplos práticos de como usar cada funcionalidade.
7. **Testes e Validação**: Orientações sobre como verificar e validar o funcionamento do código.
8. **Contribuição**: Diretrizes para quem deseja colaborar com o projeto.
9. **Licença**: Informações sobre a licença do projeto.

Esse formato deve tornar a documentação clara e fácil de seguir para quem for ler o `README.md`. Se precisar de mais ajustes ou informações adicionais, me avise!
