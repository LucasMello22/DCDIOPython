print(1+10) #Int
print(1.5+1+0.5) #Float
print(True) #Boorlean
print(False)
print("Python") #String

# Olá, iniciando estudos em Python
idade, name= (23, "Lucas Mello")
# idade = 23
# name = "Lucas Mello"
print("Hello World!")
print(f'Meu nome é {name} e eu tenho {idade} anos de idade')

limite_saque_diario = 1000 # utilizar padrão snack_case

BRAZILIAN_STATES = ["SP", "RJ", "PE"] # Constantes escritas com letra maiscula no inicio
print(BRAZILIAN_STATES)

## CONVERTENDO DADOS ##
preco = 10
print(preco)
# int para float #
preco = float(preco)
print(preco)
print(preco/2)
# float para int #
preco = int(preco)
print(preco)
print(preco/2)
# int/float para str #
preco = 10.50
idade = 28
print(str(preco))
texto = f"idade {idade} preco {preco}" # f' é utilizado para dizer que haverá variaveis dentro da Str
print(texto)
# str para int/float #
print(float(preco))
# para saber o tipo #
print(type(preco))