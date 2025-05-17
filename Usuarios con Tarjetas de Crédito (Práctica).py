
# Suponiendo que la clase TarjetaCredito ya está definida y disponible

class Usuario:
    def __init__(self, nombre, tarjeta):
        self.nombre = nombre
        self.tarjeta = tarjeta  # Una instancia de TarjetaCredito

    def hacer_compra(self, monto):
        self.tarjeta.compra(monto)
        return self

    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}")
        self.tarjeta.mostrar_info_tarjeta()

# BONUS: Usuario con varias tarjetas de crédito
class UsuarioMultipleTarjetas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = {}  # Diccionario: nombre_tarjeta -> TarjetaCredito

    def agregar_tarjeta(self, nombre_tarjeta, tarjeta):
        self.tarjetas[nombre_tarjeta] = tarjeta

    def hacer_compra(self, nombre_tarjeta, monto):
        if nombre_tarjeta in self.tarjetas:
            self.tarjetas[nombre_tarjeta].compra(monto)
        else:
            print(f"No existe la tarjeta '{nombre_tarjeta}' para el usuario.")
        return self

    def pagar_tarjeta(self, nombre_tarjeta, monto):
        if nombre_tarjeta in self.tarjetas:
            self.tarjetas[nombre_tarjeta].pago(monto)
        else:
            print(f"No existe la tarjeta '{nombre_tarjeta}' para el usuario.")
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}")
        for nombre_tarjeta, tarjeta in self.tarjetas.items():
            print(f"- {nombre_tarjeta}: ", end="")
            tarjeta.mostrar_info_tarjeta()