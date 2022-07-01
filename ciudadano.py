class Ciudadano():
    """docstring for Ciudadano."""

    def __init__(self, id):
        self.__id = id
        self.__infectado = False
        self.__estado = True
        self.__contador = 0
        self.__inmune = False
        self.__sano = True
        self.__familia = []

    #getter con setter
    @property
    def ID(self):
        return self.__id

    @ID.setter
    def ID(self, variable):
        self.__id = variable

    @property
    def infectado(self):
        return self.__infectado

    @infectado.setter
    def infectado(self, variable):
        self.__infectado = variable

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, variable):
        self.__estado = variable

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, variable):
        self.__contador = variable

    @property
    def inmune(self):
        return self.__inmune

    @inmune.setter
    def inmune(self, variable):
        self.__inmune = variable

    @property
    def sano(self):
        return self.__sano

    @sano.setter
    def sano(self, variable):
        self.__sano = variable

    @property
    def familia(self):
        return self.__familia

    def familiaAdd(self, add):
        self.__familia.append(add)
