from libreria.random_numbers import uniform_samples, poisson_samples, exponential_samples, normal_samples 
from validador import validar_ab_uniforme, validar_sample_size, validar_lambda, validar_stdev, validar_bins, validar_media
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as ExcelImage
import numpy as np
import os

def visualizations(distribution_type: str, sample_size: int, bins: int = None) -> list:
    plt.figure(figsize=(8, 6))
    if bins is None:
        bins = validar_bins()

    if distribution_type == 'u':
        a, b = validar_ab_uniforme()
        data = uniform_samples(sample_size, a, b)
        title = f'Distribución Uniforme ({a}-{b})'
    elif distribution_type == 'p':
        media = validar_lambda("poisson")
        data = poisson_samples(sample_size, media)
        title = f'Distribución de Poisson (λ={media})'
        bins = range(0, max(data) + 2)
    elif distribution_type == 'e':
        media = validar_lambda("exponencial")
        data = exponential_samples(sample_size, media)
        title = f'Distribución Exponencial (λ={media})'
    elif distribution_type == 'n':
        media = validar_media("normal")
        stdev = validar_stdev()
        data = normal_samples(sample_size, media, stdev)
        title = f'Distribución Normal (μ={media}, σ={stdev})'
    else:
        print("Tipo de distribución inválido. Elija 'u', 'p', 'e', o 'n'.")
        return []

    # Graficar y guardar figura
    plt.hist(data, bins=bins, alpha=0.7)
    plt.title(title)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    image_filename = f'temporal_{distribution_type}_distribution.png'
    plt.savefig(image_filename)
    plt.close()

    # Crear directorio si no existe
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Guardar datos en archivo Excel
    excel_filename = fr'{output_dir}/{distribution_type}_output.xlsx'
    df = pd.DataFrame({f'{distribution_type}_valores': data})
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Datos')

    # Reabrir para añadir imagen en nueva hoja
    wb = load_workbook(excel_filename)
    ws_chart = wb.create_sheet('Gráfico')
    img = ExcelImage(image_filename)
    img.anchor = 'A1'
    ws_chart.add_image(img)
    wb.save(excel_filename)
    
    # Asegurarse de volver al directorio original
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Obtener ruta absoluta completa al archivo Excel para enlace clickeable
    abs_path = os.path.abspath(excel_filename)
    formatted_path = abs_path.replace(os.sep, '/')
    url_path = formatted_path.replace(' ', '%20')
    print(f"Archivo Excel creado en: file:// {url_path}")
    # Eliminar imagen temporal
    if os.path.exists(image_filename):
        os.remove(image_filename)    
    return data
