import datetime

idade = int(input("digite sua idade: "))
dia = int(input("digite seu dia de nascimento: "))
mes = int(input("digite o mes do seu aniversario: "))



mesatual = datetime.datetime.now().month
anoatual = datetime.datetime.now().year
nasc = anoatual - idade
meses = idade * 12
dias = idade * 365
semanas = idade * 52

print("Voce nasceu em ", nasc, "sua idade em meses é: ", meses, "sua idade em dias é: ",dias,"e sua idade em semanas é:", semanas )
