compra = float(input("Digite aqui o valor da sua compra e descubra seu desconto!: "))

if compra == 1000.00:
    print("Parabéns! Você recebeu um desconto de 10%!!")
elif compra == 1001.00 or compra <= 5000.00:
    print("Parabéns! Você recebeu um desconto de 20%!!")
elif compra > 5000.00:
    print("Parabéns!! Você recebeu um super desconto de 30%!!")
else:
    print("Você não recebeu nenhum desconto! :c")

