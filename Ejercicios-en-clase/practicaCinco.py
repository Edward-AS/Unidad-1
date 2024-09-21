### 20-Septiembre-2024 ###

"""
El sistema para cosecha de manzanas, a cada trabajador se le paga por caja de manzanas cosechadas; las primeras 10 cajas se le pagan a
    50 pesos cada caja, más de 50 y menos de 80 cajas se le pagan 50% más, más de 80 se le pagan al doble; de su total de pago se le descuenta
    el 5% para caja de ahorro.

Generar un sistema que pida el nombre del trabajador y la cantidad de cajas cosechadas ese día, así como el pago que obtiene indicando
    la cantidad pagada de arcuerdo a la cantidad de cajas cosechadas así como el descuento que se hace por su pago.
"""

class Caja:

    def __init__(self):
        self.trabajador = ""
        self.cajas = 0
        self.cajas_normal = 0
        self.cajas_medio = 0
        self.cajas_doble = 0
        self.descuento = 0
        self.pago = 0
        self.pago_total = 0

    def pedir_nombre(self):
        nombre = input("Ingrese el nombre del trabajador: ")
        self.trabajador = nombre

    def pedir_cajas(self):
        cajas = int(input("Introduzca el número de cajas: "))
        self.cajas = cajas
        self.cajas_totales = cajas

    def pagar(self):
        for i in range(0, self.cajas + 1):
            if self.cajas == 0:
                print(f"{self.trabajador} no tiene niguna caja todavía.")
            elif self.cajas > 80:
                for i in range(self.cajas, 80, -1):
                    self.pago += 100
                    self.cajas_doble += 1
                self.cajas = 80
            elif self.cajas > 50:
                for i in range(self.cajas, 50, -1):
                    self.pago += 75
                    self.cajas_medio += 1
                self.cajas = 50
            else:
                for i in range(self.cajas, 0, -1):
                    self.pago += 50
                    self.cajas_normal += 1
                self.cajas = 0
                break

    def descontar(self):
        descuento = self.pago * 0.05
        self.descuento = descuento
        self.pago_total = self.pago
        self.pago -= descuento
    
    def imprimir(self):
        print(f"{self.trabajador} recogió {self.cajas_totales} cajas")
        print(f"\t{self.cajas_normal} cajas normales, {self.cajas_medio} cajas al 50% más y {self.cajas_doble} cajas al doble.")
        print(f"Cantidad pagada (antes del descuento): {self.pago_total}")
        print(f"Cantidad pagada: {self.pago}")
        print(f"Decuento realizado: {self.descuento}")


trabajador = Caja()
trabajador.pedir_nombre()
trabajador.pedir_cajas()
trabajador.pagar()
trabajador.descontar()
trabajador.imprimir()

