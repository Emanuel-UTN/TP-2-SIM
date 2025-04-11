import libreria.random_generate as rg

def uniform_samples(size: int, low: int, high: int) -> list:
    print(f"Generando {size} muestras uniformes entre {low} y {high}.")
    return [rg.generate_random_uniform_number(low, high) for _ in range(size)]

def poisson_samples(size: int, lam: float) -> list:
    print(f"Generando {size} muestras de Poisson con λ={lam}.")
    return [rg.generate_random_poisson_number(lam) for _ in range(size)]

def exponential_samples(size: int, lam: float) -> list:
    print(f"Generando {size} muestras Exponenciales con λ={lam}.")
    return [rg.generate_random_exponential_number(lam) for _ in range(size)]

def normal_samples(size: int, mu: float, sigma: float) -> list:
    print(f"Generando {size} muestras Normales con μ={mu} y σ={sigma}.")
    return [rg.generate_random_normal_number(mu, sigma) for _ in range(size)]
