#!/usr/bin/env python3
from ciudadano import Ciudadano
import random

class Comunidad():

    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad,
                  num_infectados, probabilidad_contacto_estrecho,
                  poblacion_con_enfermedad_base, poblacion_con_afeccion,
                  poblacion_vacunada, vacunas):

        # atributos de caracter privado
        self.__num_ciudadanos = num_ciudadanos
        self.__promedio_conexion_fisica = promedio_conexion_fisica
        self.__enfermedad = enfermedad
        self.__num_inicial_infectados = num_infectados
        self.__probabilidad_contacto_estrecho = probabilidad_contacto_estrecho
        self.__poblacion_con_enfermedad_base = poblacion_con_enfermedad_base
        self.__poblacion_con_afeccion = poblacion_con_afeccion
        self.__poblacion_vacunada = poblacion_vacunada
        self.__vacunas = vacunas 
        self.__lista_ciudadanos = []
        """ lista infectados contiene lista de infectados en dia indicado por indice"""
        # ejemplo: lista_infectados[0] -> lista infectados en dia 0
        self.__lista_infectados = []

        #crea lista total de ciudadanos
        for i in range(0,num_ciudadanos):
            edad = random.randint(0,90)
            self.__lista_ciudadanos.append(Ciudadano(i,edad))
        
        #print("la cantidad de ciudadanos es:", len(self.__lista_ciudadanos))

    @property
    def num_ciudadanos(self):
        return self.__num_ciudadanos
    
    @property
    def promedio_conexion_fisica(self):
        return self.__promedio_conexion_fisica
    
    @property
    def enfermedad(self):
        return self.__enfermedad
    
    @property
    def num_inicial_infectados(self):
        return self.__num_inicial_infectados
    
    @property
    def probabilidad_contacto_estrecho(self):
        return self.__probabilidad_contacto_estrecho
    
    @property
    def poblacion_con_enfermedad_base(self):
        return self.__poblacion_con_enfermedad_base
    
    @property
    def poblacion_con_afeccion(self):
        return self.__poblacion_con_afeccion
    
    @property
    def poblacion_vacunada(self):
        return self.__poblacion_vacunada
    
    @property
    def vacunas(self):
        return self.__vacunas
    
    @property
    def lista_ciudadanos(self):
        return self.__lista_ciudadanos
    
    @property
    def lista_infectados(self):
        return self.__lista_infectados
    
    @lista_infectados.setter
    def lista_infectados(self, lista_diaria):
        if isinstance(lista_diaria, list):
            self.__lista_infectados.append(lista_diaria)
    
    def lista_infectados_append(self, dia, infectado):
        if isinstance (infectado, Ciudadano):
            self.__lista_infectados[dia].append(infectado)
    
    @property
    def num_fallecidos(self):
        num_fallecidos = 0
        for infectados_diarios in self.__lista_infectados:
            for infectado in infectados_diarios:
                if infectado.vivo == False:
                    num_fallecidos = num_fallecidos + 1
        return num_fallecidos

    @property
    def num_total_infectados(self):
        num_total_infectados = 0
        for infectados_diarios in self.__lista_infectados:
            num_total_infectados = num_total_infectados + len(infectados_diarios)
        return num_total_infectados

    @property
    def num_casos_activos(self):
        num_casos_activos = 0
        for infectados_diarios in self.__lista_infectados:
            for infectado in infectados_diarios:
                if infectado.estado_infeccioso == True:
                    num_casos_activos = num_casos_activos + 1
        return num_casos_activos

    @property
    def num_poblacion_sanada(self):
        num_poblacion_sanada = 0
        for infectados_diarios in self.__lista_infectados:
            for infectado in infectados_diarios:
                if infectado.estado_inmune == True and True == infectado.vivo:
                    num_poblacion_sanada = num_poblacion_sanada + 1
        return num_poblacion_sanada

    
