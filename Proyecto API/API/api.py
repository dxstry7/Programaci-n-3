import pandas as pd
from sodapy import Socrata

def consultar_casos_covid(nombre_departamento, limite_registros): #Se define la función para consultar los casos de covid
    client = Socrata("www.datos.gov.co", None) #Se crea el cliente para conectarse a la API de datos abiertos de Colombia
    if limite_registros > 500: #Evitar que se cuelgue la llamada 
        print("El límite máximo de registros es 500. Se establecerá en 500.")
        limite_registros = 500
    result = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom = nombre_departamento.upper()) #Se especifica la base de datos, el limite de registros y el nombre del departamento

    result_df = pd.DataFrame.from_records(result)
    return result_df
