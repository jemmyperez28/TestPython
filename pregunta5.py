""" Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. """ 
#numeros=[1,2,3,4]
#suma=sum(numeros)
#print(suma)

#resultado=1 
#for x in numeros: 
#    resultado=resultado*x 
#print(resultado)

def suma(lista=[],*args):
    suma=sum(lista)
    return suma
instancia1=suma([1,2,3,4])
print(instancia1)

def multip(lista=[],*args):
    res = 1
    for i in lista:
        res = res * i
    return res 

instancia2=multip([1,2,3,4])
print(instancia2)



