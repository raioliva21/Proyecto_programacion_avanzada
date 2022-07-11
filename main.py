from enfermedad import Enfermedad
from comunidad import Comunidad
from simulacion import Simulacion
#import json


def main():
    
    virus = Enfermedad(probabilidadInfeccion=0.3, promedio_pasos=14,
                        inicio_estado_infeccioso=2, inicio_estado_sintomatico=5)
    
    """ 
    Promedio_conexion_fisica refiere a aproximacion de contactos por dia 
    de infectado en estado infeccioso y de no aislamiento.
    Estado de aislamiento comienza al dia despues de inicio de estado sintomatico.
    En estado de aislamiento se asume que infectado no infecta.
    """
    comunidad = Comunidad(num_ciudadanos=4000,promedio_conexion_fisica = 3,
                          enfermedad=virus,num_infectados=10,
                           probabilidad_contacto_estrecho=0.8)

    simulador = Simulacion(comunidad)
    simulador.run(numero_dias=25)

    """


    # Opening JSON file
    f = open('data.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    for key, values in data.items():
        for i in values:
            print(key, " : ", i)
    
    # Closing file
    f.close()
    """

if __name__ == "__main__":
    main()
