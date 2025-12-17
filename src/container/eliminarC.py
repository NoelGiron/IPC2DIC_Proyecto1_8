def eliminarContenedorVM(listaVM, idVM, idCont):
    vm = listaVM.buscarVMID(idVM)

    if vm is None:
        return False, "No se encontró la máquina virtual."

    eliminado = vm.eliminarContenedor(idCont)

    if eliminado:
        return True, "Contenedor eliminado y recursos liberados."
    else:
        return False, "No se encontró el contenedor en la VM."
