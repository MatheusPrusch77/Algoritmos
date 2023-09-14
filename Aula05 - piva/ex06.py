x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))


if x == y == z:
    print("Seu triangulo é Equilatero")
elif x != y != z:
    print("Seu triangulo é Escaleno")
elif x == z != y or y == z != x or x == y != z:
    print("Seu triangulo isosceles")

else:
    print("os lados nao formam um triangulo")

