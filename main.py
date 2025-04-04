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
from validador import validar_sample_size 
sample_size = validar_sample_size()
distribution_type = input("Enter distribution (uniform, poisson, exponential, normal): ").strip().lower()
visualizations(distribution_type, sample_size)
