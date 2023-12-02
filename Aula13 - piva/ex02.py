num = int(input("Digite seu numero: "))
def primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
if primo(num):
    print("é primo")
else:
    print("nao é primo")
