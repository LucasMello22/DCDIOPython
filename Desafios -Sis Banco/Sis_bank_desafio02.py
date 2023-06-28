class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaCorrente:
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0

    def sacar(self, valor):
        if self.saldo >= valor and self.saques_diarios < 3 and valor <= 500:
            self.saldo -= valor
            self.extrato.append(f"Saque: -{valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif self.saques_diarios >= 3:
            print("Limite diário de saques atingido.")
        elif valor > 500:
            print("Limite máximo de R$ 500,00 por saque.")
        else:
            print("Saldo insuficiente para saque.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +{valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def visualizar_extrato(self):
        if self.extrato:
            print("Extrato:")
            for movimento in self.extrato:
                print(movimento)
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    usuario = Usuario(nome, cpf)
    return usuario

def criar_conta_corrente(usuario):
    conta = ContaCorrente(usuario)
    return conta

def menu():
    usuario = criar_usuario()
    conta = None

    while True:
        print("\n----- MENU -----")
        print("1. Cadastrar Conta Corrente")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Visualizar Extrato")
        print("5. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            if conta is None:
                conta = criar_conta_corrente(usuario)
                print("Conta corrente cadastrada com sucesso.")
            else:
                print("Conta corrente já cadastrada.")
        elif opcao == "2":
            if conta is not None:
                valor_saque = float(input("Digite o valor a sacar: "))
                conta.sacar(valor_saque)
            else:
                print("Conta corrente não cadastrada.")
        elif opcao == "3":
            if conta is not None:
                valor_deposito = float(input("Digite o valor a depositar: "))
                conta.depositar(valor_deposito)
            else:
                print("Conta corrente não cadastrada.")
        elif opcao == "4":
            if conta is not None:
                conta.visualizar_extrato()
            else:
                print("Conta corrente não cadastrada.")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Digite novamente.")

menu()
