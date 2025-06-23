for numero in range (10):
    print(numero)


## sumar todos los numero del 1 al 100
suma = 0 
for i in range(1,101):
    suma += i ## suma = suma + i 
print(suma)


## mostrar tabla de multiplicar
## dado un numero presentar la tabla de multiplicar del 1 al 10 de ese numero

numero = 5

for i in range(1, 11):
    multiplicaicon = numero * i
    print(multiplicaicon)


# imprimir todos los numero pares entre el 1 y 50

for i in range(0,51):
    if i %  2 == 0:
        print(i)


# obtener el factorial de un numero
# 5! = 5 * 4 * 3 *2 *1

numero = 5
factorial = 1
for i in range(numero, 1,-1):
    factorial *= i
print(factorial)

## mostrar todos los numeros primos entre el 1 y el 100
## 20 / 5 = 4 
## 20 % 5 = 0
print("NUMEROS PRIMOS")
for i in range(1,101): # 10
    divisores = 0
    for j in range(1,i+1): # [1,2,3,4,5,6,7,8,9,10,11]
        if i % j == 0:
            divisores += 1
    if divisores == 2:
        print(i)