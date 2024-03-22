from Persona import *
class Profesion1(Persona):
    def __init__(self, nombre="", edad=int, sexo="", profesion="", sueldo=float):
        super().__init__(nombre, edad, sexo)
        self.__profesion = profesion
        self.__sueldo = sueldo
        self.__cantidad_personas = 0

    @property
    def profesion(self):
        return self.__profesion

    @property
    def sueldo(self):
        return self.__sueldo

    @property
    def cantidad_personas(self):
        return self.__cantidad_personas

    @cantidad_personas.setter
    def cantidad_personas(self, nueva_cantidad):
        self.__cantidad_personas = nueva_cantidad