class contenedor:
    def __init__(self, id_cont, nombre_cont, img_cont, cpu_cont, ram_cont, puerto):
        self.id_cont = id_cont
        self.nombre_cont = nombre_cont
        self.img_cont = img_cont
        self.cpu_cont = int(cpu_cont)
        self.ram_cont = int(ram_cont)
        self.puerto = puerto
        self.estado = "Activo"

    def pausar(self):
        if self.estado == "Activo":
            self.estado = "Pausado"
            return True, "Contenedor pausado."
        return False, f"No se puede pausar desde el estado {self.estado}."

    def activar(self):
        if self.estado in ["Pausado", "Detenido"]:
            self.estado = "Activo"
            return True, "Contenedor activado."
        return False, f"No se puede activar desde el estado {self.estado}."

    def detener(self):
        if self.estado != "Detenido":
            self.estado = "Detenido"
            return True, "Contenedor detenido."
        return False, "El contenedor ya está detenido."

    def reiniciar(self):
        if self.estado == "Activo":
            self.estado = "Reiniciando"
            self.estado = "Activo"
            return True, "Contenedor reiniciado."
        return False, f"No se puede reiniciar desde el estado {self.estado}."

    def __str__(self):
        return (
            f"ID: {self.id_cont} | Nombre: {self.nombre_cont} | "
            f"Imagen: {self.img_cont} | CPU: {self.cpu_cont} | "
            f"RAM: {self.ram_cont} | Puerto: {self.puerto} | "
            f"Estado: {self.estado}"
        )
