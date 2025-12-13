import xml.etree.ElementTree as ET

from ..structures.lista_enlazada import lista_enlazada
from ..models.centro import centro
from ..models.maquina_virtual import maquina_virtual
#from models.contenedor import contenedor
from ..models.solicitud import solicitud
from ..models.crear_vm import crear_vm
from ..models.migrar_vm import migrar_vm
from ..models.procesar import procesar

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
                print("ADVERTENCIA: No se encontró 'maquinasVirtuales'")

            solicitudes_elemento = configuracion.find('solicitudes')
        
            if solicitudes_elemento:
                print(f"\nLeyendo Solicitudes")
                self.leer_solicitudes(solicitudes_elemento)
            else:
                print("ADVERTENCIA: No se encontró 'solicitudes'")

            instrucciones_elemento = root.find('instrucciones')

            if instrucciones_elemento:
                print(f"\nLeyendo instrucciones")
                self.leer_instrucciones(instrucciones_elemento)
            else:
                print("ADVERTECNIA: No se encontró 'instrucciones'")

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
                print(f"Maquina virtual '{mv_id}' procesadas")

            except Exception as e:
                print(f"Error al procesar las MV: {e}")
    
    def leer_solicitudes(self, lista_elementos):
        if lista_elementos is None:
            print("ERROR: lista_elementos es None")

        solicitudes_encontradas = lista_elementos.findall('solicitud')

        for elemento in solicitudes_encontradas:
            try:
                solicitud_id = elemento.get('id')
                solicitud_centro = elemento.find('cliente').text
                solicitud_tipo = elemento.find('tipo').text
                solicitud_prioridad = elemento.find('prioridad').text

                solicitud_recursos = elemento.find('recursos')
                solicitud_cpu = solicitud_recursos.find('cpu').text
                solicitud_ram = solicitud_recursos.find('ram').text
                solicitud_almacenamiento = solicitud_recursos.find('almacenamiento').text

                solicitud_tiempo = elemento.find('tiempoEstimado').text

                nueva_solicitud = solicitud(
                    id_solic = solicitud_id,
                    cliente = solicitud_centro,
                    tipo_solic = solicitud_tipo,
                    prioridad = solicitud_prioridad,
                    cpu_solic = solicitud_cpu,
                    ram_solic = solicitud_ram,
                    almacenamiento_solic = solicitud_almacenamiento,
                    tiempo_solic = solicitud_tiempo
                )
                self.solicitudes.insertar(nueva_solicitud)
                print(f"Solicitudes '{solicitud_id}' procesadas")

            except Exception as e:
                print(f"Error al procesar las solicitudes: {e}")

    def leer_instrucciones(self, lista_elementos):
        if lista_elementos is None:
            print("ERROR: lista_elementos es None")

        instrucciones_encontradas = lista_elementos.findall('instruccion')

        for elemento in instrucciones_encontradas:
            try:
                instruccion_tipo = elemento.get('tipo')

                if instruccion_tipo == 'crearVM':
                    instruccion_id = elemento.find('id').text
                    instruccion_centro = elemento.find('centro').text
                    instruccion_os = elemento.find('so').text
                    instruccion_cpu = elemento.find('cpu').text
                    instruccion_ram = elemento.find('ram').text
                    instruccion_almacenamiento = elemento.find('almacenamiento').text

                    nueva_instruccion = crear_vm (
                        tipo_inst = 'crearVM',
                        id_inst = instruccion_id,
                        centro_inst = instruccion_centro,
                        so_inst = instruccion_os,
                        cpu_inst = instruccion_cpu,
                        ram_inst = instruccion_ram,
                        almacenamiento_inst = instruccion_almacenamiento
                    )
                    self.instrucciones.insertar(nueva_instruccion)
                    print(f"Instruccion '{instruccion_tipo}'")

                elif instruccion_tipo == 'migrarVM':
                    instruccion_vm = elemento.find('vmId').text
                    instruccion_origen = elemento.find('centroOrigen').text
                    instruccion_destino = elemento.find('centroDestino').text

                    nueva_instruccion = migrar_vm (
                        id_tipo = 'migrarVM',
                        vm_inst = instruccion_vm,
                        centro_dest = instruccion_destino,
                        centro_orig = instruccion_origen,
                    )
                    self.instrucciones.insertar(nueva_instruccion)
                    print(f"Instruccion '{instruccion_tipo}'")

                elif instruccion_tipo == 'procesarSolicitudes':
                    instruccion_cantidad = elemento.find('cantidad').text

                    nueva_instruccion = procesar (
                        id_pros = 'procesarSolicitudes',
                        cantidad_pros = instruccion_cantidad
                    )
                    self.instrucciones.insertar(nueva_instruccion)
                    print(f"Instrucciones a procesar {instruccion_cantidad}")

            except Exception as e:
                print(f"Error al procesar instrucciones: {e}")


    