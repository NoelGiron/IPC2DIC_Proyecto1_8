class migrar_vm:
    def __init__(self, id_tipo, vm_inst, centro_dest, centro_orig):
        self.id_tipo = id_tipo
        self.vm_inst = vm_inst
        self.centro_dest = centro_dest
        self.centro_orig = centro_orig

    def __str__(self):
        return f"Tipo: {self.id_tipo}  MV creada: {self.vm_inst} Centro de origen: {self.centro_orig} Centro de destino: {self.centro_dest}"