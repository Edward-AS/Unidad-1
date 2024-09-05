### 30-Agosto-2024 ###

class Triangulo:
    """Define un rectángulo según su base y su altura"""
    def __init__(self, b, h) -> None:
        self.b = b
        self.h = h

    def area(self):
        r = (self.b * self.h) / 2
        return r
    
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
triangulo = Triangulo(base, altura)
print("Área del triángulo que tiene una base de", base, "y con altura", altura, "es de:", triangulo.area())
