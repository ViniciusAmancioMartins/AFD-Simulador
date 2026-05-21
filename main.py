# Trabalho de Linguagens Formais e Autômatos
# Simulador de AFD - Autômato Finito Determinístico


# ------------------------------------------------------------
# FUNÇÃO: ler_lista()
# ------------------------------------------------------------
def ler_lista(mensagem):
    entrada = input(mensagem)
    lista = [item.strip() for item in entrada.split(',')]
    return lista


# ------------------------------------------------------------
# FUNÇÃO: montar_tabela_de_transicoes()
# ------------------------------------------------------------
def montar_tabela_de_transicoes(estados, alfabeto):
    transicoes = {}
    for estado in estados:
        transicoes[estado] = {}
        for simbolo in alfabeto:
            # Informa ao usuário que ele pode usar '-'
            proximo = input(f"  f({estado}, {simbolo}) [ou '-' para vazio] -> ").strip()
            transicoes[estado][simbolo] = proximo
    return transicoes


# ------------------------------------------------------------
# FUNÇÃO: checar_transicoes()
# ------------------------------------------------------------
def checar_transicoes(transicoes, estados, alphabeto):
    erros = []
    for estado in estados:
        for simbolo in alphabeto:
            destino = transicoes[estado][simbolo]
            
            # AGORA ACEITA '-': Só dá erro se o destino não for '-' E não estiver nos estados
            if destino != "-" and destino not in estados:
                erros.append(
                    f"  f({estado}, {simbolo}) -> '{destino}' nao existe nos estados (use '-' para sem transição)"
                )
    return erros


# ------------------------------------------------------------
# FUNÇÃO: rodar_palavra()
# ------------------------------------------------------------
def rodar_palavra(
    palavra,
    estado_inicial,
    estados_de_aceitacao,
    transicoes,
    alfabeto
):
    estado_atual = estado_inicial
    historico = [estado_atual]

    for letra in palavra:
        if letra not in alfabeto:
            print(f"\n  A letra '{letra}' nao pertence ao alfabeto.")
            return False

        proximo_estado = transicoes[estado_atual][letra]

        # SE ENCONTRAR '-': O autômato não tem transição, logo a palavra é rejeitada
        if proximo_estado == "-":
            historico.append("Ø (Travou)")
            print(f"\n  Caminho: {' -> '.join(historico)}")
            print(f"  [Erro]: Nao existe transicao para a letra '{letra}' a partir do estado '{estado_atual}'.")
            return False

        historico.append(proximo_estado)
        estado_atual = proximo_estado

    print(f"\n  Caminho: {' -> '.join(historico)}")

    aceita = estado_atual in estados_de_aceitacao
    return aceita


# ------------------------------------------------------------
# FUNÇÃO PRINCIPAL
# ------------------------------------------------------------
def main():
    # Loop externo que permite criar múltiplos autômatos sem fechar o programa
    while True:
        print("\n" + "=" * 45)
        print("     AFD - Simulador de Automato Finito")
        print("=" * 45 + "\n")

        print("--- CONFIGURAÇÃO DO NOVO AUTÔMATO ---")
        alfabeto = ler_lista("Simbolos do alfabeto (ex: a, b): ")
        estados = ler_lista("Conjunto de estados  (ex: q0, q1, q2): ")
        estado_inicial = input("Estado inicial: ").strip()
        estados_finais = ler_lista("Estados de aceitacao (ex: q1, q3): ")

        if estado_inicial not in estados:
            print(f"\n  Erro: '{estado_inicial}' nao esta no conjunto de estados.")
            print("  Reiniciando configuração...")
            continue

        validar_finais = True
        for estado in estados_finais:
            if estado not in estados:
                print(f"\n  Erro: '{estado}' nao esta no conjunto de estados.")
                print("  Reiniciando configuração...")
                validar_finais = False
                break
        
        if not validar_finais:
            continue

        print("\n  Preencha as transicoes (digite '-' se nao houver transicao):")
        transicoes = montar_tabela_de_transicoes(estados, alfabeto)
        erros = checar_transicoes(transicoes, estados, alfabeto)

        if erros:
            print("\n  Erros encontrados nas transicoes:")
            for erro in erros:
                print(erro)
            print("  Reiniciando configuração...")
            continue

        print("\n" + "-" * 45)
        print("Tabela de transicoes (Delta):")
        print("-" * 45)
        for estado in estados:
            for simbolo in alfabeto:
                destino = transicoes[estado][simbolo]
                print(f"  Delta({estado}, {simbolo}) : {destino}")

        print("-" * 45)
        print(f"Estado inicial   : {estado_inicial}")
        print(f"Estados de aceit.: {', '.join(estados_finais)}")
        print("-" * 45)

        # Loop interno para testar várias palavras no autômato atual
        print("\nAutomato pronto! Digite palavras para testar.")
        print("(Aperte ENTER sem digitar nada para testar a PALAVRA VAZIA)")
        print("(Digite 'novo' para CONFIGURAR OUTRO autômato)")
        print("(Digite 'sair' para FECHAR O PROGRAMA completamente)\n")

        comando_global = None

        while True:
            palavra = input("  >> ").strip()

            # Se o usuário quiser criar um novo autômato
            if palavra.lower() == 'novo':
                comando_global = 'novo'
                print("\n  Limpando memória... Vamos criar um novo autômato!")
                break

            # Se o usuário quiser fechar o programa
            if palavra.lower() == 'sair':
                comando_global = 'sair'
                print("  Encerrando o simulador. Até logo!")
                break

            aceita = rodar_palavra(
                palavra,
                estado_inicial,
                estados_finais,
                transicoes,
                alfabeto
            )

            if aceita:
                print("  Resultado: [ACEITA]\n")
            else:
                print("  Resultado: [REJEITA]\n")

        # Controla a saída do loop externo baseado na escolha do usuário
        if comando_global == 'sair':
            break
        elif comando_global == 'novo':
            continue


main()