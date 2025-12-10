def entrada():
    print("\n1 - Ver Categorias")
    print("2 - Pesquisar")
    print("3 - Sair")
    opc = input("\nEscolha uma opção: ")
    if opc == "1":
        categorias()
    elif opc == "2":
        pesquisar()
    elif opc == "3":
        print("Até mais!")
    else:
        print("Opção Inválida! Tente novamente")
        entrada()

def categorias():
    print("\n1 - Mercearia")
    print("2 - Limpeza")
    print("3 - Frutas e Verduras")
    print("4 - Bebidas")
    print("5 - Frios e Laticínios")
    print("6 - Padaria e Doces")
    print("7 - Congelados")
    print("8 - Voltar")
    opc = int(input("\nEscolha uma categoria: "))
    if opc == 1:
        print(produtos_mercearia)
        escolha = input("\nDigite um produto desta lista: ")
        compra_mercearia(escolha)
    elif opc == 2:
        print(produtos_limpeza)
        escolha = input("\nDigite um produto desta lista: ")
        compra_limpeza(escolha)
    elif opc == 3:
        print(produtos_frutas)
        escolha = input("\nDigite um produto desta lista: ")
        compra_frutas(escolha)
    elif opc == 4:
        print(produtos_bebidas)
        escolha = input("\nDigite um produto desta lista: ")
        compra_bebidas(escolha)
    elif opc == 5:
        print(produtos_frios)
        escolha = input("\nDigite um produto desta lista: ")
        compra_frios(escolha)
    elif opc == 6:
        print(produtos_padaria)
        escolha = input("\nDigite um produto desta lista: ")
        compra_padaria(escolha)
    elif opc == 7:
        print(produtos_congelados)
        escolha = input("\nDigite um produto desta lista: ")
        compra_congelados(escolha)
    elif opc == 8:
        entrada()
    else:
        print("Opção Inválida! Tente novamente")
        categorias()

def pesquisar():
    escolha = input("\nDigite o produto: ")
    if escolha in produtos_mercearia:
        print("Seu produto está na categoria Mercearia")
        compra_mercearia(escolha)
    elif escolha in produtos_limpeza:
        print("Seu produto está na categoria Limpeza")
        compra_limpeza(escolha)
    elif escolha in produtos_frutas:
        print("Seu produto está na categoria Frutas e Verduras")
        compra_frutas(escolha)
    elif escolha in produtos_bebidas:
        print("Seu produto está na categoria Bebidas")
        compra_bebidas(escolha)
    elif escolha in produtos_frios:
        print("Seu produto está na categoria Frios e Laticínios")
        compra_frios(escolha)
    elif escolha in produtos_padaria:
        print("Seu produto está na categoria Padaria e Doces")
        compra_padaria(escolha)
    elif escolha in produtos_congelados:
        print("Seu produto está na categoria Congelados")
        compra_congelados(escolha)
    elif escolha == "Voltar":
        entrada()
    else:
        print("Produto não encontrado no estabelecimento")
        pesquisar()

def compra_mercearia(escolha):
    qtd = float(input("Digite a quantidade (Kg, g, litro): "))
    total = preços_mercearia[produtos_mercearia.index(escolha)]*qtd
    print(f"O valor do {escolha} é {total}")
    valor_total.append(total)
    itens_total.append(escolha)
    print(itens_total)
    continuar_compra()

def compra_limpeza(escolha):
    qtd = float(input("Digite a quantidade (Kg, g, litro): "))
    total = preços_limpeza[produtos_limpeza.index(escolha)]*qtd
    print(f"O valor do {escolha} é {total}")
    valor_total.append(total)
    itens_total.append(escolha)
    continuar_compra()

def compra_frutas(escolha):
    qtd = float(input("Digite a quantidade (Kg, g, litro): "))
    total = preços_frutas[produtos_frutas.index(escolha)]*qtd
    print(f"O valor do {escolha} é {total}")
    valor_total.append(total)
    itens_total.append(escolha)
    continuar_compra()

def compra_bebidas(escolha):
    qtd = float(input("Digite a quantidade (Kg, g, litro): "))
    total = preços_bebidas[produtos_bebidas.index(escolha)]*qtd
    print(f"O valor do {escolha} é {total}")
    valor_total.append(total)
    itens_total.append(escolha)
    continuar_compra()

def compra_frios(escolha):
    qtd = float(input("Digite a quantidade (Kg, g, litro): "))
    total = preços_frios[produtos_frios.index(escolha)]*qtd
    print(f"O valor do {escolha} é {total}")
    valor_total.append(total)
    itens_total.append(escolha)
    continuar_compra()

def compra_padaria(escolha):
    qtd = float(input("Digite a quantidade (Kg, g, litro): "))
    total = preços_padaria[produtos_padaria.index(escolha)]*qtd
    print(f"O valor do {escolha} é {total}")
    valor_total.append(total)
    itens_total.append(escolha)
    continuar_compra()

def compra_congelados(escolha):
    qtd = float(input("Digite a quantidade (Kg, g, litro): "))
    total = preços_congelados[produtos_congelados.index(escolha)]*qtd
    print(f"O valor do {escolha} é {total}")
    valor_total.append(total)
    itens_total.append(escolha)
    continuar_compra()

def carrinho():
    print(f"\nO seu carrinho possui: {itens_total}")
    print(f"Os valores são: {valor_total}")
    print("\n1 - Remover item")
    print("2 - Finalizar compra")
    print("3 - Voltar")
    opc = int(input("\nEscolha uma opção: "))
    if opc == 1:
        remover = input("\nDigite o item para remover: ")
        if remover in itens_total:
            valor_total.pop(itens_total.index(remover))
            itens_total.remove(remover)
            carrinho()
        else:
            print("Item não encontrado")
            carrinho()
    elif opc == 2:
        conta = sum(valor_total)
        print(f"Seus itens são: \n{itens_total}")
        print(f"O valor total é de R${conta}")
        print("\nCompra finalizada! Até mais")
    elif opc == 3:
        entrada()
    else:
        print("Opção Inválida! Tente novamente")
        carrinho()

def continuar_compra():
    print("\n1 - Continuar compra")
    print("2 - Terminar compra")
    opc = int(input("\nEscolha uma opção: "))
    if opc == 1:
        entrada()
    elif opc == 2:
        carrinho()
    else:
        print("Opção Inválida! Tente novamente")
        continuar_compra()


produtos_mercearia = ["Arroz", "Feijão", "Açúcar", "Açúcar refinado", "Café", "Chá", "Achocolatado", "Leite", "Fermento", "Macarrão", "Molho de tomate", "Extrato de tomate", "Leite condensado", "Creme de leite", "Azeite", "Vinagre", "Sal"]

produtos_limpeza = ["Detergente", "Desinfetante", "Água sanitária", "Sabão em pó", "Amaciante", "Álcool", "Papel toalha", "Guardanapo", "Papel higiênico", "Shampoo", "Condicionador", "Sabonete", "Desodorante", "Creme dental", "Escova de dente"]

produtos_frutas = ["Alface", "Repolho", "Vagem", "Tomate", "Pepino", "Cebola", "Batata doce", "Batata", "Cenoura", "Chuchu", "Limão", "Banana"]

produtos_bebidas = ["Água mineral", "Refrigerante", "Suco", "Cerveja", "Vinho"]

produtos_frios = ["Leite", "Manteiga", "Iogurte", "Requeijão", "Queijo", "Queijo muçarela", "Presunto"]

produtos_padaria = ["Bolo", "Torta", "Torta doce", "Salgadinhos", "Pão", "Pão doce", "Bolacha", "Salgados", "Sanduíche"]

produtos_congelados = ["Bife", "Carne moída", "Carne de frango", "Carne de porco", "Presunto (fatiado)", "Mussarela", "Salsicha", "Linguiça"]

preços_mercearia = [7.00, 9.00, 5.00, 5.50, 18.00, 8.00, 12.00, 6.00, 2.00, 4.00, 4.50, 5.00, 7.00, 4.50, 25.00, 4.50, 3.00]

preços_limpeza = [5.00, 6.00, 7.00, 12.00, 10.00, 6.00, 8.00, 5.00, 10.00, 15.00, 15.00, 4.00, 12.00, 8.00, 7.00]

preços_frutas = [4.00, 8.00, 10.00, 10.00, 3.50, 7.00, 6.00, 5.50, 6.00, 5.00, 7.00, 10.00]

preços_bebidas = [2.50, 10.00, 8.00, 5.00, 40.00]

preços_frios = [6.00, 12.00, 5.00, 7.00, 8.00, 9.00, 6.00]

preços_padaria = [20.00, 25.00, 25.00, 8.00, 12.00, 3.50, 6.00, 4.00, 15.00]

preços_congelados = [45.00, 30.00, 20.00, 25.00, 10.00, 18.00, 20.00, 22.00]

valor_total = []

itens_total = []

print("Bem-Vindo(a) ao mercado de Diadema")
entrada()