print("Cadastro do Cliente")
clientes = []

def cadastro_cliente(nome, telefone, email):
    nome = nome.strip()
    if not nome:
        print("O nome não pode ser vazio.")
        return
    telefone = telefone.strip()
    if not telefone:
        print("O telefone não pode ser vazio.")
        return
    email = email.strip()

    id_cliente = len(clientes) + 1
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    cliente["id"] = id_cliente
    clientes.append(cliente)
    return(f"Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    print("\n----Lista de Clientes----")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"{i}. ID: {cliente['id']}, Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")

def solicitar_cadastro_cliente():
    while True:
            try:
                nome = input("Digite o nome do cliente: ").strip()
                if not nome:
                    print("O nome não pode ser vazio. Tente novamente.")
                    continue
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("O nome deve conter somente letras.")
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um nome válido.")
    
    while True:
            try:
                telefone = input("Digite o telefone do cliente: ").strip()
                if not telefone:
                    print("O telefone não pode ser vazio. Tente novamente.")
                    continue
                if not telefone.isascii() or not telefone.isdigit():
                    raise ValueError("O telefone deve conter somente números.")
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um telefone válido.")
    
    email = input("Digite o email do cliente: ").strip()
    

while True:
    print("\n1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome, telefone, email = solicitar_cadastro_cliente()
        resultado = cadastro_cliente(nome, telefone, email)
        print(resultado)
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")