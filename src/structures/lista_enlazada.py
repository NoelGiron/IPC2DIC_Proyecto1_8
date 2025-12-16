class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class lista_enlazada:
    def __init__(self):
        self.primero = None
        self.size = 0

    def lista_vacia(self):
        return self.primero == None
    
    def insertar(self, dato):
        nuevo = nodo(dato)

        if self.primero == None:
            self.primero = nuevo
        
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.size += 1

    def recorrer(self, indice):
        actual = self.primero
        contador = 0
        
        while actual != None:
            if contador == indice:
                return actual.dato
            actual = actual.siguiente
            contador += 1
        return None

    def imprimir(self):
        if self.primero == None:
            print("La lista esta vacia")
            return
        
        actual = self.primero
        while actual != None:  
            print(actual.dato)
            actual = actual.siguiente

    def buscarporID(self, id_buscar):
        actual = self.primero

        while actual is not None:
            if actual.dato.id_cd == id_buscar:
                return actual.dato

            actual = actual.siguiente

        return None
    
    def centroMC(self):
        # Si la lista está vacía
        if self.primero is None:
            return None

        # Tomamos el primer centro como referencia
        actual = self.primero
        centroMayor = actual.dato

        maxRecursos = (
            int(centroMayor.cpu) +
            int(centroMayor.ram) +
            int(centroMayor.almacenamiento)
        )

        actual = actual.siguiente

        # Recorremos el resto de la lista
        while actual is not None:
            centroActual = actual.dato

            recursosActuales = (
                int(centroActual.cpu) +
                int(centroActual.ram) +
                int(centroActual.almacenamiento)
            )

            if recursosActuales > maxRecursos:
                centroMayor = centroActual
                maxRecursos = recursosActuales

            actual = actual.siguiente

        return centroMayor

    def buscarVMID(self, idBuscado):
        actual = self.primero

        while actual is not None:
            vm = actual.dato

            if vm.id_vm == idBuscado:
                return vm

            actual = actual.siguiente

        return None
    
    def listarVMCentro(self, idCentro):
        actual = self.primero
        encontrado = False

        while actual is not None:
            vm = actual.dato

            if vm.centro_asig == idCentro:
                print(vm)
                encontrado = True

            actual = actual.siguiente

        if not encontrado:
            print("No hay máquinas virtuales en este centro")
            
    def migrarVM(self, idVM, centroOrigen, centroDestino):
        actual = self.primero
        vm = None

        while actual is not None:
            if actual.dato.id_vm == idVM:
                vm = actual.dato
                break
            actual = actual.siguiente

        if vm is None:
            print("La VM no existe")
            return False

        if vm.centro_asig != centroOrigen.id_cd:
            print("La VM no pertenece al centro origen")
            return False

        cpuVM = int(vm.cpu_vm)
        ramVM = int(vm.ram_vm)
        almVM = int(vm.almacenamiento)

        if (centroDestino.cpuDisp < cpuVM or
            centroDestino.ramDisp < ramVM or
            centroDestino.almDisp < almVM):
            print("El centro destino no tiene recursos suficientes")
            return False

        centroOrigen.cpuDisp += cpuVM
        centroOrigen.ramDisp += ramVM
        centroOrigen.almDisp += almVM

        centroDestino.cpuDisp -= cpuVM
        centroDestino.ramDisp -= ramVM
        centroDestino.almDisp -= almVM

        vm.centro_asig = centroDestino.id_cd

        print(f"VM {idVM} migrada correctamente")
        return True