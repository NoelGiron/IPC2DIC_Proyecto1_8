class centro:
    def __init__(self, id_cd, nombre, pais, ciudad, cpu, ram, almacenamiento):
        self.id_cd = id_cd
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad

        self.cpu = int(cpu)
        self.ram = int(ram)
        self.almacenamiento = int(almacenamiento)

        self.cpuDisp = int(cpu)
        self.ramDisp = int(ram)
        self.almDisp = int(almacenamiento)

    def __str__(self):
        return (
            f"ID: {self.id_cd} | {self.nombre} | "
            f"CPU: {self.cpuDisp}/{self.cpu} | "
            f"RAM: {self.ramDisp}/{self.ram} | "
            f"ALM: {self.almDisp}/{self.almacenamiento}"
        )