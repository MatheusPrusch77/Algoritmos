from func import primo
i = 0
num = int(input("Digite seu numero: "))
while num < 0:
    print("Seu numero precisa ser maior que zero!")
    num = int(input("Digite seu numero: "))
def qtd_primos(num):
    qtd = 0
    for i in range(1, num+1):
        if primo(i):
            qtd = qtd + 1
    return qtd

print(f"A quantidade de numeros primos é {num}")

print(f"A quantidade de numeros primos é {qtd_primos(num)}")
