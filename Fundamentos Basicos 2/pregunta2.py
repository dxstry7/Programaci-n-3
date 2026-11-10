'''
Modifique el ejercicio anterior esta vez en lugar de digitar el número cero para
indicar que se desea parar de ingresar estaturas usted debe de mostrar en pantalla el mensaje
“Desea ingresar mas estaturas [S/N]”. Utilice la respuesta obtenida para detener el ciclo.
'''

estaturas = float(input("Ingrese la estatura (en metros) de un estudiante: "))
if estaturas == 0:
    print("Error: No se puede calcular el promedio con cero estaturas.")
else:
    suma_estaturas = 0
    contador = 0
    while True:
        suma_estaturas += estaturas
        contador += 1
        respuesta = input("Desea ingresar más estaturas? [S/N]: ")
        if respuesta.upper() == 'N':
            break
        estaturas = float(input("Ingrese la estatura (en metros) de un estudiante: "))
    promedio = suma_estaturas / contador
    print("El promedio de estaturas es:", promedio)