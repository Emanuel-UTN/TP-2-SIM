from scipy.stats import chi2

def prueba_chi_cuadrado(data, sample_size, bins):
    """
    Realiza la prueba Chi-cuadrado en los datos proporcionados.

    Parámetros:
    data (list): La lista de números aleatorios generados.
    sample_size (int): El tamaño de la muestra.
    intervalos (int): El número de intervalos a utilizar para el histograma.

    Retorna:
    None: Imprime el resultado de la prueba Chi-cuadrado.
    """
    # Evaluar números aleatorios con chi-cuadrado
    intervalos = bins
    esperado = sample_size / intervalos
    observado = [0] * intervalos

    # Contar las ocurrencias en cada intervalo
    for value in data:
        intervalos_index = int(value // (max(data) / intervalos))
        if intervalos_index >= intervalos:
            intervalos_index = intervalos - 1
        observado[intervalos_index] += 1

    for i in range(intervalos):
        print(f"Intervalo {i + 1}: Observado = {observado[i]}, Esperado = {esperado}")
    chi_squared = sum(((o - esperado) ** 2) / esperado for o in observado)

    # Comparar con el valor de chi-cuadrado de tabla
    grados_de_libertad = intervalos - 1
    alpha = 0.05 
    # Valor crítico Chi-cuadrado para nivel de significancia 0.05

    critical_value = chi2.ppf(1 - alpha, grados_de_libertad)

    if chi_squared < critical_value:
        print(f"Valor Chi-cuadrado: {chi_squared:.2f} =< Valor crítico: {critical_value:.2f}.")
        print("La hipótesis nula es aceptada.")
    else:
        print(f"Valor Chi-cuadrado: {chi_squared:.2f} > Valor crítico: {critical_value:.2f}.")
        print("La hipótesis nula es rechazada.")