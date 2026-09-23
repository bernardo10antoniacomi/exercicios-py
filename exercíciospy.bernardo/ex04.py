def mostrarAssentos(assentos):
    print("\n========== MAPA DE ASSENTOS ==========")
    print("       A   B   C   D   E   F")

    for i in range(5):
        print(f"{i + 1}      ", end="")

        for j in range(6):
            print(f"{assentos[i][j]}   ", end="")

        print()


def validarAssento(codigo):
    codigo = codigo.strip().upper()

    if len(codigo) != 2:
        return False

    if codigo[0] not in "12345":
        return False

    if codigo[1] not in "ABCDEF":
        return False

    return True


def converterAssento(codigo):
    linha = int(codigo[0]) - 1
    coluna = ord(codigo[1]) - ord("A")

    return linha, coluna


def verificarDisponibilidade(assentos, codigo):
    linha, coluna = converterAssento(codigo)

    return assentos[linha][coluna] == "L"


def calcularPreco(codigo):
    fileira = int(codigo[0])

    if fileira == 1:
        categoria = "Executiva"
        preco = 850.00

    elif fileira in [2, 3]:
        categoria = "Espaço extra"
        preco = 600.00

    else:
        categoria = "Econômica"
        preco = 400.00

    return categoria, preco


def comprarAssento(assentos, vendas):
    codigo = input("Digite o assento desejado (ex: 2C): ").strip().upper()

    if not validarAssento(codigo):
        print("Assento inválido.")
        print("Digite um assento entre 1A e 5F.")
        return

    if not verificarDisponibilidade(assentos, codigo):
        print(f"O assento {codigo} já está ocupado.")
        print("Escolha outro assento.")
        return

    categoria, preco = calcularPreco(codigo)

    print("\n===== CONFIRMAÇÃO =====")
    print(f"Assento: {codigo}")
    print(f"Categoria: {categoria}")
    print(f"Valor: R$ {preco:.2f}")

    confirmacao = input("Confirmar compra? (S/N): ").strip().upper()

    if confirmacao == "S":
        linha, coluna = converterAssento(codigo)

        assentos[linha][coluna] = "O"

        vendas.append({
            "assento": codigo,
            "categoria": categoria,
            "valor": preco
        })

        print("\nCompra realizada com sucesso!")
        print(f"O assento {codigo} agora está indisponível.")

    elif confirmacao == "N":
        print("Compra cancelada.")

    else:
        print("Resposta inválida. Compra cancelada.")


def consultarAssento(assentos):
    codigo = input("Digite o assento para consultar: ").strip().upper()

    if not validarAssento(codigo):
        print("Assento inválido.")
        return

    if verificarDisponibilidade(assentos, codigo):
        print(f"O assento {codigo} está LIVRE.")
    else:
        print(f"O assento {codigo} está OCUPADO.")


def mostrarResumo(assentos, vendas):
    ocupados = 0

    for linha in assentos:
        for assento in linha:
            if assento == "O":
                ocupados += 1

    total = 30
    livres = total - ocupados
    percentual = (ocupados / total) * 100

    faturamento = 0

    vendas_executiva = 0
    vendas_extra = 0
    vendas_economica = 0

    for venda in vendas:
        faturamento += venda["valor"]

        if venda["categoria"] == "Executiva":
            vendas_executiva += 1

        elif venda["categoria"] == "Espaço extra":
            vendas_extra += 1

        elif venda["categoria"] == "Econômica":
            vendas_economica += 1

    print("\n========== RESUMO DO VOO ==========")
    print(f"Assentos livres: {livres}")
    print(f"Assentos ocupados: {ocupados}")
    print(f"Percentual de ocupação: {percentual:.2f}%")
    print(f"Faturamento total: R$ {faturamento:.2f}")

    print("\nVendas por categoria:")
    print(f"Executiva: {vendas_executiva}")
    print(f"Espaço extra: {vendas_extra}")
    print(f"Econômica: {vendas_economica}")


def mostrarMenu():
    print("\n========== COMPANHIA AÉREA ==========")
    print("1 - Visualizar assentos")
    print("2 - Comprar assento")
    print("3 - Consultar assento")
    print("4 - Mostrar resumo do voo")
    print("5 - Encerrar")


def main():
    assentos = [
        ["L", "L", "L", "L", "L", "L"],
        ["L", "L", "L", "L", "L", "L"],
        ["L", "L", "L", "L", "L", "L"],
        ["L", "L", "L", "L", "L", "L"],
        ["L", "L", "L", "L", "L", "L"]
    ]

    vendas = []

    while True:
        mostrarMenu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrarAssentos(assentos)

        elif opcao == "2":
            comprarAssento(assentos, vendas)

        elif opcao == "3":
            consultarAssento(assentos)

        elif opcao == "4":
            mostrarResumo(assentos, vendas)

        elif opcao == "5":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


main()
