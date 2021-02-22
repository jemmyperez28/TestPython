"""Desarrollar una funcion que me devuelva el n-esimo fibonacci"""
numero = 9

def devolver_fib(n):
    x = 0
    numero_siguiente = 1
    numero_actual = 1
    numero_anterior = 0

    while x < numero:
        numero_siguiente = numero_actual + numero_anterior
        numero_actual = numero_anterior
        numero_anterior = numero_siguiente
        x = x + 1

    return numero_siguiente

print(devolver_fib(numero))