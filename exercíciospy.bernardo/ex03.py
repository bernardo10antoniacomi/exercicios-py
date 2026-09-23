def listarMedicamentos(nomes, precos, estoques):
    print("\n===== MEDICAMENTOS =====")

    for i in range(len(nomes)):
        print(
            f"{i + 1}. {nomes[i]} | "
            f"Preço: R$ {precos[i]:.2f} | "
            f"Estoque: {estoques[i]}"
        )


def pesquisarMedicamento(nomes, precos, estoques):
    nome = input("Digite o nome do medicamento: ").strip()

    encontrado = False

    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            print("\nMedicamento encontrado:")
            print(f"Nome: {nomes[i]}")
            print(f"Preço: R$ {precos[i]:.2f}")
            print(f"Estoque: {estoques[i]}")
            encontrado = True
            break

    if not encontrado:
        print("Medicamento não encontrado.")


def encontrarIndice(nomes, nome):
    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            return i

    return -1


def lerQuantidade():
    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            else:
                return quantidade

        except ValueError:
            print("Digite uma quantidade inteira válida.")


def registrarVenda(nomes, precos, estoques):
    nome = input("Digite o medicamento vendido: ").strip()

    indice = encontrarIndice(nomes, nome)

    if indice == -1:
        print("Medicamento não encontrado.")
        return

    quantidade = lerQuantidade()

    if quantidade > estoques[indice]:
        print("Venda não realizada.")
        print(f"Estoque disponível: {estoques[indice]}")
        return

    valor = quantidade * precos[indice]

    estoques[indice] -= quantidade

    print("\nVenda realizada com sucesso!")
    print(f"Medicamento: {nomes[indice]}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor da venda: R$ {valor:.2f}")
    print(f"Estoque restante: {estoques[indice]}")


def reporEstoque(nomes, estoques):
    nome = input("Digite o medicamento para reposição: ").strip()

    indice = encontrarIndice(nomes, nome)

    if indice == -1:
        print("Medicamento não encontrado.")
        return

    quantidade = lerQuantidade()

    estoques[indice] += quantidade

    print("Estoque atualizado com sucesso!")
    print(f"Novo estoque: {estoques[indice]}")


def verificarEstoqueBaixo(nomes, estoques):
    print("\n===== ESTOQUE BAIXO =====")

    encontrou = False

    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(f"- {nomes[i]}: {estoques[i]} unidades")
            encontrou = True

    if not encontrou:
        print("Nenhum medicamento está com estoque baixo.")


def mostrarMenu():
    print("\n===== FARMÁCIA =====")
    print("1 - Listar medicamentos")
    print("2 - Pesquisar medicamento")
    print("3 - Registrar venda")
    print("4 - Repor estoque")
    print("5 - Mostrar estoque baixo")
    print("6 - Encerrar")


def main():
    nomes = [
        "Dipirona",
        "Paracetamol",
        "Loratadina",
        "Ibuprofeno",
        "Amoxicilina"
    ]

    precos = [
        12.50,
        9.90,
        18.75,
        15.00,
        25.50
    ]

    estoques = [
        20,
        15,
        8,
        3,
        2
    ]

    while True:
        mostrarMenu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listarMedicamentos(nomes, precos, estoques)

        elif opcao == "2":
            pesquisarMedicamento(nomes, precos, estoques)

        elif opcao == "3":
            registrarVenda(nomes, precos, estoques)

        elif opcao == "4":
            reporEstoque(nomes, estoques)

        elif opcao == "5":
            verificarEstoqueBaixo(nomes, estoques)

        elif opcao == "6":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Escolha entre 1 e 6.")


main()
