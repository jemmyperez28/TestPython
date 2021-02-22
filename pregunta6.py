"""Crear una funcion que determine si dado una serie de parentesis, estas se encuentran en pares, es decir,"""
def mi_funcion(entrada="",*args):
    izq=entrada.count(')')
    der=entrada.count('(')
    if izq == der: 
        return True
    else:
        return False

rpta=mi_funcion('))(((')
print(rpta)
