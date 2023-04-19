import math

# Definimos la función a integrar
def f(x):
    return 1 + math.exp(-x) * math.sin(4*x)

# Definimos los límites de integración
a = 0
b = 1

# Definimos el número de intervalos 
n = 6

# Calculamos el ancho de los intervalos
h = (b - a) / n

# Calculamos los puntos intermedios
x1 = a + h
x2 = a + 2 * h
x3 = a + 3 * h
x4 = a + 4 * h
x5 = a + 5 * h
x6 = a + 6 * h

# Calculamos la integral usando la fórmula de Simpson 3/8
integral = (3 * h / 8) * (f(a) + 3 * f(x1) + 3 * f(x2) + 2 * f(x3) + 3 * f(x4) + 3 * f(x5) + f(x6))


# Imprimimos el resultado
print("La integral de 1+e^-xsin(4x) de 0 a 1 es:", integral)