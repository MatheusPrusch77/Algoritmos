data = (input("Digite uma data no formato dd/mm/aaaa: "))
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

data2 = ano+mes+dia
print(f"{ano}{mes}{dia}")

