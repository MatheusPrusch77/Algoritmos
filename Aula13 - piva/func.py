def multiplicar(x, y):
    multi = x * y
    return multi

def primo(num):
    for i in range(1, num):
        if (num % i) == 0:
            return False
    return True