"""Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: los 5 mas bajos y los 5 mas altos"""
import random 
numeros = []

for i in range(0,10):
    x = random.randint(1,1000)
    numeros.append(x)
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
tamano = len(numeros_ordenados)
medio = tamano//2

mitad1 = numeros_ordenados[:medio]
respuesta1 = sum(mitad1)
print(respuesta1)

mitad2 = numeros_ordenados[medio:]
respuesta2 = sum(mitad2)
print(respuesta2)

