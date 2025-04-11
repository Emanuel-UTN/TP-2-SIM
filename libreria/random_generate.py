import random
import math

def random_open_0_1():
    """Retorna un número aleatorio en el intervalo [0, 1)."""
    return random.random()

def generate_random_uniform_number(a, b):
    """Genera un número aleatorio uniformemente distribuido entre a y b usando [0, 1)."""
    r = random_open_0_1()
    return a + (b - a) * r

def generate_random_exponential_number(media):
    """Genera un número aleatorio con distribución Exponencial usando [0, 1)."""
    r = random_open_0_1()
    return -media * math.log(r)

def generate_random_normal_number(media, stdev):
    """Genera un número aleatorio con distribución Normal usando [0, 1) y el método Box-Muller."""
    u1 = random_open_0_1()
    u2 = random_open_0_1()
    z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return z1 * stdev + media

def generate_random_poisson_number(lam):
    """Genera un número aleatorio con distribución de Poisson usando [0, 1) y el algoritmo de Knuth."""
    L = math.exp(-lam)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random_open_0_1()
    return k - 1
