"""

Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.

"""

numero = int(input("Digite um número e veja sua tabuada: "))
for c in range(1, 11):
    tabuada = numero * c
    print("{} x {:2} = {}".format(numero, c, tabuada))
