idade = int(input("Digite sua idade "))
if 0 < idade <= 12:
    print("Crianca")
elif 12 < idade <= 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")
else:
    ("Valor Invalido")