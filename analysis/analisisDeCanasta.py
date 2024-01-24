# Pasos para Analizar Datos
# 1. Importar el paquete  p paquetes con los que voy a analizar la información

import pandas as pd

def analizarCanastaBasica():
    # 2. Sin importar la fuente (sql, xls, JSON, csv...)
    # Crear una tabla tabulada que se llama DATAFRAME

    tabla=pd.read_csv('./data/bdcanasta.csv')

    #print(tabla)

    # 3. Aplico filtros para limpiar o seleccionar datos

    #print(tabla.head()) # .head muestra los primeros 5 datos

    #print(tabla.head(20)) # imprime los primeros N registros

    #print(tabla.tail()) # imprime los ultimos 5 registros

    print(tabla.describe()) # Informacion basica descriptiva de todos los datos