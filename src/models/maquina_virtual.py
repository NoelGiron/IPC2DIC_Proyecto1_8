from ..structures.lista_enlazada import lista_enlazada
class maquina_virtual:
    def __init__(self, id_vm, centro_asig, os, cpu_vm, ram_vm, almacenamiento, ip_mv):
        self.id_vm = id_vm
        self.centro_asig = centro_asig
        self.os = os

        self.cpu_vm = int(cpu_vm)
        self.ram_vm = int(ram_vm)
        self.almacenamiento = int(almacenamiento)

        self.ip_vm = ip_mv
        self.lista_contenedores = lista_enlazada()

        self.cpu_usada = 0
        self.ram_usada = 0

    def __str__(self):
        return (
            f"ID: {self.id_vm} | Centro: {self.centro_asig} | SO: {self.os} | "
            f"CPU: {self.cpu_usada}/{self.cpu_vm} | "
            f"RAM: {self.ram_usada}/{self.ram_vm} | "
            f"ALM: {self.almacenamiento} | IP: {self.ip_vm}"
        )

    def mostrar_contenedores(self):
        if self.lista_contenedores.lista_vacia():
            print(f"La máquina virtual {self.id_vm} no tiene contenedores.")
        else:
            print(f"Contenedores en la máquina virtual {self.id_vm}:")
            self.lista_contenedores.imprimir()

    def puede_desplegar_contenedor(self, cpu, ram):
        cpu = int(cpu)
        ram = int(ram)

        if self.cpu_usada + cpu <= self.cpu_vm and \
           self.ram_usada + ram <= self.ram_vm:
            return True
        return False

    def desplegar_contenedor(self, nuevo_contenedor):
        self.lista_contenedores.insertar(nuevo_contenedor)
        self.cpu_usada += int(nuevo_contenedor.cpu_cont)
        self.ram_usada += int(nuevo_contenedor.ram_cont)
        
    def buscar_contenedor(self, id_cont):
        actual = self.lista_contenedores.primero
        while actual:
            if actual.dato.id_cont == id_cont:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def eliminarContenedor(self, idCont):
        actual = self.lista_contenedores.primero
        anterior = None

        while actual is not None:
            if actual.dato.id_cont == idCont:
                self.cpu_vm += int(actual.dato.cpu_cont)
                self.ram_vm += int(actual.dato.ram_cont)

                if anterior is None:
                    self.lista_contenedores.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                self.lista_contenedores.size -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False
