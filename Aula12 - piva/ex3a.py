dicionario = {}
idades = []
soma = 0
for c in range(5):
    nome = str(input(f"Digite seu {c + 1} nome: "))
    idade = int(input(f"Digite sua {c +1} idade: "))
    dicionario[nome] = idade
    idades.append(idade)
    soma += idade

media = soma / 5
for nome, idade in dicionario.items():
    if idade > media:
       print(nome)

