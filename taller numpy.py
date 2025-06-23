import numpy as np
import pandas as pd

# Datos iniciales
deptos = ["Recursos Humanos", "Desarrollo", "Soporte Técnico", "Marketing"]
empleados_por_depto = [20, 40, 30, 30]
limites_bonificaciones = {
    "Recursos Humanos": 500,
    "Desarrollo": 1000,
    "Soporte Técnico": 750,
    "Marketing": 600
}

# Crear matriz de bonificaciones
def generar_bonificaciones():
    np.random.seed(0)  # Fijar semilla para reproducibilidad
    matriz = np.zeros((sum(empleados_por_depto), 12))
    
    fila_inicio = 0
    for depto, num_empleados in zip(deptos, empleados_por_depto):
        fila_fin = fila_inicio + num_empleados
        matriz[fila_inicio:fila_fin, :] = np.random.randint(
            0, limites_bonificaciones[depto] + 1, size=(num_empleados, 12)
        )
        fila_inicio = fila_fin
    
    return matriz

bonificaciones = generar_bonificaciones()

# Análisis de bonificaciones
def analizar_bonificaciones(bonificaciones, deptos, empleados_por_depto):
    resultados = {}
    fila_inicio = 0

    for depto, num_empleados in zip(deptos, empleados_por_depto):
        fila_fin = fila_inicio + num_empleados
        depto_bonificaciones = bonificaciones[fila_inicio:fila_fin, :]

        # Promedio de bonificaciones por mes
        promedio_por_mes = depto_bonificaciones.mean(axis=0)

        # Mes con la mayor suma total de bonificaciones
        mes_mayor = np.argmax(depto_bonificaciones.sum(axis=0)) + 1

        # Mes con la menor suma total de bonificaciones
        mes_menor = np.argmin(depto_bonificaciones.sum(axis=0)) + 1

        # Empleados con bonificación mensual mayor al promedio global
        promedio_global = depto_bonificaciones.mean()
        empleados_superan_promedio = []
        for i, empleado in enumerate(depto_bonificaciones):
            for mes, bonificacion in enumerate(empleado):
                if bonificacion > promedio_global:
                    empleados_superan_promedio.append(
                        (fila_inicio + i + 1, mes + 1, bonificacion)
                    )

        resultados[depto] = {
            "Promedio por mes": promedio_por_mes,
            "Mes con mayor suma": mes_mayor,
            "Mes con menor suma": mes_menor,
            "Empleados que superan promedio": empleados_superan_promedio
        }

        fila_inicio = fila_fin

    return resultados

resultados = analizar_bonificaciones(bonificaciones, deptos, empleados_por_depto)

# Mostrar resultados
for depto, analisis in resultados.items():
    print(f"Departamento: {depto}")
    print(f"Promedio de bonificaciones por mes: {analisis['Promedio por mes']}")
    print(f"Mes con mayor suma de bonificaciones: {analisis['Mes con mayor suma']}")
    print(f"Mes con menor suma de bonificaciones: {analisis['Mes con menor suma']}")
    print("Empleados que superan el promedio global:")
    for empleado, mes, bonificacion in analisis["Empleados que superan promedio"]:
        print(f"  - Empleado {empleado}, Mes {mes}, Bonificación: {bonificacion}")
    print("-" * 50)
