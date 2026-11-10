columnas = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"]

def pedir_datos():
    nombre_departamento = input("Ingrese el nombre del departamento: ")
    limite_registros = int(input("Ingrese el límite de registros a consultar (máximo 500): "))
    return nombre_departamento, limite_registros

def mostrar_resultados(resultado_df):
    if resultado_df.empty:
        print("No se encontraron resultados para el departamento especificado.")
    else:
        df = resultado_df.reindex(columns=columnas).fillna("N/A")
        print("{:<22}{:<15}{:<6}{:<14}{:<12}{}".format(
            "Ciudad", "Departamento", "Edad", "Tipo", "Estado", "País procedencia"))
        for _, f in df.iterrows():
            print("{:<22}{:<15}{:<6}{:<14}{:<12}{}".format(*f))