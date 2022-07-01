from enfermedad import Enfermedad
from comunidad import Comunidad
from simulacion import Simulacion


def main():

    virus_Z = Enfermedad(probabilidadInfeccion=0.3, promedio_pasos=10)

    comunidad = Comunidad(num_ciudadanos=500,promedio_conexion_fisica=8,
                          enfermedad=virus_Z,num_infectados=10,
                           probabilidad_contacto_estrecho=0.8)

    simulador = Simulacion(comunidad, virus_Z)
    simulador.crea_contactos()
    simulador.run(numero_dias=22)

if __name__ == "__main__":
    main()
