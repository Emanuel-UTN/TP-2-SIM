import random
import math

def random_open_0_1():
    """Return a random number in the interval [0, 1)."""
    return random.random()

def generate_random_uniform_number(a, b):
    """Generate a random number uniformly between a and b using [0, 1)."""
    r = random_open_0_1()
    return a + (b - a) * r

def generate_random_exponential_number(media):
    """Generate a random number from an Exponential distribution using [0, 1)."""
    r = random_open_0_1()
    return -media * math.log(r)

def generate_random_normal_number(media, stdev):
    """Generate a random number from a Normal distribution using [0, 1) and Box-Muller."""
    u1 = random_open_0_1()
    u2 = random_open_0_1()
    z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return z1 * stdev + media

def generate_random_poisson_number(lam):
    """Generate a random number from a Poisson distribution using [0, 1) and Knuth's algorithm."""
    L = math.exp(-lam)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random_open_0_1()
    return k - 1
