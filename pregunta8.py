"""Hacer un programa que genere un array y que imprima los numeros que no son iguales"""
import random 

array_lenght = random.randint(50,100)
lista = []
x=1
while x <= array_lenght:
    numero_alea = random.randint(1,30)
    lista.append(numero_alea)
    x = x + 1 
print("Array Generado : \n" + str(lista))

#unicos
unicos = set(lista)
print("valores unicos : \n" + str(unicos))

            