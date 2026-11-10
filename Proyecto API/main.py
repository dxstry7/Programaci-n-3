from API.api import consultar_casos_covid
from UI.ui import pedir_datos, mostrar_resultados

departamento, limite = pedir_datos()
resultado = consultar_casos_covid(departamento, limite)

if resultado.empty:
    print("No se encontraron resultados para el departamento especificado.")
else:
    mostrar_resultados(resultado)
