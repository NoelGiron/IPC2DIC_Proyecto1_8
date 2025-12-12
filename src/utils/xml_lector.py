import xml.etree.ElementTree as ET

from ..structures import lista_enlazada
from ..models import centro
from ..models import maquina_virtual
from ..models import contenedor
from ..models import solicitud
from ..models import crear_vm
from ..models import migrar_vm

class xml_lector:
    def __init__(self):
        self.centros = lista_enlazada()
        self.maquinas_virtuales = lista_enlazada()
        self.contenedroes = lista_enlazada()
        self.solicitudes = lista_enlazada()
        self.instruciones = lista_enlazada()
        self.datos_cargados = False

    def leer_xml(self, archivo):
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()

            self.leer_centros(root.find('centrosDatos'))
            self.leer_maquinas_virtuales(root.find('maquinasVirtuales'))
            self.leer_solicitudes(root.find('solicitudes'))
            self.leer_instrucciones(root.find('instrucciones'))

            self.datos_cargados = True

            return True
        
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return False

    def leer_centros(self, lista_elementos):

        if lista_elementos is None:
            return False
        
        for elemento in lista_elementos.findall('centro'):

            centro_id = elemento.get('id')
            centro_nombre = elemento.get('nombre')

            centro_ubicacion = elemento.find('ubicacion')
            centro_pais = centro_ubicacion.find('pais').text
            centro_ciudad = centro_ubicacion.find('ciudad').text

            centro_capacidad = elemento.find('capacidad')
            centro_cpu = centro_capacidad.find('cpu').text
            centro_ram = centro_capacidad.find('ram').text
            centro_almacenamiento = centro_capacidad.find('almacenamiento').text

            nuevo_centro = centro(centro_id, centro_nombre, centro_pais, centro_ciudad, centro_cpu, centro_ram, centro_almacenamiento)
            self.centros.insertar(nuevo_centro)

