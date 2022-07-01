from ciudadano import Ciudadano
import random as ran

class Comunidad():

    """docstring for Comunidad."""

    def __init__(self, num_ciudadanos, promedio_conexion_fisica, enfermedad,
                  num_infectados, probabilidad_contacto_estrecho):

        # atributos de caracter privado
        self.__num_ciudadanos = num_ciudadanos
        self.__lista_ciudadanos = []
        self.__promedio_conexion = promedio_conexion_fisica
        self.__enfermedad = enfermedad
        self.__num_infectados = num_infectados
        self.__probabilidad_contacto_estrecho = probabilidad_contacto_estrecho

        # inicia ciclo y se instancian ciudadanos agregados en lista
        for i in range(self.__num_ciudadanos):
            self.__lista_ciudadanos.append(Ciudadano(i))

        # infeccion aleatoria de ciudadanos
        aux = 0
        while aux < self.__num_infectados:
            seleccionados = ran.randint(0, self.__num_infectados)
            if(self.__lista_ciudadanos[seleccionados].infectado == False):
                self.__lista_ciudadanos[seleccionados].sano = False
                self.__lista_ciudadanos[seleccionados].inmune=True
                self.__lista_ciudadanos[seleccionados].infectado = True
                # menos 1 porque son del dia anterior
                self.__lista_ciudadanos[seleccionados].contador = -1
                aux = aux + 1

    # getters and setters
    @property
    def numero_ciudadano(self):
        return self.__num_ciudadanos

    @numero_ciudadano.setter
    def numero_ciudadano(self, variable):
        self.__num_ciudadanos = variable

    @property
    def lista_ciudadanos(self):
        return self.__lista_ciudadanos

    @lista_ciudadanos.setter
    def lista_ciudadanos(self, variable):
        self.__lista_ciudadanos = variable
    @property
    def promedio_conexion(self):
        return self.__promedio_conexion

    @promedio_conexion.setter
    def promedio_conexion(self, variable):
        self.__promedio_conexion = variable

    @property
    def dolencia(self):
        return self.__enfermedad

    @dolencia.setter
    def enfermedad(self, variable):
        self.__enfermedad = variable

    @property
    def numero_infectados(self):
        return self.numero_infectados

    @numero_infectados.setter
    def numero_infectados(self, variable):
        self.__num_infectados = variable

    @property
    def probabilidad_conexion(self):
        return self.__probabilidad_contacto_estrecho

    @probabilidad_conexion.setter
    def probabilidad_conexion(self, variable):
        self.__probabilidad_contacto_estrecho = variable
