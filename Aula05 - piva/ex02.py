nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
nota_exame = 0
if media < 3.0:
    resultado = "Reprovado!"

else:
    if media < 7:
        resultado = "Exame"
        nota_exame = 12 - media
    else:
        resultado = "Aprovado"

print(f"Média {media:5.2f} - {resultado}!")
if nota_exame != 0:
    print(f"tem que tirar no minimo {nota_exame:5.2f}")



