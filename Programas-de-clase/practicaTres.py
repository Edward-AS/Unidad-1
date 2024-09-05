### 30-Agosto-2024 ###

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        """Imprime un saludo en la pantalla"""
        print(f"¡Hola, {self.nombre}!")


usuario = input("Ingrese su nombre: ")
x = Alumno(usuario)
x.saludar()
#print(x.nombre)