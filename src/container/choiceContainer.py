from ..container.desplegarC import desplegarContenedor
from ..container.listarC import listarContenedoresVM
from ..container.cambiarEstadoC import cambiar_estado_contenedor

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
                idCont = input("ID contenedor: ")
                nombre = input("Nombre contenedor: ")
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
                listarContenedoresVM(listaVM)
            elif opcion == "3":
                idVM = input("ID de la VM (o 'x' para volver): ").strip()
                if idVM.lower() == 'x':
                    continue

                idCont = input("ID del contenedor: ").strip()

                print("\n1) Pausar")
                print("2) Activar")
                print("3) Reiniciar")
                print("4) Detener")

                accion_op = input("Elige una acción: ").strip()

                acciones = {
                    "1": "pausar",
                    "2": "activar",
                    "3": "reiniciar",
                    "4": "detener"
                }

                if accion_op not in acciones:
                    print("Opción no válida.")
                    continue

                ok, msg = cambiar_estado_contenedor(
                    listaVM,
                    idVM,
                    idCont,
                    acciones[accion_op]
                )

                print(msg)

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