from ..models.contenedor import contenedor

def desplegarContenedor(listaVM, idVM, idCont, nombre, imagen, cpu, ram, puerto):
    vm = listaVM.buscarVMID(idVM)

    if not vm:
        return False, "No se encontró la máquina virtual."

    if not vm.puede_desplegar_contenedor(cpu, ram):
        return False, "La VM no tiene recursos suficientes."

    nuevo_contenedor = contenedor(
        id_cont=idCont,
        nombre_cont=nombre,
        img_cont=imagen,
        cpu_cont=cpu,
        ram_cont=ram,
        puerto=puerto
    )

    vm.desplegar_contenedor(nuevo_contenedor)
    return True, "Contenedor desplegado."
