import xml.etree.ElementTree as ET

from ..structures.lista_enlazada import lista_enlazada
from ..models.centro import centro
#from models.maquina_virtual import maquina_virtual
#from models.contenedor import contenedor
#from models.solicitud import solicitud
#from models.crear_vm import crear_vm
#from models.migrar_vm import migrar_vm

class xml_lector:
    def __init__(self):
        self.centros = lista_enlazada()
        self.maquinas_virtuales = lista_enlazada()
        self.contenedores = lista_enlazada()
        self.solicitudes = lista_enlazada()
        self.instrucciones = lista_enlazada()
        self.datos_cargados = False

    def leer_xml(self, archivo):
        try:
            ruta_completa = "src/data/" + archivo
            tree = ET.parse(ruta_completa)
            root = tree.getroot()

            configuracion = root.find('configuracion')
            if configuracion is None:
                print("ERROR: No se encontró 'configuracion'")
                return False

            centros_elemento = configuracion.find('centrosDatos')
        
            if centros_elemento:
                print(f"\nLeyendo centros")
                self.leer_centros(centros_elemento)
            else:
                print("ADVERTENCIA: No se encontró 'centrosDatos'")

            self.datos_cargados = True
            return True
        
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return False

    def leer_centros(self, lista_elementos):

        if lista_elementos is None:
            print("ERROR: lista_elementos es None")
            return
        
        centros_encontrados = lista_elementos.findall('centro')
        
        for elemento in centros_encontrados:
            try:
                centro_id = elemento.get('id')
                centro_nombre = elemento.get('nombre')

                centro_ubicacion = elemento.find('ubicacion')
                centro_pais = centro_ubicacion.find('pais').text
                centro_ciudad = centro_ubicacion.find('ciudad').text

                centro_capacidad = elemento.find('capacidad')
                centro_cpu = centro_capacidad.find('cpu').text
                centro_ram = centro_capacidad.find('ram').text
                centro_almacenamiento = centro_capacidad.find('almacenamiento').text

                nuevo_centro = centro(
                    id_cd = centro_id,
                    nombre = centro_nombre,
                    pais = centro_pais,
                    ciudad = centro_ciudad,
                    cpu = centro_cpu,
                    ram = centro_ram,
                    almacenamiento = centro_almacenamiento

                )
                self.centros.insertar(nuevo_centro)
                print(f"Centro '{centro_nombre}' procesado")

            except Exception as e:
                print(f"Error al procesar los centros: {e}")

