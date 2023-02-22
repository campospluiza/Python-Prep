#1A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1. 
numeros = []
counter = -15
while counter >= -1:
    numeros.append(counter)
    counter -= 1
print(numeros)

#2 Sí, es posible recorrer la lista numbers para imprimir sólo los números pares utilizando un ciclo while. Aquí está un ejemplo:
counter = 0
while counter < len(numeros):
    if numeros[counter] % 2 == 0:
        print(numeros[counter])
    counter += 1

#3 Resolver el punto anterior sin utilizar un ciclo while
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
for number in numeros_pares:
    print(number)

#4 Utilizar el iterable para recorrer sólo los primeros 3 elementos
for i in range(3):
    print(numeros[i])

#5 Utilizar la función enumerate para obtener dentro del iterable, también el índice que corresponde al elemento
for index, number in enumerate(numeros):
    print(index, number)

#6 Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
lista = [1,2,5,7,8,10,13,14,15,17,20]
nueva_lista = []
i = 1
while i <= 20:
    if i not in lista:
        nueva_lista.append(i)
    i += 1
print(nueva_lista)

#7 2 - La sucesión de Fibonacci es un listado de números que sigue la fórmula:
#n0 = 0
#n1 = 1
#ni = ni-1 + ni-2
#Crear una lista con los primeros treinta números de la sucesión.
sucesion_fibonacci = [0, 1]
while len(sucesion_fibonacci) < 30:
    n = sucesion_fibonacci[-1] + sucesion_fibonacci[-2]
    sucesion_fibonacci.append(n)
print(sucesion_fibonacci)

#8 Realizar la suma de todos los elementos del punto anterior
suma = sum(sucesion_fibonacci)
print(suma)

#9 La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:
print(sucesion_fibonacci[-1] / sucesion_fibonacci[-2])
print(sucesion_fibonacci[-2] / sucesion_fibonacci[-3])
print(sucesion_fibonacci[-3] / sucesion_fibonacci[-4])
print(sucesion_fibonacci[-4] / sucesion_fibonacci[-5])
print(sucesion_fibonacci[-5] / sucesion_fibonacci[-6])

#10 A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
posiciones = [i for i, caracter in enumerate(cadena) if caracter == 'n']
print(posiciones)

#11  Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
lista_cadena = list(cadena)
for caracter in lista_cadena:
    print(caracter)

#12Crear dos listas y unirlas en una tupla utilizando la función zip
lista_numeros = [1,2,3,4,5]
lista_letras = ['A','B','C','D','E']
lista_unida = list(zip(lista_numeros, lista_letras))
print(lista_unida)

#13 A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7
#lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
nueva_lista2 = [num for num in lis if num % 7 == 0]
print(nueva_lista2)

#14 A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:
#lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
count = 0
for elemento in lis:
    if type(elemento) == list:
        count += len(elemento)
    else:
        count += 1
print(count)

#15 Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es:
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lista_final = []
for elemento in lis:
    if type(elemento) != list:
        lista_final.append([elemento])
    else:
        lista_final.append(elemento)
print(lista_final)
