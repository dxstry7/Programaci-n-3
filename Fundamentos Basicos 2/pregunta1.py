'''
Para este ejercicio debe crear un programa que calcule las estaturas (interos,
dobles) promedio de un salón de clase. El usuario debe de ingresar el número cero (como una
variable sentinela de manera que pueda indicar que ya no desea ingresar mas datos).
Su programa debe mostrar un mensaje de error apropiado si el primer valor ingresado
por el usuario es 0.

El cero no puede hacer parte de las estaturas registradas ni incluido en el promedio de estaturas.
'''

estaturas = float(input("Ingrese la estatura (en metros) de un estudiante (ingrese 0 para terminar):"))
if estaturas == 0:
    print("Error: No se puede calcular el promedio con cero estaturas.")
else:
    suma_estaturas = 0
    contador = 0
    while estaturas != 0:
        suma_estaturas += estaturas
        contador += 1
        estaturas = float(input("Ingrese la estatura (en metros) de un estudiante (Ingrese 0 para terminar): "))
    promedio = suma_estaturas / contador
    print("El promedio de estaturas es:", promedio)