print("Cadastro do Cliente")
clientes = []

def cadastro_cliente():
    id_cliente = len(clientes) + 1
    while True:
        nome = input("Digite o nome do cliente: ").strip()
        if not nome:
            print("O nome não pode ser vazio. Tente novamente.")
            continue
        break
    while True:
        telefone = input("Digite o telefone do cliente: ").strip()
        if not telefone:
            print("O telefone não pode ser vazio. Tente novamente.")
            continue
        break
    email = input("Digite o email do cliente: ").strip()

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    cliente["id"] = id_cliente
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    print("\n----Lista de Clientes----")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. ID: {cliente['id']}, Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")  

while True:
    print("\n1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastro_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")