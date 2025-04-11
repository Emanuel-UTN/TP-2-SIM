from scipy.stats import chi2

def prueba_chi_cuadrado(data, sample_size, bins):
    """
    Perform Chi-squared test on the given data.

    Parameters:
    data (list): The list of random numbers generated.
    sample_size (int): The size of the sample.
    bins (int): The number of bins to use for the histogram.

    Returns:
    None: Prints the result of the Chi-squared test.
    """
    # Evaluar numero aleatorios con chi-cuadrado
    esperado = sample_size / bins
    observado = [0] * bins

    # Count the occurrences in each bin
    for value in data:
        bin_index = int(value // (max(data) / bins))
        if bin_index >= bins:
            bin_index = bins - 1
        observado[bin_index] += 1

    chi_squared = sum((o - esperado) ** 2 / esperado for o in observado)

    # Comparar con el vlor de chi-cuadrado de tabla
    grados_de_libertad = bins - 1
    alpha = 0.05 
    # Chi-squared critical value for 0.05 significance level

    critical_value = chi2.ppf(1 - alpha, grados_de_libertad)

    if chi_squared < critical_value:
        print(f"Chi-squared value: {chi_squared:.2f} =< Critical value: {critical_value:.2f}.")
        print("The null hypothesis is accepted.")
    else:
        print(f"Chi-squared value: {chi_squared:.2f} > Critical value: {critical_value:.2f}.")
        print("The null hypothesis is rejected.")