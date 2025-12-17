from ..container.desplegarC import desplegarContenedor

def opcionesCN():
    print("\n--------Gestión de centro de datos-----------")
    print("1) Desplegar contenedor en VM")
    print("2) Listar contenedores de una VM")
    print("3) Cambiar estado de contenedor")
    print("4) Eliminar contenedor")
    print("5) Volver al menu principal")
    
def eleccionCN(listaVM):
    while True:
        opcionesCN()
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                idVM = input("ID de la VM: ")
                idCont = input("ID del contenedor: ")
                nombre = input("Nombre del contenedor: ")
                imagen = input("Imagen: ")
                cpu = input("CPU requerida: ")
                ram = input("RAM requerida: ")
                puerto = input("Puerto: ")

                ok, msg = desplegarContenedor(
                    listaVM,
                    idVM,
                    idCont,
                    nombre,
                    imagen,
                    cpu,
                    ram,
                    puerto
                )

                print(msg)
            elif opcion == "2":
                print("\nlistar")
            elif opcion == "3":
                print("\ncambiar")
            elif opcion == "4":
                print("\neliminar")
            elif opcion == "5":
                print("\nmenu principal")
                break
            else:
                print("\nOpcion no valida")
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\nError: {e}")