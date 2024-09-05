### 04-Septiembre-2024 ###

class Calificaciones:

    def __init__(self):
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.n = ""

    def prom(self):
        r = (self.c1 + self.c2 + self.c3) / 3
        r = round(r, 2)
        return r

    def comparacion(self, num):
        if num >= 70:
            rs = "Aprobado"
        else:
            rs = "Reprobado"
        return rs


cal = Calificaciones() #Encapsulamiento --> ()
cal.n = input("Escribe el nombre: ")
cal.c1 = int(input("Escribe la primera calificación: "))
cal.c2 = int(input("Escribe la segunda calificación: "))
cal.c3 = int(input("Escribe la tercera calificación: "))

p = cal.prom()
c = cal.comparacion(p)

print(f"El alumno {cal.n} con calificaciones: {cal.c1}, {cal.c2}, {cal.c3} y con promedio de {p} está '{c}'")
