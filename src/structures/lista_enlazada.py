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
            while actual.siguiente != None:
                print(actual.dato)
                actual = actual.siguiente
            print(actual.dato)
            