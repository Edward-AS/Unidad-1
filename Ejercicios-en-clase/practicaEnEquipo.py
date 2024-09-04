### 03-Septiembre-2024 ###

"""
Se pieden tres calificaciones asi como el nombre del alumno; se promedian las calificaciones
si el promedio es mayor que 70 se escribe aprobado, si es menor se indica que reprobó.

*Modalaridad
    Entra: 3 calificaciones, nombre del alumno
    Proceso: Métodos
    Salida: Promedio, resultado (reporte)

Métodos:
    Constructor -> Tres calificaciones y un nombre (4 variables)
    Promedio -> Calcula el promedio
    Comparación -> Revisa si aprueba o no
    Pedir datos -> Se ingresan los datos


! Tarea:
Investigar: Clases UML
"""

class Datos:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del alumno: ")
        self.cali1 = float(input("Ingrese la primera calificación: "))
        self.cali2 = float(input("Ingrese la segunda calificación: "))
        self.cali3 = float(input("Ingrese la tercera calificación: "))
        self.promedio = 0

    def promedio_(self):
        self.promedio = (self.cali1 + self.cali2 + self.cali3) / 3
        self.promedio = round(self.promedio, 2)
        print(f"\nPromedio de {self.nombre}: {self.promedio}")

    def comparacion(self):
        if (self.promedio >= 70):
            print(f"\n\tEl alumno {self.nombre} está APROBADO")
        else:
            print(f"\n\tEl alumno {self.nombre} está REPROBADO")

alumno = Datos()
alumno.promedio_()
alumno.comparacion()
