dicionario = {}
maior_sobrenome = ""
maior_idade = 0
for i in range(5):
    chave = str(input(f"Digite seu {i +1} sobrenome: "))
    valor = int(input(f"Digite sua {i +1} idade: "))
    dicionario[chave] = valor

print(f"Seu dicionário é {dicionario} e o maior valor é {max(dicionario)}")

for chave, valor in dicionario.items():
    if valor > maior_idade:
        maior_idade = valor
        maior_sobrenome = chave
print(f"a maior idade {maior_sobrenome}")
