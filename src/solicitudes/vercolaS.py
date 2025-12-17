from ..structures.lista_enlazada import lista_enlazada

def verColaSolicitudes(listaSolicitudes):
    if listaSolicitudes.lista_vacia():
        print("No hay solicitudes pendientes.")
        return

    colaOrdenada = lista_enlazada()

    actual = listaSolicitudes.primero
    while actual is not None:
        colaOrdenada.insertarOrdenadoPrioridad(actual.dato)
        actual = actual.siguiente

    print("\nCola de solicitudes ordenada por prioridad:")
    colaOrdenada.imprimir()
