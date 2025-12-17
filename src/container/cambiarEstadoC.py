def cambiar_estado_contenedor(listaVM, idVM, idCont, accion):
    vm = listaVM.buscarVMID(idVM)
    if not vm:
        return False, "No se encontró la máquina virtual."

    cont = vm.buscar_contenedor(idCont)
    if not cont:
        return False, "No se encontró el contenedor."

    if accion == "pausar":
        return cont.pausar()
    elif accion == "activar":
        return cont.activar()
    elif accion == "detener":
        return cont.detener()
    elif accion == "reiniciar":
        return cont.reiniciar()
    else:
        return False, "Acción no válida."
