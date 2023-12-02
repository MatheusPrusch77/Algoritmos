import math
from math import pi, pow
num = int(input("Digite o raio: "))
def volume(num):
    vol = (4/3) * pi * pow(num, 3)
    return vol
volume(num)
print(volume(num))
