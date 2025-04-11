def validar_ab_uniforme():
    while True:
        try:
            a = float(input("Ingrese el límite inferior para la distribución uniforme: "))
            b = float(input("Ingrese el límite superior para la distribución uniforme: "))
            if a < b:
                return a, b
            else:
                print("El límite inferior debe ser menor que el límite superior. Por favor intente de nuevo.")
        except ValueError:
            print("Por favor ingrese números válidos.")

def validar_sample_size():
    while True:
        try:
            sample_size = int(input("Ingrese el tamaño de la muestra: "))
            if 0 < sample_size <= 50000:
                return sample_size  # Retorna el tamaño de muestra validado
            else:
                print("El tamaño de la muestra debe estar entre 1 y 50000. Por favor intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número entero válido.")

def validar_lambda(distribution: str):
    while True:
        try:
            lam = float(input(f"Ingrese el lambda (λ) para la distribución {distribution}: "))
            if lam > 0:
                return lam
            else:
                print("Lambda debe ser un número positivo. Por favor intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def validar_stdev():
    while True:
        try:
            stdev = float(input("Ingrese la desviación estándar (σ) para la distribución Normal: "))
            if stdev > 0:
                return stdev
            else:
                print("La desviación estándar debe ser un número positivo. Por favor intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número válido.")


def validar_bins():
    """Valida el número de intervalos (debe ser 10, 15, 20, o 25)."""
    opciones_validas = [10, 15, 20, 25]
    while True:
        try:
            bins = int(input("Ingrese el número de intervalos (10, 15, 20, 25): "))
            if bins in opciones_validas:
                return bins
            else:
                print("Entrada inválida. Por favor ingrese 10, 15, 20, o 25.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

def validar_media(distribution: str):
    while True:
        try:
            media = float(input(f"Ingrese la media (μ) para la distribución {distribution}: "))
            return media
        except ValueError:
            print("Por favor ingrese un número válido.")