def opcionesMV():
    print("\n--------Gestión de máquinas virtuales-----------")
    print("1) Buscar VM por ID")
    print("2) Listar VMs de un centro")
    print("3) Migrar VM entre centros")
    print("4) Volver al menu principal")


def eleccionMV(listaVM, listaCentros):
    while True:
        opcionesMV()

        try:
            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                while True:
                    idVM = input("Ingrese ID de la VM (o 'x' para volver): ").strip()
                    if idVM.lower() == 'x':
                        break

                    vm = listaVM.buscarVMID(idVM)

                    if vm:
                        print("\nVM encontrada:")
                        print(vm)
                    else:
                        print("\nVM no encontrada")

            elif opcion == "2":
                while True:
                    idCentro = input("Ingrese ID del centro (o 'x' para volver): ").strip()
                    if idCentro.lower() == 'x':
                        break

                    print(f"\nMáquinas virtuales en el centro {idCentro}:")
                    listaVM.listarVMCentro(idCentro)

            elif opcion == "3":
                idVM = input("ID de la VM: ").strip()
                idOrig = input("Centro origen: ").strip()
                idDest = input("Centro destino: ").strip()

                centroO = listaCentros.buscarporID(idOrig)
                centroD = listaCentros.buscarporID(idDest)

                if centroO and centroD:
                    listaVM.migrarVM(idVM, centroO, centroD)
                else:
                    print("Centro inválido")

            elif opcion == "4":
                break

            else:
                print("\nOpción no válida")

        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\nError: {e}")
