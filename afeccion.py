#!/usr/bin/env python3
# por planteamiento, esta clase no requiere mayor contenido
""" superclase en clases obesidad y desnutricion. """

class Afeccion():
    def __init__(self):
        self.__factor_agravante = None

    @property
    def factor_agravante(self):
        return self.__factor_agravante

""" CLASES CHILD """
class Obesidad(Afeccion):
    @property
    def factor_agravante(self):
        return 2.0

class Desnutricion(Afeccion):
    @property
    def factor_agravante(self):
        return 1.9