s_peso = 0
s_altura = 0
maior_imc = 0
menor_imc = 0
for i in range(1, 6):
    peso = float(input(f"Pessoa {i} Peso: "))
    altura = float(input(f"Pessoa {i}: Altura: "))
    s_peso = s_peso + peso
    s_altura = s_altura + altura
    imc = peso / (altura * altura)
    if i == 1:
        maior_imc = imc
        menor_imc = imc
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
    media_peso = s_peso / 5
    media_altura = s_altura / 5
    print(f"O peso médio..: {media_peso:5.2f}")
    print(f"A altura média..: {media_altura:5.2f}")
    print(f"O maior imc é..: {maior_imc:5.2f}")
    print(f"o menor imc é..: {menor_imc:5.2f}")
