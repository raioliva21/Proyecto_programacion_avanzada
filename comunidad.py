
from infectado import Infectado


class Comunidad():

    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad,
                  num_infectados, probabilidad_contacto_estrecho):

        # atributos de caracter privado
        self.__num_ciudadanos = num_ciudadanos
        self.__promedio_conexion_fisica = promedio_conexion_fisica
        self.__enfermedad = enfermedad
        self.__num_inicial_infectados = num_infectados
        self.__probabilidad_contacto_estrecho = probabilidad_contacto_estrecho
        """ lista infectados contiene lista de infectados en dia indicado por indice"""
        # ejemplo: lista_infectados[0] -> lista infectados en dia 0
        self.__lista_infectados = []
    
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
    def lista_infectados(self):
        return self.__lista_infectados
    
    @lista_infectados.setter
    def lista_infectados(self, lista_diaria):
        if isinstance(lista_diaria, list):
            self.__lista_infectados.append(lista_diaria)
        else:
            print("Error, lista_infectados.setter.")
    
    def lista_infectados_append(self, dia, infectado):
        if isinstance (infectado, Infectado):
            self.__lista_infectados[dia].append(infectado)
        else:
            print("Error, lista_infectados_append.setter.")
    
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

    
