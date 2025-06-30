import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 1  # Radio del círculo
n_terms = 10  # Número de términos en la serie de Fourier
theta = np.pi / 2  # Ángulo de rotación (90 grados)

# Crear el vector de tiempo
t = np.linspace(0, 2 * np.pi, 1000)

# Inicializar las coordenadas x y y del círculo
x_approx = np.zeros_like(t)
y_approx = np.zeros_like(t)

# Sumar los términos de Fourier (coseno y seno)
for n in range(1, n_terms + 1):
    x_approx += (r / n) * np.cos(n * t)  # Componente coseno
    y_approx += (r / n) * np.sin(n * t)  # Componente seno

# Aplicar rotación de 90 grados
x_rot = np.cos(theta) * x_approx - np.sin(theta) * y_approx
y_rot = np.sin(theta) * x_approx + np.cos(theta) * y_approx

# Graficar el resultado
plt.figure(figsize=(6, 6))
plt.plot(x_rot, y_rot, label=f'Aproximación con {n_terms} términos')
plt.title('Aproximación de una medusa usando Fourier (Rotado 90 grados)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()














