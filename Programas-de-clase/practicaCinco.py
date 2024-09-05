### 30-Agosto-2024 ###

class Poligono:
    """Define un polígono según su base y su altura."""
    def __init__(self, b, h):
        self.b = b
        self.h = h

class Rectangulo(Poligono):
    def area(self):
        return self.b * self.h

class Triangulo(Poligono):
    def area(self):
        return (self.b * self.h) / 2

base_r = float(input("Ingrese la base del rectángulo: "))
altura_r = float(input("Ingrese la altura del rectángulo: "))
rectangulo = Rectangulo(base_r, altura_r)

base_t = float(input("Ingrese la base del triángulo: "))
altura_t = float(input("Ingrese la altura del triángulo: "))
triangulo = Triangulo(base_t, altura_t)

print("Área del rectángulo:", rectangulo.area())
print("Área del triángulo:", triangulo.area())