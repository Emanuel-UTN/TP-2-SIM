def validar_ab_uniforme():
    while True:
        try:
            a = float(input("Enter the lower bound for uniform distribution: "))
            b = float(input("Enter the upper bound for uniform distribution: "))
            if a < b:
                return a, b
            else:
                print("Lower bound must be less than upper bound. Please try again.")
        except ValueError:
            print("Please enter valid integers.")

def validar_sample_size():
    while True:
        try:
            sample_size = int(input("Enter the sample size: "))
            if 0 < sample_size <= 50000:
                return sample_size  # Return the validated sample_size
            else:
                print("Sample size must be between 1 and 50000. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")

def validar_lambda(distribution: str):
    while True:
        try:
            lam = float(input("Enter the lambda (λ) for {distribution} distribution: "))
            if lam > 0:
                return lam
            else:
                print("Lambda must be a positive integer. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")

def validar_stdev():
    while True:
        try:
            stdev = float(input("Enter the standard deviation (σ) for Normal distribution: "))
            if stdev > 0:
                return stdev
            else:
                print("Standard deviation must be a positive integer. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")


def validar_bins():
    """Validate the number of bins (must be 10, 15, 20, or 25)."""
    opciones_validas = [10, 15, 20, 25]
    while True:
        try:
            bins = int(input("Enter the number of intervals (10, 15, 20, 25): "))
            if bins in opciones_validas:
                return bins
            else:
                print("Invalid input. Please enter 10, 15, 20, or 25.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def validar_media(distribution: str):
    while True:
        try:
            media = float(input(f"Enter the mean (μ) for {distribution} distribution: "))
            return media
        except ValueError:
            print("Please enter a valid number.")