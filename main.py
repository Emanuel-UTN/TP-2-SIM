# from visualizacion import visualizations

# # Tamaño de muestra global
# sample_size = 1000
# # Bucle principal del programa
# while True:
#     distribution_type = input("Ingrese el tipo de distribución (uniforme, poisson, exponencial, normal): ").strip().lower()
#     if distribution_type in ['uniforme', 'poisson', 'exponencial', 'normal']:
#         visualizations(distribution_type, sample_size)
#         break
#     else:
#         print("Tipo de distribución inválida. Por favor ingrese 'uniforme', 'poisson', 'exponencial', o 'normal'.")

from excel_generator import visualizations
from validador import validar_sample_size, validar_bins
from libreria.validador_chi import prueba_chi_cuadrado

tamanio_muestra = validar_sample_size()
tipo_distribucion = input("Ingrese distribución (u -> uniforme, p -> poisson, e -> exponencial, n -> normal): ").strip().lower()

while tipo_distribucion not in ['u', 'p', 'e', 'n']:
    print("Entrada inválida. Por favor ingrese 'u', 'p', 'e', o 'n'.")
    tipo_distribucion = input("Ingrese distribución (u -> uniforme, p -> poisson, e -> exponencial, n -> normal): ").strip().lower()

intervalos = validar_bins()

datos = visualizations(distribution_type=tipo_distribucion, sample_size=tamanio_muestra, bins=intervalos)

prueba_chi_cuadrado(data=datos, sample_size=tamanio_muestra, bins=intervalos)