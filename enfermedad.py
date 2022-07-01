class Enfermedad():
    """docstring for Enfermedad."""

    def __init__(self, probabilidadInfeccion, promedio_pasos):
        self.__probabilidadInfeccion =  probabilidadInfeccion
        self.__promedio_pasos = promedio_pasos

    #getters and setters
    @property
    def probabilidadInfeccion(self):
        return self.__probabilidadInfeccion

    @probabilidadInfeccion.setter
    def probabilidadInfeccion(self, variable):
        self.__probabilidadInfeccion = variable

    @property
    def promedioPasos(self):
        return self.__promedio_pasos

    @promedioPasos.setter
    def promedioPasos(self, variable):
        self.__promedio_pasos = variable
