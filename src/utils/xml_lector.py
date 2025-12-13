import xml.etree.ElementTree as ET

from ..structures.lista_enlazada import lista_enlazada
from ..models.centro import centro
from ..models.maquina_virtual import maquina_virtual
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
                print(f"\nLeyendo Centros de datos")
                self.leer_centros(centros_elemento)
            else:
                print("ADVERTENCIA: No se encontró 'centrosDatos'")

            maquinas_elemento = configuracion.find('maquinasVirtuales')

            if maquinas_elemento:
                print(f"\nLeyendo Maquinas virtuales")
                self.leer_maquinas_virtuales(maquinas_elemento)
            else:
                print("ADVERTENCIA: No se encontró 'naquinasVirtuales'")

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

    def leer_maquinas_virtuales(self, lista_elementos):

        if lista_elementos is None:
            print("ERROR: lista_elementos es None")
            return
        
        maquinas_encontradas = lista_elementos.findall('vm')
        
        for elemento in maquinas_encontradas:
            try:
                mv_id = elemento.get('id')
                mv_centro = elemento.get('centroAsignado')

                mv_os = elemento.find('sistemaOperativo').text

                mv_recursos = elemento.find('recursos')
                mv_cpu = mv_recursos.find('cpu').text
                mv_ram = mv_recursos.find('ram').text
                mv_almacenamiento = mv_recursos.find('almacenamiento').text

                mv_ip = elemento.find('ip').text

                nuevo_mv = maquina_virtual(
                    id_vm = mv_id,
                    centro_asig = mv_centro,
                    os = mv_os,
                    cpu_vm = mv_cpu,
                    ram_vm = mv_ram,
                    almacenamiento = mv_almacenamiento,
                    ip_mv =  mv_ip

                )
                self.maquinas_virtuales.insertar(nuevo_mv)
                print(f"Maquina virtual '{mv_id}' procesado")

            except Exception as e:
                print(f"Error al procesar los centros: {e}")

