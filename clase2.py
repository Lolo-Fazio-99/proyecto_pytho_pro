import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Longitud = int(input("ingrese la longitud de la contraseña: "))
contrasena = ""
for i in range (Longitud):
    contrasena += random.choice(caracteres)
print(contrasena)

###################

for i in range(6):
    print( "*" * i)

###################
nombre = input(int("ingrese su nombre: "))
