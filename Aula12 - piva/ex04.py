lista1, lista2 = [], []

for c in range(5):
    ele1 = int(input(f"Digite seu {c + 1} elemento:"))
    ele2 = int(input(f"Digite outro {c +1} elemento: "))
    lista1.append(ele1)
    lista2.append(ele2)
uniao = set(lista1+lista2)
#uniao = set(lista1).union(lista2)
print(f"A união das listas é {uniao}")
