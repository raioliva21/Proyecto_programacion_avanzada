#!/usr/bin/env python3
from afeccion import Afeccion
from enfermedad_base import Enfermedad_base
from vacuna import Vacuna

class Ciudadano():

    def __init__(self, id, edad):
        self.__id = id #identificador
        self.__edad = edad
        # infectado, de ser True, comienza en estado de incubacion de la enfermedad 
        # dsp de determinado dia, pasa a estado infeccioso
        # dias en estado incubando e infeccioso son determinados en clase main
        self.__infectado = False
        self.__estado = {'incubador': False, 'infeccioso': False,
        'aislamiento': False, 'grave': False, 'inmune': False}
        self.__vivo = True
        self.__enfermedad_base = False
        self.__tipo_enfermedad_base = None
        self.__afeccion = False
        self.__tipo_afeccion = None
        self.__vacuna = False
        self.__tipo_vacuna = None

    #getters and setters
    @property
    def ID(self):
        return self.__id
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def infectado(self):
        return self.__infectado
    
    @infectado.setter
    def infectado(self, value):
        if isinstance(value, bool):
            self.__infectado = value
            if value == True:
                self.__estado['incubador']=True

    @property 
    def estado_infeccioso(self):
        return self.__estado['infeccioso']

    @property 
    def estado_aislamiento(self):
        return self.__estado['aislamiento']
    
    @property
    def estado_grave(self):
        return self.__estado['grave']
    
    @property 
    def estado_inmune(self):
        return self.__estado['inmune']
    
    def estado(self, key, value):
        if isinstance(value, bool):
            self.__estado[key] = value

    @property
    def vivo(self):
        return self.__vivo
    
    @vivo.setter
    def vivo(self, value):
        if isinstance(value, bool):
            self.__vivo = value
        
    @property
    def enfermedad_base(self):
        return self.__enfermedad_base
    
    @enfermedad_base.setter
    def enfermedad_base(self, value):
        if isinstance(value, bool):
            self.__enfermedad_base = value

    @property
    def tipo_enfermedad_base(self):
        return self.__tipo_enfermedad_base
    
    @tipo_enfermedad_base.setter
    def tipo_enfermedad_base(self, enfermedad):
        if isinstance(enfermedad, Enfermedad_base):
            self.__tipo_enfermedad_base = enfermedad
    
    @property
    def afeccion(self):
        return self.__afeccion
    
    @afeccion.setter
    def afeccion(self, value):
        if isinstance(value, bool):
            self.__afeccion = value

    @property
    def tipo_afeccion(self):
        return self.__tipo_afeccion
    
    @tipo_afeccion.setter
    def tipo_afeccion(self, afeccion):
        if isinstance(afeccion, Afeccion):
            self.__tipo_afeccion = afeccion

    @property
    def vacuna(self):
        return self.__vacuna
    
    @vacuna.setter
    def vacuna(self, value):
        if isinstance(value, bool):
            self.__vacuna = value
    
    @property
    def tipo_vacuna(self):
        return self.__tipo_vacuna
    
    @tipo_vacuna.setter
    def tipo_vacuna(self, vacuna):
        if isinstance(vacuna, Vacuna):
            self.__tipo_vacuna = vacuna

