# Listem tem a capacidade de armazenar qualquer tipo de objeto (Como um ARRAY)

#Criando com padrão '["","",""]"
frutas = ["laranja", "maca", "uva"]
print(frutas)
#Criando uma lista vazia
frutas = []
print(frutas)

#Criando com construtor reservado 'list'
#neste caso, cada letra é uma parte, como uma string, ou seja, letra[0] = p, letra[1] =y ...
letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# indices negativos, basicamente é a escola dos elementos de maneira decrescente (esquerda para direita)
frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja

#Construindo uma matriz e chamando
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

#Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

#Exemplo
carros =["gol","palio", "celta"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}:{carros}")

#Filtro
numeros =[1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros)
print(pares)

#Modificando valores
quadrados = [numero ** 2 for numero in numeros]
print(quadrados)