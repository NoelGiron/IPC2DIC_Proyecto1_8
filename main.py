from src.utils.xml_lector import xml_lector

gestor_cloudsync = xml_lector()

def menu_principal():
    print("--------CloudSync Managaer-----------")
    print("1) Cargar archivo XML")
    print("2) Gestión de centro de datos")
    print("3) Gestión de maquinas virtuales")
    print("4) Gestión de contenedores")
    print("5) Reportes en Graphviz")
    print("6) Historial de operaciones")
    print("7) Salir")

def main():
     while True:
        menu_principal()
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                archivo = input("\nIngrese el nombre del archivo:")

                gestor_cloudsync.leer_xml(archivo)
                gestor_cloudsync.centros.imprimir()
                gestor_cloudsync.maquinas_virtuales.imprimir()
                gestor_cloudsync.solicitudes.imprimir()

                
            elif opcion == "2":
               print("\nen procesos")
                
            elif opcion == "3":
                print("\nen procesos")
                
            elif opcion == "4":
                print("\nen procesos")
                
            elif opcion == "5":
                print("\nen procesos")
                
            elif opcion == "6":
                print("\nen procesos")
                
            elif opcion == "7":
                print("\n¡Hasta luego!")
                break
                
            else:
                print("\n Opción no válida. Intente nuevamente.")
                
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__=="__main__":
    main()