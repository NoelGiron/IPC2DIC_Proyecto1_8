import xml.etree.ElementTree as ET

from ..structures.lista_enlazada import lista_enlazada
from ..models.centro import centro
from ..models.maquina_virtual import maquina_virtual
from ..models.contenedor import contenedor
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
                print("No se encontró la sección de configuración")
                return False

            centros_elemento = configuracion.find('centrosDatos')
            if centros_elemento:
                print("\nCargando centros de datos...")
                self.leer_centros(centros_elemento)
            else:
                print("Advertencia: no hay centros de datos definidos")

            maquinas_elemento = configuracion.find('maquinasVirtuales')
            if maquinas_elemento:
                print("\nCargando máquinas virtuales...")
                self.leer_maquinas_virtuales(maquinas_elemento)
            else:
                print("Advertencia: no hay máquinas virtuales definidas")

            solicitudes_elemento = configuracion.find('solicitudes')
            if solicitudes_elemento:
                print("\nCargando solicitudes...")
                self.leer_solicitudes(solicitudes_elemento)
            else:
                print("Advertencia: no hay solicitudes")

            instrucciones_elemento = root.find('instrucciones')
            if instrucciones_elemento:
                print("\nCargando instrucciones...")
                self.leer_instrucciones(instrucciones_elemento)
            else:
                print("Advertencia: no hay instrucciones")

            self.datos_cargados = True
            print("\nArchivo XML cargado correctamente")
            return True

        except Exception as e:
            print(f"No se pudo leer el archivo: {e}")
            return False

    def leer_centros(self, lista_elementos):
        centros_encontrados = lista_elementos.findall('centro')

        for elemento in centros_encontrados:
            try:
                nuevo_centro = centro(
                    id_cd=elemento.get('id'),
                    nombre=elemento.get('nombre'),
                    pais=elemento.find('ubicacion/pais').text,
                    ciudad=elemento.find('ubicacion/ciudad').text,
                    cpu=elemento.find('capacidad/cpu').text,
                    ram=elemento.find('capacidad/ram').text,
                    almacenamiento=elemento.find('capacidad/almacenamiento').text
                )

                self.centros.insertar(nuevo_centro)
                print(f"Centro '{nuevo_centro.nombre}' agregado")

            except Exception as e:
                print(f"No se pudo cargar un centro: {e}")

    def leer_maquinas_virtuales(self, lista_elementos):
        maquinas_encontradas = lista_elementos.findall('vm')

        for elemento in maquinas_encontradas:
            try:
                mv_id = elemento.get('id')
                mv_centro = elemento.get('centroAsignado')

                nuevo_mv = maquina_virtual(
                    id_vm=mv_id,
                    centro_asig=mv_centro,
                    os=elemento.find('sistemaOperativo').text,
                    cpu_vm=elemento.find('recursos/cpu').text,
                    ram_vm=elemento.find('recursos/ram').text,
                    almacenamiento=elemento.find('recursos/almacenamiento').text,
                    ip_mv=elemento.find('ip').text
                )

                centro_actual = self.centros.buscarporID(mv_centro)

                if centro_actual:
                    centro_actual.cpuDisp -= int(nuevo_mv.cpu_vm)
                    centro_actual.ramDisp -= int(nuevo_mv.ram_vm)
                    centro_actual.almDisp -= int(nuevo_mv.almacenamiento)
                else:
                    print(f"No se encontró el centro {mv_centro} para la VM {mv_id}")

                contenedores_elementos = elemento.find('contenedores')
                if contenedores_elementos is not None:
                    for contenedor_elemento in contenedores_elementos.findall('contenedor'):
                        nuevo_contenedor = contenedor(
                            id_cont=contenedor_elemento.get('id'),
                            nombre_cont=contenedor_elemento.find('nombre').text,
                            img_cont=contenedor_elemento.find('imagen').text,
                            cpu_cont=contenedor_elemento.find('recursos/cpu').text,
                            ram_cont=contenedor_elemento.find('recursos/ram').text,
                            puerto=contenedor_elemento.find('puerto').text
                        )
                        nuevo_mv.lista_contenedores.insertar(nuevo_contenedor)

                self.maquinas_virtuales.insertar(nuevo_mv)
                print(f"Máquina virtual '{mv_id}' cargada")

            except Exception as e:
                print(f"Error al cargar una máquina virtual: {e}")

    def leer_solicitudes(self, lista_elementos):
        solicitudes_encontradas = lista_elementos.findall('solicitud')

        for elemento in solicitudes_encontradas:
            try:
                nueva_solicitud = solicitud(
                    id_solic=elemento.get('id'),
                    cliente=elemento.find('cliente').text,
                    tipo_solic=elemento.find('tipo').text,
                    prioridad=elemento.find('prioridad').text,
                    cpu_solic=elemento.find('recursos/cpu').text,
                    ram_solic=elemento.find('recursos/ram').text,
                    almacenamiento_solic=elemento.find('recursos/almacenamiento').text,
                    tiempo_solic=elemento.find('tiempoEstimado').text
                )

                self.solicitudes.insertar(nueva_solicitud)
                print(f"Solicitud '{nueva_solicitud.id_solic}' registrada")

            except Exception as e:
                print(f"No se pudo cargar una solicitud: {e}")

    def leer_instrucciones(self, lista_elementos):
        instrucciones_encontradas = lista_elementos.findall('instruccion')

        for elemento in instrucciones_encontradas:
            try:
                instruccion_tipo = elemento.get('tipo')

                if instruccion_tipo == 'crearVM':
                    nueva_instruccion = crear_vm(
                        tipo_inst='crearVM',
                        id_inst=elemento.find('id').text,
                        centro_inst=elemento.find('centro').text,
                        so_inst=elemento.find('so').text,
                        cpu_inst=elemento.find('cpu').text,
                        ram_inst=elemento.find('ram').text,
                        almacenamiento_inst=elemento.find('almacenamiento').text
                    )
                    self.instrucciones.insertar(nueva_instruccion)
                    print("Instrucción para crear VM agregada")

                elif instruccion_tipo == 'migrarVM':
                    nueva_instruccion = migrar_vm(
                        id_tipo='migrarVM',
                        vm_inst=elemento.find('vmId').text,
                        centro_dest=elemento.find('centroDestino').text,
                        centro_orig=elemento.find('centroOrigen').text,
                    )
                    self.instrucciones.insertar(nueva_instruccion)
                    print("Instrucción para migrar VM agregada")

                elif instruccion_tipo == 'procesarSolicitudes':
                    cantidad = elemento.find('cantidad').text
                    nueva_instruccion = procesar(
                        id_pros='procesarSolicitudes',
                        cantidad_pros=cantidad
                    )
                    self.instrucciones.insertar(nueva_instruccion)
                    print(f"Se procesarán {cantidad} solicitudes")

            except Exception as e:
                print(f"Error al leer una instrucción: {e}")


    