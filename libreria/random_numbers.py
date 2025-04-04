import random_generate as rg

def uniform_samples(size: int, low: int, high: int) -> list:
    print(f"Generating {size} uniform samples between {low} and {high}.")
    return [rg.generate_random_uniform_number(low, high) for _ in range(size)]

def poisson_samples(size: int, lam: float) -> list:
    print(f"Generating {size} Poisson samples with λ={lam}.")
    return [rg.generate_random_poisson_number(lam) for _ in range(size)]

def exponential_samples(size: int, lam: float) -> list:
    print(f"Generating {size} Exponential samples with λ={lam}.")
    return [rg.generate_random_exponential_number(lam) for _ in range(size)]

def normal_samples(size: int, mu: float, sigma: float) -> list:
    print(f"Generating {size} Normal samples with μ={mu} and σ={sigma}.")
    return [rg.generate_random_normal_number(mu, sigma) for _ in range(size)]
