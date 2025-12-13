class procesar:
    def __init__(self, id_pros, cantidad_pros):
        self.id_pros = id_pros
        self.cantidad_pros = cantidad_pros

    def __str__(self):
        return print(f"Tipo: {self.id_pros} Cantidad: {self.cantidad_pros}")