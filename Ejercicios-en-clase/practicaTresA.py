### 17-Septiembre-2024 ###

class NumeroFor:

    def __init__(self, numero):
        self.numero = numero

    def tabla(self):
        print(f"Tabla de multiplicar de {self.numero}")
        for a in range(1, 11):
            print(f"{self.numero} x {a} = {self.numero * a}")

numero = int(input("Ingrese el número: "))
num = NumeroFor(numero)
num.tabla()


class NumeroWhile:

    def __init__(self, numero):
        self.numero = numero

    def tabla(self):
        a = 1
        print(f"Tabla de multiplicar de {self.numero}")
        while a <= 10:
            print(f"{self.numero} x {a} = {self.numero * a}")
            a += 1

"""numero = int(input("Ingrese el número: "))
num = NumeroWhile(numero)
num.tabla()"""