from ..structures.lista_enlazada import lista_enlazada
class maquina_virtual:
    def __init__(self, id_vm, centro_asig, os, cpu_vm, ram_vm, almacenamiento, ip_mv):
        self.id_vm = id_vm
        self.centro_asig = centro_asig
        self.os = os
        self.cpu_vm = cpu_vm
        self.ram_vm = ram_vm
        self.almacenamiento = almacenamiento
        self.ip_vm = ip_mv
        self.lista_contenedores = lista_enlazada()

    def __str__(self):
        return f"ID: {self.id_vm} Centro asignado: {self.centro_asig} Sistema Operativo: {self.os} CPU: {self.cpu_vm} RAM: {self.ram_vm} Almacenamiento: {self.almacenamiento} IP: {self.ip_vm}"
    
    def mostrar_contenedores(self):
        if self.lista_contenedores.lista_vacia():
            print(f"la VM {self.id_vm} no tiene contenedores")
        else:
            print(f"Contenendores de la VM {self.id_vm}:")
            self.lista_contenedores.imprimir()