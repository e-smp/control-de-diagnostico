class Persona():
    def __init__(self, nombre="", edad=int, sexo=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo

    #El método property nos sirve para adquirir los atributos:
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def sexo(self):
        return self.__sexo