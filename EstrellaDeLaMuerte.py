class EstrellaDeLaMuerteClase:
    def __init__(self, puntos):
        self.puntos = puntos

    def destruir_planeta(self, planeta):
        if planeta.clasificacion <= self.puntos:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}!")
        else:
            print(f"La Estrella de la Muerte no puede destruir el planeta {planeta.nombre}.")
