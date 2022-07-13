#!/usr/bin/env python3
class Enfermedad():

    def __init__(self, probabilidadInfeccion, promedio_pasos,
                inicio_estado_infeccioso, inicio_estado_sintomatico, tasa_de_letalidad):
        self.__probabilidadInfeccion =  probabilidadInfeccion
        self.__promedio_pasos = promedio_pasos
        self.__inicio_estado_infeccioso = inicio_estado_infeccioso
        self.__inicio_estado_sintomatico = inicio_estado_sintomatico
        self.__gravedad = tasa_de_letalidad

    @property
    def probabilidadInfeccion(self):
        return self.__probabilidadInfeccion
    
    @property
    def promedio_pasos(self):
        return self.__promedio_pasos

    @property
    def inicio_estado_infeccioso(self):
        return self.__inicio_estado_infeccioso
    
    @property
    def inicio_estado_sintomatico(self):
        return self.__inicio_estado_sintomatico

    @property
    def gravedad(self):
        return self.__gravedad
    
    