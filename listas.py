listas = [1,2,3,4,5,6,6,6,6]

lista_mezclada = [1,"Hola",5.2,["python",5]]

listas.append(50)
print(listas)

listas.extend([100,101,102])
print(listas)

listas.remove(50)
print(listas)

listas.pop()
print(listas)

print(listas.index(100))


print(listas.count(6))

print(len(listas))

print(max(listas))
print(min(listas))


lista_copia *= 2
print(lista_copia)

lista_cuadrado = []

for i in range(len(lista)):
    lista_cuadrado.append(lista[i]**2)
print(lista_cuadrado)

# promedio de mi lista

suma = sum(lista)
elementos = len(lista)
promedio = suma/elementos
print(promedio)


palabras = ["hola", "mundo", "Python", "programación"]
longitud = 5
lista_longitd = []

for i in range(len(palabras)):
    if len(palabras[i] ) >= longitud:
        lista_longitd.append(palabras[i])
print(lista_longitd)