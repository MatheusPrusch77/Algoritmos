largura = float(input("Digite a largura do aposento em metros: "))
comprimento = float(input("Digite o comprimento do aposento em metros: "))
lata = float(input("Digite a quantidade de litros da lata de tinta: "))

altura_teto = 2.80
area_paredes = 2 * (largura + comprimento) * altura_teto

area_porta = 0.80 * 2.10
area_paredes -= area_porta

litros_necessarios = area_paredes / 3  
quantidade_latas = litros_necessarios / lata

print(f"Quantidade de latas de tinta necessárias: {quantidade_latas:.2f} latas")


