import numpy as np
import random as rd

matriz = np.zeros((10,10),int)
print(matriz)

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j] = rd.randint(50,100)

print(matriz)

vector = np.linspace(500,300,5)
print(vector)


matriz_ordenada = np.sort(matriz,axis=None)[::-1].reshape(10,10)
print(matriz_ordenada)


cuadrante_1 = matriz_ordenada[0:5,0:5]
cuadrante_2 = matriz_ordenada[0:5,5:10]
cuadrante_3 = matriz_ordenada[5:10,0:5]
cuadrante_4 = matriz_ordenada[5:10,5:10]



promedio_cuadrante_1 = np.mean(cuadrante_1)
promedio_cuadrante_2 = np.mean(cuadrante_2)
promedio_cuadrante_3 = np.mean(cuadrante_3)
promedio_cuadrante_4 = np.mean(cuadrante_4)

print(promedio_cuadrante_1)
print(promedio_cuadrante_2)
print(promedio_cuadrante_3)
print(promedio_cuadrante_4)

subsidio_cuadrante_1 = cuadrante_1[cuadrante_1< promedio_cuadrante_1 ]
subsidio_cuadrante_2 = cuadrante_2[cuadrante_2< promedio_cuadrante_2 ]
subsidio_cuadrante_3 = cuadrante_3[cuadrante_3< promedio_cuadrante_3 ]
subsidio_cuadrante_4 = cuadrante_4[cuadrante_4< promedio_cuadrante_4 ]

print(subsidio_cuadrante_1)
print(subsidio_cuadrante_2)
print(subsidio_cuadrante_3)
print(subsidio_cuadrante_4)

asignacion_subsidio_cuadrante_1 = vector[0]
asignacion_subsidio_cuadrante_2 = vector[1]
asignacion_subsidio_cuadrante_3 = vector[2]
asignacion_subsidio_cuadrante_4 = vector[3]


print(len(subsidio_cuadrante_1))
print(len(subsidio_cuadrante_2))
print(len(subsidio_cuadrante_3))
print(len(subsidio_cuadrante_4))


valores_subsidios = np.array([len(subsidio_cuadrante_1)*vector[0],len(subsidio_cuadrante_2)*vector[1],len(subsidio_cuadrante_3)*vector[2],len(subsidio_cuadrante_4)*vector[3]])

print(valores_subsidios)


print(valores_subsidios.max())
print(valores_subsidios.min())
print(valores_subsidios.argmax()+1)
print(valores_subsidios.argmin()+1)