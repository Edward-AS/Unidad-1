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


print("***** Menú *****\n1.- Rectángulo\n2.- Triángulo") #Imprime un menú de opciones
opcion = int(input("Ingrese una opción: ")) #El usuario elige una opción

match opcion: #Se relaciona la entrada del usuario con cada caso
    case 1:
        base_r = float(input("Ingrese la base del rectángulo: "))
        altura_r = float(input("Ingrese la altura del rectángulo: "))
        rectangulo = Rectangulo(base_r, altura_r) #Se instancia la clase 'Rectangulo' con una base y altura dadas por el usuario

        print("Área del rectángulo:", rectangulo.area())
    case 2:
        base_t = float(input("Ingrese la base del triángulo: "))
        altura_t = float(input("Ingrese la altura del triángulo: "))
        triangulo = Triangulo(base_t, altura_t) #Se instancia la clase 'Triangulo' con una base y altura dadas por el usuario

        print("Área del triángulo:", triangulo.area())
    case _:
        print("Opción no válida...") #Se imprime el mensaje en caso de que el usuario ingrese un carácter inválido