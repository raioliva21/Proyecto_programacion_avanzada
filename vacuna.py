#!/usr/bin/env python3
# por planteamiento, esta clase no requiere mayor contenido
""" superclase en clases avacuna_1, vacuna_2, vacuna_3 """

class Vacuna():
    def __init__(self, razon) -> None:
        self.__razon = razon
        self.__cantidad_disponible = None
        self.__desarrollo_inmunidad = None
        self.__impedimiento_gravedad = None
        self.__disminucion_gravedad_enfermedad = None
        pass

    @property
    def razon(self):
        return self.__razon
    
    @property
    def cantidad_disponible(self):
        return self.__cantidad_disponible
    
    @cantidad_disponible.setter
    def cantidad_disponible(self, num):
        if isinstance(num, int):
            self.__cantidad_disponible = num
    
    @property
    def desarrollo_inmunidad(self):
        return self.__desarrollo_inmunidad
    
    @property
    def impedimiento_gravedad(self):
        return self.__impedimiento_gravedad
    
    @property
    def disminucion_gravedad_enfermedad(self):
        return self.__disminucion_gravedad_enfermedad

class Vacuna_1(Vacuna):
    def __init__(self,razon) -> None:
        super().__init__(razon)

    @property
    def desarrollo_inmunidad(self):
        return False
    
    @property
    def impedimiento_gravedad(self):
        return False

    @property
    def disminucion_gravedad_enfermedad(self):
        return 0.25

class Vacuna_2(Vacuna):
    def __init__(self, razon) -> None:
        super().__init__(razon)
    
    @property
    def desarrollo_inmunidad(self):
        return False
    
    @property
    def impedimiento_gravedad(self):
        return True

class Vacuna_3(Vacuna):
    def __init__(self, razon) -> None:
        super().__init__(razon)
    
    @property
    def desarrollo_inmunidad(self):
        return True
    