import pandas as pd

datos = {
    "producto": [
        "Cuaderno", "lapicera", "mochila", "Regla", "Cartuchera", "Calculadora",
        "Auriculares", "Resaltadores", "Goma", "Lapiz"
    ],
    "categoria" : [
        "Libreria", "libreria", "Accesorios", "libreria", "accesorios", "Tecnologia",
        "tecnologia", "Libreria", "Indumentaria", "libreria"
    ],
    "precio" : [3500, 1200, 15000, 800, 9500, 12000, 18000, 2500, 600, 500],
    "cantidad_vendida": [2, 25, 7, 12, 3, 5, 8, 30, 40, 22],
    "sucursal" : [ "Centro", "Centro", "Norte", "Sur", "Norte", "Centro", "Sur", "Centro", 
                  "Sur", "Centro"],
    "forma_pago" : [ "Efectivo", "debito", "Credito", "Efectivo", "Debito", "credito", "Credito",
                    "Debito", "Efectivo", "Debito"],
    "fecha" : [ "2024-03-01", "2024-03-01", "2024-03-02", "2024-03-02",
               "2024-03-03", "2024-03-03", "2024-03-04", "2024-03-04", "2024-03-05",
               "2024-03-05"]
}

df = pd.DataFrame(datos)
#Limpieza categoria
reemplazos ={
    "libreria" : "Libreria", "accesorios" : "Accesorios",
    "tecnologia" : "Tecnologia", "indumentaria" : "Indumentaria"
}

df["categoria_limpia"] = (
    df["categoria"].str.strip().str.lower().replace(reemplazos)
)

#Normalización forma_pago
df["forma_pago"] = df["forma_pago"].str.strip().str.lower()

#Filtro compuesto 

filtro = (df["categoria_limpia"] == "Libreria") & (df["forma_pago"] == "debito") & (df["cantidad_vendida"] >= 20)

resultado_final = df[filtro][["producto", "precio", "sucursal"]]

print(resultado_final)
print(type(resultado_final))
print(resultado_final.shape)