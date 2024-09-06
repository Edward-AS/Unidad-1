### 06-Septiembre-2024 ###

class Alumno:

    def __init__(self):
        self.n = input("Escribe el nombre: ")
        self.c1 = int(input("Escribe la primera calificación: "))
        self.c2 = int(input("Escribe la segunda calificación: "))
        self.c3 = int(input("Escribe la tercera calificación: "))
        self.promedio = 0

class Promedio(Alumno):

    def prom(self): #Agregar aquí la tarea (debajo)
        if self.c1 >= 70 and self.c2 >= 70 and self.c3 >= 70:
            self.promedio = (self.c1 + self.c2 + self.c3) / 3
            self.promedio = round(self.promedio, 2)
        else:
            self.promedio = 0
        
class Comparacion(Promedio):

    def comparacion(self):
        if self.promedio >= 70:
            rs = "Aprobado"
        else:
            rs = "Reprobado"
        return rs

class Imprimir(Comparacion):

    def imprimir(self):
        print(f"""\nEl alumno {self.n} con calificaciones:
              Calificación 1: {self.c1}
              Calificación 2: {self.c2}
              Calificación 3: {self.c3}

              Tuvo un promedio de {self.promedio} y está {self.comparacion()}""")
        

cal = Imprimir()
cal.prom()
cal.comparacion()
cal.imprimir()
