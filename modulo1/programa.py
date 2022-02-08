#programa.py
sum = 1 + 2
print(sum)

# La función print()
print('Hola desde la consola')

# Variables
sum = 1 + 2 #3
product = sum * 2
print("El producto es :"+str(product))

#Typo de dato

distancia_a_alfa_centauri = 4.367

print(distancia_a_alfa_centauri)
# Descubrimos su tipo de dato

print(type(distancia_a_alfa_centauri))

#print(date.today())
# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

#Entrada del  Usuario

print("bienvenido a al programa de bienvenida")
name = input("Inroduzca su nombre: ")
print("Saludos:" + name)

#Trabajar con números
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
#print(first_number + second_number)
print(int(first_number)+ int(second_number))

