# Trabalho de Linguagens Formais e Autômatos
# Simulador de AFD - Autômato Finito Determinístico


# ------------------------------------------------------------
# FUNÇÃO: ler_lista()
# ------------------------------------------------------------
# Lê uma linha digitada pelo usuário e transforma em lista.
#
# Exemplo:
# Entrada:
#   q0, q1, q2
#
# Saída:
#   ["q0", "q1", "q2"]
#
# O strip() remove espaços extras antes/depois do texto.
# ------------------------------------------------------------
def ler_lista(mensagem):
    entrada = input(mensagem)

    # split(',') separa a string usando vírgula
    # item.strip() remove espaços desnecessários
    lista = [item.strip() for item in entrada.split(',')]

    return lista


# ------------------------------------------------------------
# FUNÇÃO: montar_tabela_de_transicoes()
# ------------------------------------------------------------
# Cria a tabela de transições do autômato.
#
# A tabela será um dicionário no formato:
#
# transicoes[estado][simbolo] = proximo_estado
#
# Exemplo:
# transicoes["q0"]["a"] = "q1"
#
# Significa:
# "Se estiver em q0 e ler 'a', vá para q1"
# ------------------------------------------------------------
def montar_tabela_de_transicoes(estados, alfabeto):

    # Dicionário principal das transições
    transicoes = {}

    # Percorre cada estado do autômato
    for estado in estados:

        # Cria um dicionário interno para esse estado
        transicoes[estado] = {}

        # Para cada símbolo do alfabeto...
        for simbolo in alfabeto:

            # Pergunta qual será o próximo estado
            proximo = input(f"  f({estado}, {simbolo}) -> ").strip()

            # Salva a transição no dicionário
            transicoes[estado][simbolo] = proximo

    return transicoes


# ------------------------------------------------------------
# FUNÇÃO: checar_transicoes()
# ------------------------------------------------------------
# Verifica se os estados digitados nas transições existem.
#
# Isso evita erros como:
# q9 (quando q9 nem existe no conjunto de estados)
# ------------------------------------------------------------
def checar_transicoes(transicoes, estados, alfabeto):

    # Lista que guardará mensagens de erro
    erros = []

    # Percorre todos os estados
    for estado in estados:

        # Percorre todos os símbolos
        for simbolo in alfabeto:

            # Descobre para qual estado a transição aponta
            destino = transicoes[estado][simbolo]

            # Verifica se esse estado realmente existe
            if destino not in estados:

                # Se não existir, adiciona um erro na lista
                erros.append(
                    f"  f({estado}, {simbolo}) -> '{destino}' nao existe nos estados"
                )

    return erros


# ------------------------------------------------------------
# FUNÇÃO: rodar_palavra()
# ------------------------------------------------------------
# Simula o funcionamento do AFD lendo uma palavra.
#
# O programa percorre letra por letra da palavra,
# mudando de estado conforme a tabela de transições.
#
# No final:
# - Se terminar em estado final -> ACEITA
# - Caso contrário -> REJEITA
# ------------------------------------------------------------
def rodar_palavra(
    palavra,
    estado_inicial,
    estados_de_aceitacao,
    transicoes,
    alfabeto
):

    # O autômato começa no estado inicial
    estado_atual = estado_inicial

    # Lista para guardar todos os estados visitados
    historico = [estado_atual]

    # Percorre cada letra da palavra digitada
    for letra in palavra:

        # Verifica se a letra pertence ao alfabeto
        if letra not in alfabeto:

            print(f"\n  A letra '{letra}' nao pertence ao alfabeto.")

            # Retorna False porque a palavra é inválida
            return False

        # Consulta a tabela:
        # "Em qual estado vou parar?"
        proximo_estado = transicoes[estado_atual][letra]

        # Guarda no histórico
        historico.append(proximo_estado)

        # Atualiza o estado atual
        estado_atual = proximo_estado

    # Mostra todo o caminho percorrido pelo autômato
    print(f"\n  Caminho: {' -> '.join(historico)}")

    # A palavra será aceita se o último estado
    # estiver entre os estados de aceitação
    aceita = estado_atual in estados_de_aceitacao

    return aceita


# ------------------------------------------------------------
# FUNÇÃO PRINCIPAL
# ------------------------------------------------------------
# Controla todo o funcionamento do programa.
# ------------------------------------------------------------
def main():

    # Exibe o cabeçalho do sistema
    print("\n" + "=" * 45)
    print("     AFD - Simulador de Automato Finito")
    print("=" * 45 + "\n")

    # --------------------------------------------------------
    # LEITURA DAS DEFINIÇÕES DO AUTÔMATO
    # --------------------------------------------------------

    # Lê o alfabeto
    alfabeto = ler_lista("Simbolos do alfabeto (ex: a, b): ")

    # Lê os estados
    estados = ler_lista("Conjunto de estados  (ex: q0, q1, q2): ")

    # Lê o estado inicial
    estado_inicial = input("Estado inicial: ").strip()

    # Lê os estados finais
    estados_finais = ler_lista(
        "Estados de aceitacao (ex: q1, q3): "
    )

    # --------------------------------------------------------
    # VALIDAÇÕES
    # --------------------------------------------------------

    # Verifica se o estado inicial existe
    if estado_inicial not in estados:

        print(
            f"\n  Erro: '{estado_inicial}' nao esta no conjunto de estados."
        )

        return

    # Verifica se os estados finais existem
    for estado in estados_finais:

        if estado not in estados:

            print(
                f"\n  Erro: '{estado}' nao esta no conjunto de estados."
            )

            return

    # --------------------------------------------------------
    # MONTAGEM DAS TRANSIÇÕES
    # --------------------------------------------------------

    print(
        "\n  Preencha as transicoes "
        "(para onde cada estado vai com cada simbolo):"
    )

    # Cria a tabela de transições
    transicoes = montar_tabela_de_transicoes(estados, alfabeto)

    # Verifica se há erros nas transições
    erros = checar_transicoes(transicoes, estados, alfabeto)

    # Se houver erros, mostra todos e encerra
    if erros:

        print("\n  Erros encontrados nas transicoes:")

        for erro in erros:
            print(erro)

        return

    # --------------------------------------------------------
    # EXIBE A TABELA DE TRANSIÇÕES
    # --------------------------------------------------------

    print("\n" + "-" * 45)
    print("  Tabela de transicoes (Delta):")
    print("-" * 45)

    # Percorre toda a tabela e imprime
    for estado in estados:

        for simbolo in alfabeto:

            destino = transicoes[estado][simbolo]

            print(f"  Delta({estado}, {simbolo}) : {destino}")

    # --------------------------------------------------------
    # RESUMO DO AUTÔMATO
    # --------------------------------------------------------

    print("-" * 45)

    print(f"  Estado inicial   : {estado_inicial}")

    print(f"  Estados de aceit.: {', '.join(estados_finais)}")

    print("-" * 45)

    # --------------------------------------------------------
    # LOOP DE TESTE DE PALAVRAS
    # --------------------------------------------------------

    print("\n  Automato pronto! Digite palavras para testar.")

    print("  (Pressione Enter vazio para sair)\n")

    while True:

        # Lê uma palavra digitada pelo usuário
        palavra = input("  >> ").strip()

        # Enter vazio encerra o programa
        if not palavra:

            print("  Encerrando.")

            break

        # Executa a simulação da palavra
        aceita = rodar_palavra(
            palavra,
            estado_inicial,
            estados_finais,
            transicoes,
            alfabeto
        )

        # Exibe o resultado final
        if aceita:

            print("  Resultado: [ACEITA]\n")

        else:

            print("  Resultado: [REJEITA]\n")


# ------------------------------------------------------------
# INÍCIO DO PROGRAMA
# ------------------------------------------------------------
# Chama a função principal para iniciar o sistema
# ------------------------------------------------------------
main()