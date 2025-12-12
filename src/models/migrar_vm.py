class migrar_vm:
    def __init__(self, tipo_inst, id_inst, centro_inst, so_inst, cpu_inst, ram_inst, almacenamiento_inst):
        self.tipo_inst = tipo_inst
        self.id_inst = id_inst
        self.centro_inst = centro_inst
        self.so_inst = so_inst
        self.cpu_inst = cpu_inst
        self.ram_inst = ram_inst
        self.almacenamiento_inst = almacenamiento_inst

    def __str__(self):
        return f"\nTipo: {self.tipo_inst} \nID: {self.id_inst} \nCentro: {self.centro_inst} \nSistema Operativo: {self.so_inst} \nCPU: {self.cpu_inst} \nRAM: {self.ram_inst} \nAlmacenamiento: {self.almacenamiento_inst}"
        