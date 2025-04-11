from libreria.random_numbers import uniform_samples, poisson_samples, exponential_samples, normal_samples 
from validador import validar_ab_uniforme, validar_sample_size, validar_lambda, validar_stdev, validar_bins
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as ExcelImage
import numpy as np
import os

def visualizations(distribution: str, sample_size: int) -> None:
    plt.figure(figsize=(8, 6))
    bins = validar_bins()

    if distribution == 'uniform':
        a, b = validar_ab_uniforme()
        data = uniform_samples(sample_size, a, b)
        title = f'Uniform Distribution ({a}-{b})'
    elif distribution == 'poisson':
        media = validar_lambda()
        data = poisson_samples(sample_size, media)
        title = f'Poisson Distribution (λ={media})'
        bins = range(0, max(data) + 2)
    elif distribution == 'exponential':
        media = validar_lambda()
        data = exponential_samples(sample_size, media)
        title = f'Exponential Distribution (λ={media})'
    elif distribution == 'normal':
        media = validar_lambda()
        stdev = validar_stdev()
        data = normal_samples(sample_size, media, stdev)
        title = f'Normal Distribution (μ={media}, σ={stdev})'
    else:
        print("Invalid distribution type. Choose 'uniform', 'poisson', 'exponential', or 'normal'.")
        return

    # Plot and save figure
    plt.hist(data, bins=bins, alpha=0.7)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    image_filename = f'{distribution}_distribution.png'
    plt.savefig(image_filename)
    plt.close()

    # Crear directorio si no existe
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    os.chdir(output_dir)

    # Save data to Excel file
    excel_filename = fr'{output_dir}\{distribution}_output.xlsx'
    df = pd.DataFrame({f'{distribution}_values': data})
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Data')

    # Reopen to add image in new sheet
    wb = load_workbook(excel_filename)
    ws_chart = wb.create_sheet('Chart')
    img = ExcelImage(image_filename)
    img.anchor = 'A1'
    ws_chart.add_image(img)
    wb.save(excel_filename)

    print(f"Excel file '{excel_filename}' created with data and chart.")
