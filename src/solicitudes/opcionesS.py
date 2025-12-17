from ..solicitudes.vercolaS import verColaSolicitudes

def opcionesS():
    print("\n--------Gestión de máquinas virtuales-----------")
    print("1) Agregar nueva solicitud")
    print("2) Procesar solicitud de mayor prioridad")
    print("3) Procesar N solicitudes")
    print("4) Ver cola de solicitudes")
    print("5) Volver al menu principal")


def eleccionS(listaSolicitudes):
    while True:
        opcionesS()

        try:
            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                print("Agregar nueva solicitud")
            elif opcion == "2":
                print("Procesar solicitud de mayor prioridad")
            elif opcion == "3":
                print("Procesar N solicitudes")

            elif opcion == "4":
                verColaSolicitudes(listaSolicitudes)
                
            elif opcion == "5":
                break

            else:
                print("\nOpción no válida")

        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\nError: {e}")