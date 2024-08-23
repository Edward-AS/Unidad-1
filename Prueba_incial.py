"""
Se pide '3' calificaciones (de 0 a 100), así como el nombre del alumno (de 'n' alumnos).
    Se promedia los alumnos que tengan calificación menor a 70 se les imprime un mensaje de "Reprobado".
Al finalizar el sistema se imprime el nombre y promedio del alumno con mayor calificación y el alumno con menor calificación

Para entregar el día de hoy
    Se entrega:
    - Algoritmo
    - Diagrama de flujo
    - Programa
"""

numero_alumnos = int(input("Ingrese el número de alumnos que desea promediar: "))

alumnos = {}
aprobados = {}
calificaciones_aprobadas = []

for i in range(0, numero_alumnos):
    nombre_alumno = input("\nNombre del estudiante: ")
    calificaciones = []
    print("Las calificaciones deben de ser en el formato (0 - 100)")
    for i in range(1, 4):
        calificacion = int(input(f"\tCalificación {i} de {nombre_alumno}: "))
        calificaciones.append(calificacion)
    promedio = sum(calificaciones) / len(calificaciones)
    alumnos[nombre_alumno] = round(promedio, 2)

print("\nREPROBADOS:")
for alumno in alumnos:
    promedio = alumnos[alumno]
    if (promedio < 70):
        print(f"\n\t---> El alumno '{alumno}' está reprobado...")
    else:
        aprobados[alumno] = promedio
        calificaciones_aprobadas.append(promedio)
        calificaciones_aprobadas.sort()

print("\nMejor y menor calificación:")
for alumno in aprobados:
    if (calificaciones_aprobadas[len(calificaciones_aprobadas) - 1] == aprobados[alumno]):
        print(f"\t----- {alumno} tuvo la mejor calificación.")
    elif (calificaciones_aprobadas[0] == aprobados[alumno]):
        print(f"\t----- {alumno} tuvo la menor calificación.")




