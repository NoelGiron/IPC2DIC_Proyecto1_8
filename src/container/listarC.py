def listarContenedoresVM(listaVM):
    while True:
        idVM = input(
            "\nIngresa el ID de la VM (o 'x' para volver): "
        ).strip()

        if idVM.lower() == 'x':
            return

        vm = listaVM.buscarVMID(idVM)

        if vm:
            print()
            vm.mostrar_contenedores()
        else:
            print("\nNo se encontró la máquina virtual.")