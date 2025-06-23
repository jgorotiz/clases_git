
import random as rd

dado = rd.randint(1,6)
print(f"El dado salio {dado}")


#palabra = input("Ingrese una palabra: ")

#for letra in palabra:
#    print(letra)


"""numero_adivinar = rd.randint(1,50)
print(numero_adivinar)

intentos = 3

while intentos >= 1:
    numero = int(input("Ingrese un numero: "))
    if numero > numero_adivinar:
        print("El numero es menor")
    elif numero < numero_adivinar:
        print("El numero es mayor")
    elif numero == numero_adivinar:
        print("ACERTO")
    intentos-=1
    

primer_dado =  rd.randint(1,6)
segundo_dado = rd.randint(1,6)

print(f"Primer dado {primer_dado}")
print(f"Segundo  dado {segundo_dado}")

if (primer_dado+segundo_dado) % 2 == 0:
    print("El resultado es par")
else:
    print("El resultado es impar")

"""
## "Hola mundo".split() --> ["Hola","mundo"]

file = open("texto.txt","r")
lineas = file.readlines()
print(lineas)
print(f"Mi archivo contiene {len(lineas)} lineas")
cant_palabras = 0
for linea in lineas:
    cant_palabras += len(linea.split())
print(f"la cantidad de palabras {cant_palabras}")
cont_caracteres = 0
for linea in lineas :
    cont_caracteres += len(linea)

print(cont_caracteres)

file.close()

file = open("tareas.txt","w")
tareas =["Cocinar","Tender la cama","Lavar ropa","trapear"]

for tarea in tareas:
    file.write(tarea+"\n")







