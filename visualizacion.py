from random_numbers import uniform_samples, poisson_samples, exponential_samples, normal_samples 
from validador import validar_ab_uniforme, validar_sample_size, validar_lambda, validar_stdev, validar_bins, validar_media
import matplotlib.pyplot as plt
import numpy as np


def visualizations(distribution: str, sample_size: int) -> None:
    plt.figure(figsize=(8, 6))
    bins = validar_bins()

    if distribution == 'uniform':
        a, b = validar_ab_uniforme()
        data = uniform_samples(sample_size, a, b)
        title = f'Uniform Distribution ({a}-{b})'
    elif distribution == 'poisson':
        media = validar_lambda(distribution)
        data = poisson_samples(sample_size, media)
        title = f'Poisson Distribution (λ={media})'
        bins = range(0, max(data) + 2)  # bins must be integers
    elif distribution == 'exponential':
        media = validar_lambda(distribution)
        data = exponential_samples(sample_size, media)
        title = f'Exponential Distribution (λ={media})'
    elif distribution == 'normal':
        media = validar_media(distribution)
        stdev = validar_stdev()
        data = normal_samples(sample_size, media, stdev)
        title = f'Normal Distribution (μ={media}, σ={stdev})'
    else:
        print("Invalid distribution type. Choose 'uniform', 'poisson', 'exponential', or 'normal'.")
        return

    plt.hist(data, bins=bins, alpha=0.7)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f'{distribution}_distribution.png')
    plt.show()
