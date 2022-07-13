#!/usr/bin/env python3
import random 
import json
from enfermedad_base import Asma,Enfermedad_cerebrovascular,Fibrosis_quistica,Hipertension,PAA
from afeccion import Obesidad,Desnutricion

class Simulacion():

    def __init__(self, comunidad):
        self.__comunidad = comunidad
        self.porcentaje_proba_infeccion = self.__comunidad.probabilidad_contacto_estrecho * \
                            self.__comunidad.enfermedad.probabilidadInfeccion * 100
        self.dia = 0
        self.__aa = {}
        self.crear_poblacion_de_riesgo()
        self.crear_poblacion_vacunada()
    
    def crear_poblacion_de_riesgo(self):

        num_ciudadanos_con_EnfermedadBase = int(self.__comunidad.num_ciudadanos * \
                            self.__comunidad.poblacion_con_enfermedad_base)
        num_ciudadanos_con_Afeccion = int(self.__comunidad.num_ciudadanos * \
                            self.__comunidad.poblacion_con_afeccion)

        i = 0
        while i < num_ciudadanos_con_EnfermedadBase:
            num_ciudadano = random.randrange(0, self.__comunidad.num_ciudadanos)
            ciudadano = self.__comunidad.lista_ciudadanos[num_ciudadano]
            if ciudadano.enfermedad_base == False:
                """ otorga enfermedad base a ciudadano seleccionado"""
                ciudadano.enfermedad_base = True
                # para especificar enfermedad base
                self.select_tipo_de_enfermedad(ciudadano)
                i += 1

        i = 0
        while i < num_ciudadanos_con_Afeccion:
            num_ciudadano = random.randrange(0, self.__comunidad.num_ciudadanos)
            ciudadano = self.__comunidad.lista_ciudadanos[num_ciudadano]
            if ciudadano.afeccion == False:
                """ otorga afeccion a ciudadano seleccionado"""
                ciudadano.afeccion = True
                # para especificar afeccion
                self.select_tipo_de_afeccion(ciudadano)
                i += 1
    
    """ otorga enfermedad especifica a ciudadano.enfermedad_base = True """
    def select_tipo_de_enfermedad(self, ciudadano):

        enfermedades_base = [Asma(),Enfermedad_cerebrovascular(),
        Fibrosis_quistica(),Hipertension(),PAA()]
        enfermedad_base = random.choice(enfermedades_base)
        ciudadano.tipo_enfermedad_base = enfermedad_base
        
    """ otorga afeccion especifica a ciudadano.afeccion = True """
    def select_tipo_de_afeccion(self, ciudadano):

        afecciones = [Obesidad(),Desnutricion()]
        afeccion = random.choice(afecciones)
        ciudadano.tipo_afeccion = afeccion
    
    def crear_poblacion_vacunada(self):

        lista_prioridad = []
        for list in range(0,4):
            lista_prioridad.append([])

        """ Clasifica ciudadanos de acuerdo a probalidad de agrabamiento al infectarse. 
            Aquellos ciudadanos con mayor probabilidad de agrabamiento
            seran de mayor prioridad en etapa de vacunacion """
        for ciudadano in self.__comunidad.lista_ciudadanos:
            gravedad = self.evaluar_gravedad(ciudadano)
            if gravedad >= 50:
                lista_prioridad[0].append(ciudadano)
            elif gravedad < 50 and 30 <= gravedad:
                lista_prioridad[1].append(ciudadano)
            elif gravedad < 30 and 10 <= gravedad:
                lista_prioridad[2].append(ciudadano)
            else:
                lista_prioridad[3].append(ciudadano)
        
        # cantidad total de vacunas
        cantidad_vacunas = int(self.__comunidad.num_ciudadanos * \
                            self.__comunidad.poblacion_vacunada)

        # resuelve cantidad inicial disponible de cada vacuna
        for vacuna in self.__comunidad.vacunas:
            vacuna.cantidad_disponible = int(vacuna.razon * cantidad_vacunas)
        
        # recorre lista de prioridad
        for lista in lista_prioridad:
            for ciudadano in lista:
                # selecciona un tipo de vacuna de manera aleatoria
                vacuna = random.choice(self.__comunidad.vacunas)
                # si existe disponibilidad (cantidad > 0) de tal vacuna
                if vacuna.cantidad_disponible > 0:
                    ciudadano.vacuna = True
                    ciudadano.tipo_vacuna = vacuna
                    if vacuna.desarrollo_inmunidad == True:
                        ciudadano.estado('inmune', True)
                    vacuna.cantidad_disponible = vacuna.cantidad_disponible - 1

    """ metodo principal que encarga de correr simulacion """
    def run(self, numero_dias):

        # se ingresan listas vacias en lista de infectados
        # 'self.__comunidad.lista_infectados' contiene lista de infectados por dia
        for i in range(0, numero_dias):
            self.__comunidad.lista_infectados = []
        
        # instancian infectados iniciales -dia 0- que son almacenados en lista 
        i = 0
        while i < self.__comunidad.num_inicial_infectados:
            ciudadano = random.choice(self.__comunidad.lista_ciudadanos)
            if ciudadano.vacuna == False:
                ciudadano.infectado = True
                # se agrega ciudadano, ya infectado, en lista de ciudadanos
                self.__comunidad.lista_infectados_append(self.dia,ciudadano)
                i=i+1

        # periodo de ciclo = un dia
        """se han otorgado vacunas pero no se han modifican estados de ciudadanos"""
        for self.dia in range(1, numero_dias):
            self.transicion_estado_infectados()
            self.evaluar_infeccion()
            self.imprimir_data_diaria()
            self.creacion_diccionario()
        self.write_data()

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

        contacto = 0
        while contacto < self.__comunidad.promedio_conexion_fisica:
            rand = random.randint(0,100)
            if rand <= self.porcentaje_proba_infeccion and \
                self.__comunidad.num_total_infectados < self.__comunidad.num_ciudadanos:
                    ciudadano = random.choice(self.__comunidad.lista_ciudadanos)
                    if ciudadano.estado_inmune == False and ciudadano.infectado == False:
                        ciudadano.infectado = True
                        self.__comunidad.lista_infectados_append(self.dia,ciudadano)
            contacto =contacto+1     

    def transicion_estado_infectados(self):

        if self.dia >= self.__comunidad.enfermedad.inicio_estado_infeccioso:
            
            for infectado in self.__comunidad.lista_infectados[self.dia - \
                self.__comunidad.enfermedad.inicio_estado_infeccioso]:
                infectado.estado('infeccioso', True)
        

        inicio_aislamiento = self.__comunidad.enfermedad.inicio_estado_sintomatico + 1

        if self.dia >= inicio_aislamiento:
            for infectado in self.__comunidad.lista_infectados[self.dia -\
                inicio_aislamiento]:
                infectado.estado('aislamiento', True)
                infectado.estado('incubador', False)
                
                gravedad = self.evaluar_gravedad(infectado)
                rand = random.randint(0,100)

                # infectado puede tener vacuna 1 o 2
                if infectado.vacuna == True:
                    # si tiene vacuna 1
                    if infectado.tipo_vacuna.impedimiento_gravedad == False:
                        gravedad = gravedad-infectado.tipo_vacuna.disminucion_gravedad_enfermedad
                        if rand <= gravedad:
                            infectado.estado('grave',True)
                    # infectado con vacuna 2
                    else:
                        # estado.gravedad = False ; valor de atributo se mantiene
                        pass

        
        if self.dia >= self.__comunidad.enfermedad.promedio_pasos:
            
            for infectado in self.__comunidad.lista_infectados[self.dia - \
                    self.__comunidad.enfermedad.promedio_pasos]:
                
                """ infectado es dado de 'alta', tal que pasa a estado inmune """
                if infectado.estado_grave == False:
                    infectado.estado('inmune', True)         
                else:
                    """
                    Innfectado en estado grave.
                    Proablilidad arbitraria: 50% de que infectado en estado grave muera.
                    """
                    rand = random.choice([True, False])
                    infectado.vivo = rand
                    if rand == True:
                        infectado.estado('inmune', True)
                infectado.estado('infeccioso', False)  
    
    def evaluar_gravedad(self, ciudadano):
        
        if ciudadano.edad <= 9:
            gravedad = self.__comunidad.enfermedad.gravedad['edad(0,9)']
        elif ciudadano.edad >= 10 and 39 >= ciudadano.edad:
            gravedad = self.__comunidad.enfermedad.gravedad['edad(10,39)']
        elif ciudadano.edad >= 40 and 49 >= ciudadano.edad:
            gravedad = self.__comunidad.enfermedad.gravedad['edad(40,49)']
        elif ciudadano.edad >= 50 and 59 >= ciudadano.edad:
            gravedad = self.__comunidad.enfermedad.gravedad['edad(50,59)']
        elif ciudadano.edad >= 60 and 69 >= ciudadano.edad:
            gravedad = self.__comunidad.enfermedad.gravedad['edad(60,69)']
        elif ciudadano.edad >= 70 and 79 >= ciudadano.edad:
            gravedad = self.__comunidad.enfermedad.gravedad['edad(70,79)']
        else:
            gravedad = self.__comunidad.enfermedad.gravedad['edad(80,+oo)']
        
    
        if ciudadano.enfermedad_base == True:
            gravedad = gravedad * (ciudadano.tipo_enfermedad_base.factor_agravante)
        
        if ciudadano.afeccion == True:
            gravedad = gravedad * (ciudadano.tipo_afeccion.factor_agravante)
        
        return gravedad 

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

    # se crea diccionario 
    def creacion_diccionario(self):

        _dict ={
            f"Dia {self.dia} ":  
                {"Poblacion total (vivos)" : self.__comunidad.num_ciudadanos - \
                self.__comunidad.num_fallecidos,
                "Nuevos infectados: ": len(self.__comunidad.lista_infectados[self.dia]),
                "Casos activos:" : self.__comunidad.num_casos_activos,
                "Susceptibles a enfermarse: " : self.__comunidad.num_ciudadanos - \
                self.__comunidad.num_total_infectados,
                "Sanados de enfermedad (vivos): " : self.__comunidad.num_poblacion_sanada,
                "Fallecidos: ": self.__comunidad.num_fallecidos}
        }
        self.__aa.update(_dict)


    def write_data(self):

        with open("data.json", "w") as file:
            json.dump(self.__aa, file, indent=4)

    


