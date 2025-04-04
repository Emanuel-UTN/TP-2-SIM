# TP-2-SIM

# Ejecucion
- Para la ejecucuion
    ´pip install -r requirements.txt´

- Ejecutar main.py y se genera un .xlsx con dos hojas, uno con los numeros y otra con el grafico

# Consigna 
 - Realizar una librería que proporcione (mediante funciones o métodos) la funcionalidad necesaria
para generar valores de variables aleatorias para las siguientes distribuciones: uniforme, exponencial,
poisson y normal.
El usuario debe poder ingresar los parámetros de las distribuciones y la cantidad de valores a generar
(hasta 50000). Los valores generados deben poder ser visualizados de alguna manera.

Funciones libreria 'random_number.py':
    uniform_samples(size, low, high)
    poisson_samples(size, lam)
    exponential_samples(size, lam)
    normal_samples(size, mu, sigma)

 - Realizar un programa que grafique las distribuciones anteriores utilizando la librería pedida en el
punto anterior. (La gráfica se aceptará que se genere en base a un archivo de salida del programa, en
Excel).
La cantidad de intervalos de la gráfica debe ingresarse por parámetro. Y se deberá realizar pruebas
de los generadores (Chi-Cuadrado o alguna otra)
