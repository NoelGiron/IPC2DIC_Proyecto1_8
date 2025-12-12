class maquina_virtual:
    def __init__(self, id_vm, centro_asig, os, cpu_vm, ram_vm, almacenamiento, ip_mv):
        self.id_vm = id_vm
        self.centro_asig = centro_asig
        self.os = os
        self.cpu_vm = cpu_vm
        self.ram_vm = ram_vm
        self.almacenamiento = almacenamiento
        self.ip_vm = ip_mv

    def __str__(self):
        return f"ID: {self.id_vm} Centro asignado: {self.centro_asig} Sistema Operativo: {self.os} CPU: {self.cpu_vm} RAM: {self.ram_vm} Almacenamiento: {self.almacenamiento} IP: {self.ip_vm}"