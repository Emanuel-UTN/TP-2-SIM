# from visualizacion import visualizations

# # Global sample size
# sample_size = 1000
# # Main program loop
# while True:
#     distribution_type = input("Enter the distribution type (uniform, poisson, exponential, normal): ").strip().lower()
#     if distribution_type in ['uniform', 'poisson', 'exponential', 'normal']:
#         visualizations(distribution_type, sample_size)
#         break
#     else:
#         print("Invalid distribution type. Please enter 'uniform', 'poisson', 'exponential', or 'normal'.")

from excel_generator import visualizations
from validador import validar_sample_size, validar_bins
import pandas as pd
import xlsxwriter

sample_size = validar_sample_size()
distribution_type = input("Enter distribution (u -> uniform, p -> poisson, e -> exponential, n -> normal): ").strip().lower()

while distribution_type not in ['u', 'p', 'e', 'n']:
    print("Invalid input. Please enter 'u', 'p', 'e', or 'n'.")
    distribution_type = input("Enter distribution (u -> uniform, p -> poisson, e -> exponential, n -> normal): ").strip().lower()

bins = validar_bins()

data = visualizations(distribution_type=distribution_type, sample_size=sample_size, bins=bins)

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