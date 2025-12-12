class contenedor:
    def __init__(self, id_cont, nombre_cont, img_cont, cpu_cont, ram_cont, almacenamiento_cont, puerto):
        self.id_cont = id_cont
        self.nombre_cont = nombre_cont
        self.img_cont = img_cont
        self.cpu_cont = cpu_cont
        self.ram_cont = ram_cont
        self.almacenamiento_cont = almacenamiento_cont
        self.puerto = puerto

    def __str__(self):
        return f"ID: {self.id_cont} Nombre: {self.nombre_cont} Imagen: {self.img_cont} CPU: {self.cpu_cont} RAM: {self.ram_cont} Almacenamiento: {self.almacenamiento_cont} Puerto: {self.puerto}"