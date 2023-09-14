salario = float(input("Digite seu salário: "))
percentual = float(input("Digite o percentual de aumento: "))

novo_salario = salario * percentual / 100

print(f"Seu salário era {salario} com o aumento de {percentual}% seu salário agora é {novo_salario + salario}")