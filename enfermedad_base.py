#!/usr/bin/env python3
# por planteamiento, esta clase no requiere mayor contenido
""" superclase en clases asma, enfermedad cerebrovascular, 
    fibrosis quistica, hipertension y presion arterial alta """

class Enfermedad_base():
    def __init__(self):
        self.__factor_agravante = 3.0
        pass
    @property
    def factor_agravante(self):
        return self.__factor_agravante

""" CLASES CHILD """

class Asma(Enfermedad_base):
    pass

class Enfermedad_cerebrovascular(Enfermedad_base):
    pass

class Fibrosis_quistica(Enfermedad_base):
    pass

class Hipertension(Enfermedad_base):
    pass

class PAA(Enfermedad_base):
    pass