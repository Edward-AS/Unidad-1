### 30-Agosto-2024 ###

class Rectangulo:
    """Define un rectángulo según su base y su altura"""
    def __init__(self, b, h) -> None:
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h
    
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
rectangulo = Rectangulo(base, altura)
print("Área del rectángulo que tiene una base de", base, "y con altura", altura, "es de:", rectangulo.area())
