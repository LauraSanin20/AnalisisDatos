# Pasos para Analizar Datos
# 1. Importar el paquete  p paquetes con los que voy a analizar la información

import pandas as pd
from helpers.creacionTabla import crearTabla
from helpers.creacionGraficas import generarGrafica

def analizarCanastaBasica():
    # 2. Sin importar la fuente (sql, xls, JSON, csv...)
    # Crear una tabla tabulada que se llama DATAFRAME

    tabla=pd.read_csv('./data/bdcanasta.csv')

    crearTabla(tabla,"canastabasica")

    #print(tabla)

    # 3. Aplico filtros para limpiar o seleccionar datos
    #Un filtro es un nuevo dataframe y un dataframe es
    # filtroPanes=tabla.query("Nombre Campo o columna que quiero filtrar=='Pan'")
    # para filtrar dos condiciones se separan con and

    #filtroPanes=tabla.query(" (Producto=='Pan') and (Origen=='India') ")
    #print(filtroPanes) para imprimir la variable
    #crearTabla(filtroPanes,"filtropanes") # Para crear tabla con el filtro aplicado

    filtroPrecios=tabla.query("PrecioporUnidad < 50")
    crearTabla(filtroPrecios,"filtroPrecios")

    #print(tabla.head()) # .head muestra los primeros 5 datos

    #print(tabla.head(20)) # imprime los primeros N registros

    #print(tabla.tail()) # imprime los ultimos 5 registros

    #print(tabla.describe()) # Informacion basica descriptiva de todos los datos

    filtroPanes=tabla.query(" (Producto=='Pan')")

    # 4. Graficando los dataframes
    generarGrafica(filtroPanes) 