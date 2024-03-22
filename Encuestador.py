#Respuestas preguntas sobre la teoría:
#1. Encapsulamiento, herencia y polimorfismo.
#2. Una clase es como un molde con ciertas características propias, por ejemplo la clase auto,
# auto tiene varias características propias como 4 ruedas, motor, bencina, etc.
#3. tomando de ejemplo la respuesta anterior, un objeto es un caso específico de un molde, como por ejemplo:
# La clase es auto, el objeto es Nissan, este objeto hereda todos los atributos de la clase Auto, y además
# tiene sus propios atributos.

# Nombres y ruts de los estudiantes:
# Damon Murray 21.012.282-6
# Emilio San Martin 21.484.522-9

#Importamos la clase Profesion1:
from Profesion1 import *
class Encuestador():
    def __init__(self):
        #Creamos una lista que almanecenará los datos de cada persona, para así poder procesarlos:
        self.__personas = []
    #Método que le pide al usuario ingresar sus datos, con sus respectivas restricciones al momento de ingresar los datos:
    def capturar_persona(self):
        print("\nEncuesta de personas")
        nombre = input("\nIngrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        while edad <= 0:
            print("La edad debe ser un número entero mayor a 0.")
            edad = int(input("Ingrese la edad de la persona: "))

        sexo = input("Ingrese el sexo de la persona (M/F/O): ")
        while sexo not in ["M", "F", "O"]:
            print("El sexo debe ser M (masculino), F (femenino) u O (Otro)")
            sexo = input("Ingrese el sexo de la persona (M/F/O): ")

        profesion = input("Elija la profesión de la persona (Ingeniero/Abogado/Otra): ")
        while profesion not in ["Ingeniero", "Abogado", "Otra"]:
            print("La profesión debe ser 'Ingeniero', 'Abogado' u 'Otra'.")
            profesion = input("Elija la profesión de la persona (Ingeniero/Abogado/Otra): ")

        sueldo = float(input("Ingrese el sueldo de la persona: "))

        persona = Profesion1(nombre, edad, sexo, profesion, sueldo)
        self.__personas.append(persona)

    #Método que muestra por pantalla todos los porcentajes y promedios que se pidieron:
    def mostrar_resultados(self):
        total_personas = len(self.__personas)
        porcentaje_ingenieros = sum(1 for persona in self.__personas if persona.profesion == "Ingeniero") / total_personas * 100
        porcentaje_abogados = sum(1 for persona in self.__personas if persona.profesion == "Abogado") / total_personas * 100
        porcentaje_otra = sum(1 for persona in self.__personas if persona.profesion == "Otra") / total_personas * 100

        sueldo_ingenieros = sum(ing.sueldo for ing in self.__personas if ing.profesion == "Ingeniero") / total_personas
        sueldo_abogados = sum(ab.sueldo for ab in self.__personas if ab.profesion == "Abogado") / total_personas
        sueldo_otra = sum(ot.sueldo for ot in self.__personas if ot.profesion == "Otra") / total_personas

        print("\nResultados de la encuesta:")
        print("\nPorcentaje de Ingenieros:", porcentaje_ingenieros)
        print("Porcentaje de Abogados:", porcentaje_abogados)
        print("Porcentaje de otras profesiones:", porcentaje_otra)
        print("\nPromedio de sueldo de Ingenieros:", sueldo_ingenieros)
        print("Promedio de sueldo de Abogados:", sueldo_abogados)
        print("Promedio de sueldo de otras profesiones:", sueldo_otra)

# Función principal
def main():
    encuestador = Encuestador()

    while True:
        encuestador.capturar_persona()
        continuar = input("¿Desea continuar con otra persona? (Si/No): ").lower()
        if continuar != "si":
            break

    encuestador.mostrar_resultados()

if __name__ == "__main__":
    main()
