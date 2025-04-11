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
from libreria.validacion import prueba_chi_cuadrado

sample_size = validar_sample_size()
distribution_type = input("Enter distribution (u -> uniform, p -> poisson, e -> exponential, n -> normal): ").strip().lower()

while distribution_type not in ['u', 'p', 'e', 'n']:
    print("Invalid input. Please enter 'u', 'p', 'e', or 'n'.")
    distribution_type = input("Enter distribution (u -> uniform, p -> poisson, e -> exponential, n -> normal): ").strip().lower()

bins = validar_bins()

data = visualizations(distribution_type=distribution_type, sample_size=sample_size, bins=bins)

prueba_chi_cuadrado(data=data, sample_size=sample_size, bins=bins)