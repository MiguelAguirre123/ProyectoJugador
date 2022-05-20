from Fecha import Fecha
from Nif import Nif
from Nombre import Nombre

class Persona:

    nombre:Nombre
    nif:Nif
    fechaNac:Fecha

    def __init__(self, nombre:Nombre, nif:Nif, fechanac:Fecha):

        self.nombre = nombre
        self.nif = nif
        self.fechaNac = fechanac
