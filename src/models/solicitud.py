class solicitud:
    def __init__(self, id_solic, cliente, tipo_solic, prioridad, cpu_solic, ram_solic, almacenamiento_solic, tiempo_solic):
        self.id_solic = id_solic
        self.cliente = cliente
        self.tipo_solic = tipo_solic
        self.prioridad = prioridad
        self.cpu_solic = cpu_solic
        self.ram_solic = ram_solic
        self.almacenamiento_solic = almacenamiento_solic
        self.tiempo_solic = tiempo_solic 

    def __str__(self):
        return f"ID: {self.id_solic} Cliente: {self.cliente} Tipo de solicitud: {self.tipo_solic} Prioridad: {self.prioridad} CPU: {self.cpu_solic} RAM: {self.ram_solic} Almacenamiento: {self.almacenamiento_solic} Tiempo: {self.tiempo_solic}min"