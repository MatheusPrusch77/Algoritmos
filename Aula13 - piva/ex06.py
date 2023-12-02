hora = int(input("Digite suas horas: "))
minuto = int(input("Digite seus minutos: "))
segundo = int(input("Digite seus segundos: "))

def conversao(hora, minuto,segundo):
    conv = (hora * 3600) + (minuto * 60) + segundo
    return conv

print(f"em segundos a hora é {conversao(hora, minuto, segundo)}")

