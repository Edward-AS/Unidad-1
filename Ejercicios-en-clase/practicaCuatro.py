### 18-Septiembre-2024 ###

"""
Desarrollar un sistema 'caja de cambio' en el cual se inserta un billete o se le indica una cantidad a cambiar el sistema devuelve
    la cantidad en monedas de 10, 5 y 1 peso.

REGLA GENERAL:
    No se puede devolver todo de una sola moneda. Al menos una de cada denominacón

Ejemplo:
    Le damos 100 pesos

    Regresa:
        9 de 10 pesos
        1 de 5 pesos
        5 de 1 peso
"""

class Moneda:
    
    def __init__(self):
        self.billete = 0
        self.uno = 0
        self.cinco = 0
        self.diez = 0

    def pedir_datos(self):
        cantidad = int(input("Ingresa la cantidad de dinero que desea cambiar: "))
        self.billete = cantidad

    def conversion(self):
        while self.billete > 0:
            if self.billete > 10:
                self.billete -= 10
                self.diez += 1
            elif self.billete > 5:
                self.billete -= 5
                self.cinco += 1
            else:
                self.billete -= 1
                self.uno += 1

    def imprimir(self):
        print(f"\nSe entregan:\n\t{self.diez} monedas de 10 pesos\n\t{self.cinco} monedas de 5 pesos\n\t{self.uno} monedas de 1 peso")


cambio = Moneda()
cambio.pedir_datos()
cambio.conversion()
cambio.imprimir()