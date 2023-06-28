
class ContaBancaria:
    def __init__(self):
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

conta = ContaBancaria()

while True:
    print("\n----- MENU -----")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Visualizar Extrato")
    print("4. Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        valor_saque = float(input("Digite o valor a sacar: "))
        conta.sacar(valor_saque)
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a depositar: "))
        conta.depositar(valor_deposito)
    elif opcao == "3":
        conta.visualizar_extrato()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Digite novamente.")
