lista = []

for i in range(5):
    lista.append(int(input(f"Insira o número {i + 1}: ")))

    maior= sorted(lista, reverse=True)[0]
    pos = lista.index(maior)
print(f"O maior número é o {maior} e esta localizado na posição {pos}")

