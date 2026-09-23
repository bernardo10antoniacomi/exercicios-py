def calcularTotalGols(gols):
    return sum(gols)


def calcularMediaGols(gols):
    return calcularTotalGols(gols) / len(gols)


def encontrarArtilheiros(jogadores, gols):
    maior_gols = max(gols)
    artilheiros = []

    for i in range(len(jogadores)):
        if gols[i] == maior_gols:
            artilheiros.append(jogadores[i])

    return artilheiros


def mostrarRelatorio(jogadores, gols):
    print("\n===== RELATÓRIO DO TIME =====")

    for i in range(len(jogadores)):
        print(f"{jogadores[i]}: {gols[i]} gols")

    total = calcularTotalGols(gols)
    media = calcularMediaGols(gols)
    artilheiros = encontrarArtilheiros(jogadores, gols)

    print(f"\nTotal de gols: {total}")
    print(f"Média de gols: {media:.2f}")

    print("\nJogadores acima da média:")
    encontrou = False

    for i in range(len(jogadores)):
        if gols[i] > media:
            print(f"- {jogadores[i]} ({gols[i]} gols)")
            encontrou = True

    if not encontrou:
        print("Nenhum jogador marcou acima da média.")

    print("\nArtilheiro(s):")
    for jogador in artilheiros:
        print(f"- {jogador}")

    if len(artilheiros) > 1:
        print("Houve empate na artilharia.")
    else:
        print("Não houve empate na artilharia.")


def lerGols():
    gols = []

    for i in range(5):
        while True:
            try:
                quantidade = int(input(f"Digite os gols do jogador {i + 1}: "))

                if quantidade < 0:
                    print("A quantidade de gols não pode ser negativa.")
                else:
                    gols.append(quantidade)
                    break

            except ValueError:
                print("Digite um número inteiro válido.")

    return gols


def main():
    jogadores = [
        "Lucas",
        "Gabriel",
        "Rafael",
        "Pedro",
        "André"
    ]

    gols = lerGols()

    mostrarRelatorio(jogadores, gols)


main()
