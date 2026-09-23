def registrarTentativas():
    tentativas = []

    for i in range(10):
        while True:
            try:
                resultado = int(
                    input(f"Digite o resultado da tentativa {i + 1} (0, 1, 2 ou 3): ")
                )

                if resultado not in [0, 1, 2, 3]:
                    print("Valor inválido! Digite somente 0, 1, 2 ou 3.")
                else:
                    tentativas.append(resultado)
                    break

            except ValueError:
                print("Digite um número inteiro válido.")

    return tentativas


def calcularPontuacao(tentativas):
    return sum(tentativas)


def calcularAproveitamento(tentativas):
    convertidos = 0

    for tentativa in tentativas:
        if tentativa > 0:
            convertidos += 1

    return (convertidos / len(tentativas)) * 100


def encontrarCestaMaisFrequente(tentativas):
    quantidade_1 = tentativas.count(1)
    quantidade_2 = tentativas.count(2)
    quantidade_3 = tentativas.count(3)

    maior = max(quantidade_1, quantidade_2, quantidade_3)

    tipos = []

    if quantidade_1 == maior:
        tipos.append("Cesta de 1 ponto")

    if quantidade_2 == maior:
        tipos.append("Cesta de 2 pontos")

    if quantidade_3 == maior:
        tipos.append("Cesta de 3 pontos")

    return tipos


def mostrarRelatorio(tentativas):
    pontuacao = calcularPontuacao(tentativas)
    aproveitamento = calcularAproveitamento(tentativas)

    convertidos = 0
    errados = 0

    for tentativa in tentativas:
        if tentativa == 0:
            errados += 1
        else:
            convertidos += 1

    mais_frequente = encontrarCestaMaisFrequente(tentativas)

    print("\n===== RELATÓRIO =====")
    print(f"Tentativas: {tentativas}")
    print(f"Pontuação total: {pontuacao}")
    print(f"Arremessos convertidos: {convertidos}")
    print(f"Arremessos errados: {errados}")
    print(f"Aproveitamento: {aproveitamento:.2f}%")

    print("Tipo de cesta mais frequente:")
    for tipo in mais_frequente:
        print(f"- {tipo}")


def main():
    print("===== ARREMESSOS DE BASQUETE =====")

    tentativas = registrarTentativas()

    mostrarRelatorio(tentativas)


main()
