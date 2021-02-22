"""
Escribir un programa que tenga como input 10 numeros positivos de 3 digitos, y como output liste los que son capicuas,
 
ordenandolos de menor a mayor
"""
lista=[]
resultado=[]
n_max = 10
contador = 1
indice1= 1
indice2= 1
while contador <= n_max : 
    print("Ingrese el numero con orden " + str(contador))
    n = input()
    if int(n) <= 0:
        print("Error , no puede ingresar numeros negativos o 0")
        break
    else:
        lista.append(int(n))
        contador += 1 
"""
for i in lista:
    indice2=1
    for x in lista : 
        if indice1 == indice2:
            indice2+=1
            pass
        else:
            if str(i) == str(x)[::-1]:
                resultado.append(i)
            indice2+=1
    indice1 +=1 

resultado2=set(resultado)
"""
for i in lista:
    if str(i) == str(i)[::-1]:
        resultado.append(i)

for y in resultado:
    print("El numero " + str(y) + " Es Capicua \n")


