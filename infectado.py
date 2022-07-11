from ciudadano import Ciudadano

class Infectado(Ciudadano):

    def __init__(self, id, edad):
        self.__id = id #identificador
        self.__edad = edad
        """ A modo de ahorrar espacio en memoria, se desconsidera eventual key 
        'susceptible' tal que se crean unicamente ciudadanos incialmente enfermos 
        en vez de instanciar la totalidad de ciudadanos de la comunidad """
        # infectado comienza en estado de incubacion de la enfermedad 
        # dsp de determinado dia, pasa a estado infeccioso
        # dias en estado incubando e infeccioso son determinados en clase main
        self.__estado = {'incubador': True, 'infeccioso': False,
        'aislamiento': False, 'inmune': False}
        self.__vivo = True

    #getters and setters
    @property
    def ID(self):
        return self.__id
    
    @property
    def edad(self):
        return self.__edad

    @property 
    def estado_infeccioso(self):
        return self.__estado['infeccioso']

    @property 
    def estado_aislamiento(self):
        return self.__estado['aislamiento']
    
    @property 
    def estado_inmune(self):
        return self.__estado['inmune']
    
    def estado(self, key, value):
        if isinstance(value, bool):
            self.__estado[key] = value
        else:
            print("error, estado.setter")

    @property
    def vivo(self):
        return self.__vivo
    
    @vivo.setter
    def vivo(self, value):
        if isinstance(value, bool):
            self.__vivo = value
        else:
            print("error, vive.setter")
