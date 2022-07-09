import random as ran
import json

class Simulacion():
    """docstring for Simulacion."""

    def __init__(self, comunidad, enfermedad):
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad
        self.__array = {}

    
    def run(self, numero_dias):
        for self.dia in range(1, numero_dias):
            self.contagio_x_contacto(self.dia)
            self.imprimir_contagiados()
            self.crear_diccionario()
        self.write_data()
            
    
    def contagio_x_contacto(self, numero_dias):
        for i in range(len(self.__comunidad.lista_ciudadanos)):
            potencial_contagio = False
            for k in range(len(self.__comunidad.lista_ciudadanos[i].familia)):
                if (self.__comunidad.lista_ciudadanos[k].estado and
                    self.__comunidad.lista_ciudadanos[k].sano ==False):
                    potencial_contagio = True

            #if para que se infecten
            if(self.__comunidad.lista_ciudadanos[i].estado==True and
               self.__comunidad.lista_ciudadanos[i].inmune==False and
               self.__comunidad.lista_ciudadanos[i].sano==True and 
               potencial_contagio):
                # para enfermar segun probabilidad y la cantidad de personas que se asocian
                random = ran.randint(0,100)
                #probabilidad conexion es para los contactos estrechos
                if (random < (self.__enfermedad.probabilidadInfeccion *\
                     self.__comunidad.probabilidad_conexion*100)):
                    self.__comunidad.lista_ciudadanos[i].sano = False
                    self.__comunidad.lista_ciudadanos[i].inmune=True
                    self.__comunidad.lista_ciudadanos[i].infectado = True
                    self.__comunidad.lista_ciudadanos[i].contador = numero_dias

            """ fragmento que determina si caso activo sana """
            if(self.__comunidad.lista_ciudadanos[i].estado and
               self.__comunidad.lista_ciudadanos[i].sano==False and
               (numero_dias) == self.__enfermedad.promedioPasos+\
                   self.__comunidad.lista_ciudadanos[i].contador):
                probabilidad_muerte = ran.randint(0,100)
                if probabilidad_muerte <= 25:
                    self.__comunidad.lista_ciudadanos[i].sano = False
                    self.__comunidad.lista_ciudadanos[i].estado = False
                    self.__comunidad.lista_ciudadanos[i].infectado = False
                else:
                    self.__comunidad.lista_ciudadanos[i].sano=True
                    self.__comunidad.lista_ciudadanos[i].infectado = False


    def crea_contactos(self):

        avance = 0
        while avance < len(self.__comunidad.lista_ciudadanos):
            for i in range(self.__comunidad.promedio_conexion):
                random = ran.randint(0,(len(self.__comunidad.lista_ciudadanos)-1))
                # si listas no estan llenas sobre el promedio de conexion
                if (len(self.__comunidad.lista_ciudadanos[avance].familia) < \
                    self.__comunidad.promedio_conexion and
                    len(self.__comunidad.lista_ciudadanos[random].familia)< \
                        self.__comunidad.promedio_conexion):
                    # añade a lista si no se tiene familia 
                    self.__comunidad.lista_ciudadanos[avance].familiaAdd(random)
            avance = avance + 1

    def imprimir_contagiados(self):

        self.__casos_activos = 0
        self.__poblacion = 0
        self.__poblacion_susceptible = 0
        self.__poblacion_inmune = 0

        for i in range(len(self.__comunidad.lista_ciudadanos)):
            if (self.__comunidad.lista_ciudadanos[i].estado):
                if(self.__comunidad.lista_ciudadanos[i].sano == True and
                self.__comunidad.lista_ciudadanos[i].inmune == False):
                    self.__poblacion_susceptible = self.__poblacion_susceptible + 1
                if(self.__comunidad.lista_ciudadanos[i].inmune == True):
                    self.__poblacion_inmune = self.__poblacion_inmune + 1
                if(self.__comunidad.lista_ciudadanos[i].infectado == True):
                    self.__casos_activos = self.__casos_activos + 1
                self.__poblacion = self.__poblacion + 1
        
        self.__poblacion_sanada = self.__poblacion_inmune - self.__casos_activos

        print("--------------------------------------------------")
        #print("Nuevos contagios: ", casos_nuevos_contagios)
        print("Dia:", self.dia)
        print("\nPoblacion total (vivos): ", self.__poblacion)
        print("Casos activos:", self.__casos_activos)
        print("Susceptibles a enfermarse: ", self.__poblacion_susceptible)
        print("Sanados de enfermedad (vivos): ", self.__poblacion_sanada)
        print("Fallecidos: ", len(self.__comunidad.lista_ciudadanos)-self.__poblacion)

        print("--------------------------------------------------")

    
    """ se crea diccionario """
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

    





