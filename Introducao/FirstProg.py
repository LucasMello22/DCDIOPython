# input é a função para ler dados de entreda (teclado) #
nome = input("informe o seu nome: ")

print(f"Seu nome é {nome}!")

quantidade_notas = int(input("Digite a quantidade de notas: "))
notas = []

for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
media = sum(notas) / quantidade_notas


print("A média das notas é:", media)