#!/usr/bin/env python3
from enfermedad import Enfermedad
from comunidad import Comunidad
from simulacion import Simulacion
from vacuna import Vacuna_1,Vacuna_2,Vacuna_3

def main():
    
    #tasa de letalidad de enfermedad subdividida por rango etario
    #valores son dados arbitrariamente
    tsl = {'edad(0,9)': 0, 'edad(10,39)': 10.0, 'edad(40,49)': 16.0,
            'edad(50,59)': 20.3,'edad(60,69)': 28.6,'edad(70,79)': 34.0,
            'edad(80,+oo)': 44.8}

    virus = Enfermedad(probabilidadInfeccion=0.3, promedio_pasos=8,
                        inicio_estado_infeccioso=2, inicio_estado_sintomatico=5,
                        tasa_de_letalidad = tsl)
    
    """ 
    Promedio_conexion_fisica refiere a aproximacion de contactos por dia 
    de infectado en estado infeccioso y de no aislamiento.
    Estado de aislamiento comienza al dia despues de inicio de estado sintomatico.
    En estado de aislamiento se asume que infectado no infecta.
    """
    
    comunidad = Comunidad(num_ciudadanos=5000,promedio_conexion_fisica=3,
                          enfermedad=virus,num_infectados=10,
                           probabilidad_contacto_estrecho=0.8,
                           poblacion_con_enfermedad_base = 0.25,
                           poblacion_con_afeccion = 0.6,
                           poblacion_vacunada = 0.5,
                           vacunas = [Vacuna_1(razon=9/18), \
                            Vacuna_2(razon=6/18), Vacuna_3(razon=3/18)])

    simulador = Simulacion(comunidad)
    simulador.run(numero_dias=25)

if __name__ == "__main__":
    main()
