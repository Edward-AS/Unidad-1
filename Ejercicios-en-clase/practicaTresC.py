### 17-Septiembre-2024 ###

class SolicitarNombre:
    
    def __init__(self):
        self.nombre = ""

    def pedir_nombre(self):
        while True:
            self.nombre = input("Ingresa tu nombre (o escribe 'salir' para terminar): ")
            if self.nombre.lower() == "salir": 
                print("Saliendo del programa.")
                break
            elif not self.nombre:
                print("El nombre no puede estar vacío. Inténtalo de nuevo.")
            else:
                print("Nombre ingresado:", self.nombre)
                

solicitar_nombre = SolicitarNombre()
solicitar_nombre.pedir_nombre()