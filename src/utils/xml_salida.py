import os
import xml.etree.ElementTree as ET
from datetime import datetime

def generar_xml_salida(listaCentros, listaVMs):
    carpeta = "src/data"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    root = ET.Element("resultadoCloudSync")

    timestamp = ET.SubElement(root, "timestamp")
    timestamp.text = datetime.now().isoformat()

    estadoCentros = ET.SubElement(root, "estadoCentros")

    actual_centro = listaCentros.primero
    while actual_centro is not None:
        c = actual_centro.dato
        centro_elem = ET.SubElement(estadoCentros, "centro", {"id": c.id_cd})

        nombre = ET.SubElement(centro_elem, "nombre")
        nombre.text = c.nombre

        recursos = ET.SubElement(centro_elem, "recursos")

        cpuTotal = ET.SubElement(recursos, "cpuTotal")
        cpuTotal.text = str(c.cpu)

        cpuDisponible = ET.SubElement(recursos, "cpuDisponible")
        cpuDisponible.text = str(c.cpuDisp)

        cpuUtilizacion = ET.SubElement(recursos, "cpuUtilizacion")
        cpuUtilizacion.text = f"{(c.cpu - c.cpuDisp) / c.cpu * 100:.2f}%"

        ramTotal = ET.SubElement(recursos, "ramTotal")
        ramTotal.text = str(c.ram)

        ramDisponible = ET.SubElement(recursos, "ramDisponible")
        ramDisponible.text = str(c.ramDisp)

        ramUtilizacion = ET.SubElement(recursos, "ramUtilizacion")
        ramUtilizacion.text = f"{(c.ram - c.ramDisp) / c.ram * 100:.2f}%"

        cantidadVMs = 0
        cantidadContenedores = 0

        actual_vm = listaVMs.primero
        while actual_vm is not None:
            vm = actual_vm.dato
            if vm.centro_asig == c.id_cd:
                cantidadVMs += 1
                cantidadContenedores += (
                    vm.lista_contenedores.tamano()
                    if hasattr(vm.lista_contenedores, "tamano")
                    else 0
                )
            actual_vm = actual_vm.siguiente

        ET.SubElement(centro_elem, "cantidadVMs").text = str(cantidadVMs)
        ET.SubElement(centro_elem, "cantidadContenedores").text = str(cantidadContenedores)

        actual_centro = actual_centro.siguiente

    estadisticas = ET.SubElement(root, "estadisticas")

    totalVMs = 0
    totalContenedores = 0
    actual_vm = listaVMs.primero
    while actual_vm is not None:
        totalVMs += 1
        totalContenedores += (
            actual_vm.dato.lista_contenedores.tamano()
            if hasattr(actual_vm.dato.lista_contenedores, "tamano")
            else 0
        )
        actual_vm = actual_vm.siguiente

    ET.SubElement(estadisticas, "vmsActivas").text = str(totalVMs)
    ET.SubElement(estadisticas, "contenedoresTotales").text = str(totalContenedores)

    ruta_salida = os.path.join(carpeta, "salida.xml")
    tree = ET.ElementTree(root)

    ET.indent(tree, space="    ", level=0)

    tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
    print(f"XML generado correctamente en: {ruta_salida}")
