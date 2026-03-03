import csv

# Lista para armazenar os dados dos clientes
clientes = []

def adicionar_cliente(nome, idade, email):
    cliente = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    clientes.append(cliente)
    print("=========================================")
    print("Cliente cadastrado com sucesso!")
    print("=========================================")

def listar_clientes():
    if not clientes:
        print("=========================================")
        print("Nenhum cliente cadastrado.")
        print("=========================================")
    else:
        print("=========== Lista de Clientes ===========")
        for cliente in clientes:
            print(f"\nNome: {cliente['nome']}\nIdade: {cliente['idade']}\nEmail: {cliente['email']}")
        print("=========================================")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente["email"] == email:
            return cliente
    return None

def exportar_csv(nome_arquivo="clientes.csv"):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        # Cabeçalho
        escritor.writerow(["Nome", "Idade", "Email"])
        # Dados
        for cliente in clientes:
            escritor.writerow([cliente["nome"], cliente["idade"], cliente["email"]])
    print("=====================================================")
    print(f"Dados exportados para {nome_arquivo} com sucesso!")
    print("=====================================================")

# Menu para interagir com o sistema de cadastro de clientes
while True:
    print("\n----- MENU -----")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Exportar clientes para CSV")
    print("5 - Sair")
    print("----------------")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        print("=========================================")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")
        print("=========================================")
        adicionar_cliente(nome, idade, email)

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        print("=========================================")
        email = input("Digite o email do cliente: ")
        resultado = buscar_cliente(email)
        print("=========================================")

        if resultado:
            print("=========== Cliente encontrado ===========")
            print(f"Nome: {resultado['nome']}")
            print(f"Idade: {resultado['idade']}")
            print(f"Email: {resultado['email']}")
            print("=========================================")
        else:
            print("===================!!!!!==================")
            print("Cliente não encontrado")
            print("===================!!!!!==================")

    elif opcao == "4":
        exportar_csv()

    elif opcao == "5":
        print("=========================================")
        print("Saindo do sistema...")
        print("=========================================")
        break

    else:
        print("===================!!!!!==================")
        print("Opção inválida!")
        print("===================!!!!!==================")
