import matplotlib.pyplot as plt
def generarGrafica(dataFrame):
    # Agrupar datos del dataframe segun el analisis que quiere
    # Estadisticas de un alimento (pan) por pais y su promedio al año
    # El el parentesis se pone el dato que va en el eje X
    # En el corchete se pone el dato que va en el eje Y
    # mean() para capturar la media

    preciosPromedioPais=dataFrame.groupby('Origen')['PrecioporUnidad'].mean()
    print(preciosPromedioPais)

    # 0. Generando lista de colores
    colores=["#E933FF","#751381","#DC7EE7"]

    # 1. Generar una figura
    plt.figure(figsize=(10,10))

    # 2. Genero la grafica que deseo, bar es grafica de barras
    #index es origen y values es precio
    plt.bar(preciosPromedioPais.index, preciosPromedioPais.values, color=colores)

    # 3. Muestro la grafica
    #plt.show()

    # 4. Agrego titulo a la grafica
    plt.title("Ventas promedio de panes por paises") #siembre e arboles promedio por municipio por ejemplo

    # 5. Etiqueta o nombre del eje X
    plt.xlabel("Paises")

    # 6. Etiqueta o nombre del eje Y
    plt.ylabel("Precio promedio")

    # 7. Activar el grid
    plt.grid(True)

    # 8. Rotar los labels
    plt.xticks(rotation=45)

    # 9. Guardando nuestra grafica
    plt.savefig("./graphs/promediopanes.png")

    # 
    