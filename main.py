from enfermedad import Enfermedad
from comunidad import Comunidad
from simulacion import Simulacion
import json


def main():

    virus_Z = Enfermedad(probabilidadInfeccion=0.3, promedio_pasos=10)

    comunidad = Comunidad(num_ciudadanos=500,promedio_conexion_fisica=8,
                          enfermedad=virus_Z,num_infectados=10,
                           probabilidad_contacto_estrecho=0.8)

    simulador = Simulacion(comunidad, virus_Z)
    simulador.crea_contactos()
    simulador.run(numero_dias=22)

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
