from scipy.stats import uniform, norm, expon, poisson, chi2
import numpy as np

def prueba_chi_cuadrado(data, sample_size, cant_intervalos, distribucion_teorica="uniforme", **kwargs):
    """
    Realiza una prueba Chi-cuadrado para verificar si los datos siguen una distribución teórica.
    
    Parámetros:
    - data: lista de números generados.
    - sample_size: tamaño de la muestra.
    - cant_intervalos: cantidad de intervalos (bins).
    - distribucion_teorica: distribución esperada ("u"=uniforme, "n"=normal, "e"=exponencial, "p"=poisson).
    - kwargs: parámetros extra para la distribución (ej: media, sigma, lambda, etc.).
    """
    
    # Inicializar observados en 0
    observados = [0] * cant_intervalos
    min_valor = min(data)
    max_valor = max(data)

    # Calcular los bordes de los intervalos (bins)
    limites = np.linspace(min_valor, max_valor, cant_intervalos + 1)

    # Contar cuántos datos caen en cada intervalo
    for num in data:
        for i in range(cant_intervalos):
            if limites[i] <= num < limites[i + 1] or (i == cant_intervalos - 1 and num == limites[i + 1]):
                observados[i] += 1
                break

    # === CASO POISSON ===
    if distribucion_teorica == "p":
        mu = kwargs.get("mu", np.mean(data))
        
        # Agrupar observados por valor entero
        max_k = int(max(data))
        conteo_por_valor = np.bincount([int(x) for x in data], minlength=max_k + 1)
        observados = conteo_por_valor[:cant_intervalos]
        
        # Calcular frecuencias esperadas usando la función PMF de Poisson
        esperados = [sample_size * poisson.pmf(k, mu) for k in range(cant_intervalos)]
        
        # Calcular estadístico Chi-cuadrado
        chi_squared = sum(((o - e) ** 2) / e for o, e in zip(observados, esperados) if e > 0)
        grados_libertad = cant_intervalos - 1
        valor_critico = chi2.ppf(0.95, grados_libertad)
        
        print("\n--- Distribución: Poisson ---")
        for i, (o, e) in enumerate(zip(observados, esperados)):
            print(f"k = {i}: Observado = {o}, Esperado = {e:.2f}")
    
    # === CASO UNIFORME / NORMAL / EXPONENCIAL ===
    else:
        # Selección de la distribución teórica
        if distribucion_teorica == "u":
            dist = uniform(loc=min_valor, scale=max_valor - min_valor)
        elif distribucion_teorica == "n":
            media = kwargs.get("media", np.mean(data))
            sigma = kwargs.get("sigma", np.std(data))
            dist = norm(loc=media, scale=sigma)
        elif distribucion_teorica == "e":
            lambd = kwargs.get("lambd", 1 / np.mean(data))
            dist = expon(scale=1 / lambd)
        else:
            raise ValueError("Distribución no reconocida (usar 'u', 'n', 'e' o 'p').")
        
        # Calcular frecuencias esperadas usando la CDF
        esperados = []
        for i in range(cant_intervalos):
            probabilidad_intervalo = dist.cdf(limites[i + 1]) - dist.cdf(limites[i])
            esperados.append(probabilidad_intervalo * sample_size)

        # Calcular estadístico Chi-cuadrado
        chi_squared = sum(((o - e) ** 2) / e for o, e in zip(observados, esperados) if e > 0)
        grados_libertad = cant_intervalos - 1
        valor_critico = chi2.ppf(0.95, grados_libertad)

        print(f"\n--- Distribución teórica: {distribucion_teorica.upper()} ---")
        for i in range(cant_intervalos):
            print(f"[{limites[i]:.2f}, {limites[i + 1]:.2f}): Observado = {observados[i]}, Esperado = {esperados[i]:.2f}")

    # === Resultado final ===
    print("\n--- Resultado de la prueba ---")
    if chi_squared < valor_critico:
        print(f"Valor Chi-cuadrado: {chi_squared:.2f} <= Valor crítico: {valor_critico:.2f}")
        print("✅ La hipótesis nula es **aceptada** (los datos se ajustan a la distribución esperada).")
    else:
        print(f"Valor Chi-cuadrado: {chi_squared:.2f} > Valor crítico: {valor_critico:.2f}")
        print("❌ La hipótesis nula es **rechazada** (los datos **no** se ajustan a la distribución esperada).")
