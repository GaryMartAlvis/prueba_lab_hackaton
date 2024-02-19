def calcular_promedios(verbales: str, numericas: str) -> int:
    # Valores string ingredados guardarlos en lista con su conversion a entero
    lista_verbales = list(map(int, verbales.split()))
    lista_numericas = list(map(int, numericas.split()))

    # Funcion lambda (Alternativa a for in)
    # Recorre dos listas dadas y realiza la suma de sus valores en sus respectivas posiciones
    suma_valores_lista = lambda lista1, lista2: lista1 + lista2

    # Suma de valores de lista utilizando la funcion lambda declara en la anterior linea, conversion de resultado a lista
    lista_consolidada = list(map(suma_valores_lista, lista_verbales, lista_numericas))

    # Calculo de valor promedio
    promedio = sum(lista_consolidada) / len(lista_consolidada)

    # Funcion lambda (Alternativa a for in)
    # Recorre una lista e identifica los valores mayores al promedio para guardarlos en una lista independiente esos valores filtrados
    casos_menores_promedio = list(filter(lambda menores_promedio: menores_promedio < promedio, lista_consolidada))

    # Cuenta de valores superiores al promedio
    resultado = len(casos_menores_promedio)

    return resultado
