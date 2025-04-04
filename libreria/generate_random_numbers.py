import random
import math

def generate_uniform_numbers(n, lower_bound, upper_bound):
    """
    Generar n numeros random distribuidos uniformemente entre lower_bound y upper_bound.
    
    Parametros:
    n (int): Cantidad de numeros random a generar.
    lower_bound (float): Limite inferior de la distribucion uniforme.
    upper_bound (float): Limite superior de la distribucion uniforme.
    
    Returns:
    list: Lista de n numeros random distribuidos entre lower_bound y upper_bound.
    """
    if lower_bound >= upper_bound:
        raise ValueError("El limite inferior debe ser menor que el limite superior.")
    if n <= 0:
        raise ValueError("La cantidad de numeros a generar debe ser mayor que cero.")
    elif n > 50000:
        raise ValueError("La cantidad de numeros a generar debe ser menor que 50.000.")
    
    return [(lower_bound + random.random*(upper_bound-lower_bound)) for _ in range(n)]


def generate_normal_numbers(n, mean, std_dev):
    """
    Generar n numeros random distribuidos normalmente con la media y la desviacion estandar.
    
    Parameters:
    n (int): Cantidad de numeros random a generar.
    mean (float): Media de la distribucion normal.
    std_dev (float): Desviación estandar de la distribucion estandar.
    
    Returns:
    list: Lista n numeros random distribuidos normalmente con la media y la desviacion estandar.
    """
    if std_dev <= 0:
        raise ValueError("La desviacion estandar debe ser mayor que cero.")
    if n <= 0:
        raise ValueError("La cantidad de numeros a generar debe ser mayor que cero.")
    elif n > 50000:
        raise ValueError("La cantidad de numeros a generar debe ser menor que 50.000.")

    list = []
    for _ in range(n/2):  # Generar pares de números para usar el método Box-Muller
        # Generar dos números aleatorios uniformemente distribuidos entre 0 y 1
        n1 = random.random()
        n2 = random.random()
        # Aplicar la transformación de Box-Muller
        # Generar dos números aleatorios normalmente distribuidos
        z1 = math.sqrt(-2 * math.log(n1)) * math.cos(2 * math.pi * n2)
        z2 = math.sqrt(-2 * math.log(n1)) * math.sin(2 * math.pi * n2)
        list.append(z1 * std_dev + mean, z2 * std_dev + mean)

    return list[:n]  # Asegurarse de que la lista tenga exactamente n elementos

def generate_exponential_numbers(n, rate):
    """
    Generar n numeros random distribuidos exponencialmente con la tasa dada.
    
    Parameters:
    n (int): Cantidad de numeros random a generar.
    rate (float): Tasa de la distribucion exponencial.
    
    Returns:
    list: Lista n numeros random distribuidos exponencialmente con la tasa dada.
    """
    if rate <= 0:
        raise ValueError("La tasa debe ser mayor que cero.")
    if n <= 0:
        raise ValueError("La cantidad de numeros a generar debe ser mayor que cero.")
    elif n > 50000:
        raise ValueError("La cantidad de numeros a generar debe ser menor que 50.000.")
    
    return [(-1 / rate) * math.log(1 - random.random()) for _ in range(n)]

def generate_poisson_numbers(n, lam):
    """
    Generar n numeros random de la distribución Poisson con el lambda dado.
    
    Parameters:
    n (int): Cantidad de numeros random a generar.
    lam (float): Lambda de la distribucion Poisson.
    
    Returns:
    list: Lista n numeros random de la distribución Poisson con el lambda dado.
    """
    if lam <= 0:
        raise ValueError("Lambda debe ser mayor que cero.")
    if n <= 0:
        raise ValueError("La cantidad de numeros a generar debe ser mayor que cero.")
    elif n > 50000:
        raise ValueError("La cantidad de numeros a generar debe ser menor que 50.000.")
    
    list = []
    for _ in range(n):
        A = math.exp(-lam)
        x = -1
        p = 1
        while p >= A:
            x += 1
            p *= random.random()
        list.append(x)
    
    return list