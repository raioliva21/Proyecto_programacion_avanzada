import random 
#import json
from infectado import Infectado

class Simulacion():

    def __init__(self, comunidad):
        self.__comunidad = comunidad
        self.porcentaje_proba_infeccion = self.__comunidad.probabilidad_contacto_estrecho * \
                            self.__comunidad.enfermedad.probabilidadInfeccion * 100
        # identificacion (numero) de infectado
        self.id = None

    def run(self, numero_dias):

        for lista_infectados_diarios in range(0, numero_dias):
            self.__comunidad.lista_infectados = []
        
        """ instancia infectados iniciales -dia 0- que son almacenados en lista """
        for self.id in range(0,self.__comunidad.num_inicial_infectados):
            edad = edad = random.randint(0,90)
            self.__comunidad.lista_infectados_append(dia=0,infectado=Infectado(self.id, edad))

        # periodo de ciclo = dia
        for self.dia in range(1, numero_dias):
            self.transicion_estado_infectados()
            self.evaluar_infeccion()
            self.imprimir_data_diaria()
            #self.crear_diccionario()
        #self.write_data()

    """ evalua nuevas infecciones por dia """
    def evaluar_infeccion(self):
        # recorre infectados registrados en lista
        for infectados_diarios in self.__comunidad.lista_infectados:
            for infectado in infectados_diarios:
                if infectado.estado_infeccioso == True and\
                    infectado.estado_aislamiento == False:
                    # se crean nuevos infectados
                    self.estimador_nuevos_infectados()

    def estimador_nuevos_infectados(self):

        for contacto in range(0, self.__comunidad.promedio_conexion_fisica):
            rand = random.randint(0,100)
            if rand <= self.porcentaje_proba_infeccion and \
                self.__comunidad.num_total_infectados < self.__comunidad.num_ciudadanos:
                self.id = self.id + 1
                edad = random.randint(0,90)
                self.__comunidad.lista_infectados_append(self.dia,Infectado(self.id, edad))
    
    def transicion_estado_infectados(self):

        if self.dia >= self.__comunidad.enfermedad.inicio_estado_infeccioso:
            
            for infectado in self.__comunidad.lista_infectados[self.dia - \
                self.__comunidad.enfermedad.inicio_estado_infeccioso]:
                infectado.estado('infeccioso', True)
        
        """ se da por supuesto que estado de aislamiento comienza el dia despues
        del inicio de estado sintomatico """

        inicio_aislamiento = self.__comunidad.enfermedad.inicio_estado_sintomatico + 1

        if self.dia >= inicio_aislamiento:
            
            for infectado in self.__comunidad.lista_infectados[self.dia -\
                inicio_aislamiento]:
                infectado.estado('aislamiento', True)
                infectado.estado('incubador', False)

        
        """ infectado es dado de 'alta', tal que pasa a estado inmune """
        if self.dia >= self.__comunidad.enfermedad.promedio_pasos:

            for infectado in self.__comunidad.lista_infectados[self.dia - \
                self.__comunidad.enfermedad.promedio_pasos]:
                infectado.estado('inmune', True)
                infectado.estado('infeccioso', False)
                self.evaluar_estado(infectado)
    
    def evaluar_estado(self, infectado):
        
        if infectado.edad <= 9:
            tasa_de_letalidad = 0
        elif infectado.edad >= 10 and 39 >= infectado.edad:
            tasa_de_letalidad = 0.2
        elif infectado.edad >= 40 and 49 >= infectado.edad:
            tasa_de_letalidad = 0.4
        elif infectado.edad >= 50 and 59 >= infectado.edad:
            tasa_de_letalidad = 1.3
        elif infectado.edad >= 60 and 69 >= infectado.edad:
            tasa_de_letalidad = 3.6
        elif infectado.edad >= 70 and 79 >= infectado.edad:
            tasa_de_letalidad = 8
        else:
            tasa_de_letalidad = 14.8

        rand = random.randint(0,100)

        if rand <= tasa_de_letalidad:
            #print("infectado ", infectado.ID, "muere")
            infectado.vivo = False

    def imprimir_data_diaria(self):

        print("--------------------------------------------------")
        print("Dia:", self.dia)
        print("\nPoblacion total (vivos): ", self.__comunidad.num_ciudadanos - \
            self.__comunidad.num_fallecidos)
        print("Nuevos infectados: ", len(self.__comunidad.lista_infectados[self.dia]))
        print("Total infectados: ", self.__comunidad.num_total_infectados) 
        print("Casos activos:", self.__comunidad.num_casos_activos)
        print("Susceptibles a enfermarse: ", self.__comunidad.num_ciudadanos - \
            self.__comunidad.num_total_infectados)
        print("Sanados de enfermedad (vivos): ", self.__comunidad.num_poblacion_sanada)
        print("Fallecidos: ", self.__comunidad.num_fallecidos)

        print("--------------------------------------------------")

    """
    
    establecer limite para que cantidad de contagiados no supere la cantidad total poblacion

    # se crea diccionario 
    def crear_diccionario(self):

        self.__dict ={
            f"Dia {self.dia} ": [ 
                {"Poblacion total (vivos)" : self.__poblacion,
                "Casos activos:" : self.__casos_activos,
                "Susceptibles a enfermarse: " : self.__poblacion_susceptible,
                "Sanados de enfermedad (vivos): " : self.__poblacion_sanada,
                "Fallecidos: ": len(self.__comunidad.lista_ciudadanos)-self.__poblacion}
            ]
        }
        self.__array.update(self.__dict)


    def write_data(self):

        with open("data.json", "w") as file:
            json.dump(self.__array, file, indent=4)

    """


