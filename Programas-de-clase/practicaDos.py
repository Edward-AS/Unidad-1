### 30-Agosto-2024 ###

class Alumno:
    def __init__(self):
        self.nombre = "Pablo"

    def saludar(self):
        """Imprime un saludo en la pantalla"""
        print(f"¡Hola, {self.nombre}!")


x = Alumno()
x.saludar()
print(x.nombre)