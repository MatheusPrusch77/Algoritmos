lista = []

for i in range(5):
    lista.append(int(input(f"Insira o número {i + 1}: ")))
maior = max(lista)
pos = 0
for i in range(0, len(lista)):
    if lista[i] >= maior:
        maior = lista[i]
        pos = i

print(f"O maior elemento é {maior} e a sua posição na lista é {pos}")


