class centro:
    def __init__(self, id_cd, nombre, pais, ciudad, cpu, ram, almacenamiento):
        self.id_cd = id_cd
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento

    def __str__(self):
        return f"ID: {self.id_cd} Nombre: {self.nombre} País: {self.pais} Ciudad: {self.ciudad} CPU: {self.cpu} RAM: {self.ram} Almacenamiento: {self.almacenamiento}"