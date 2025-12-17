from src.structures.lista_enlazada import lista_enlazada


def opcionesCD():
    print("\n--- Gestión de centros de datos ---")
    print("1) Ver todos los centros")
    print("2) Buscar un centro por ID")
    print("3) Mostrar el centro con más recursos")
    print("4) Volver al menú principal")


def eleccionCD(listaCentros):
    while True:
        opcionesCD()

        try:
            opcion = input("\nElige una opción: ").strip()

            if opcion == "1":
                listaCentros.imprimir()

            elif opcion == "2":
                while True:
                    idCD = input("\nIngresa el ID del centro (o 'x' para volver): ").strip()
                    if idCD.lower() == 'x':
                        break
                    
                    centro = listaCentros.buscarporID(idCD)
                    if centro:
                        print(f"\nCentro encontrado:\n{centro}")
                    else:
                        print("\nNo se encontró ningún centro con ese ID.")

            elif opcion == "3":
                centro = listaCentros.centroMC()

                if centro is None:
                    print("\nNo hay centros registrados.")
                else:
                    print("\nCentro con mayor capacidad:")
                    print(centro)

            elif opcion == "4":
                print("\nVolviendo al menú principal...")
                break

            else:
                print("\nOpción no válida. Intenta de nuevo.")

        except KeyboardInterrupt:
            print("\n\nPrograma detenido por el usuario.")
            break

        except Exception as e:
            print(f"\nOcurrió un error: {e}")