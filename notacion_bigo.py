import matplotlib.pyplot as plt
import numpy as np

# valores entrada
n = np.linspace(1, 7, 50)  

# notacion big o
O_1 = np.ones_like(n)
O_log_n = np.log(n)
O_n = n
O_n_log_n = n * np.log(n)
O_n_squared = n**2
O_2_power_n = 2**n

# crear gráfica
plt.figure(figsize=(10, 6))

plt.plot(n, O_1, label='O(1)', linestyle='--')
plt.plot(n, O_log_n, label='O(log n)', linestyle='--')
plt.plot(n, O_n, label='O(n)', linestyle='--')
plt.plot(n, O_n_log_n, label='O(n log n)', linestyle='--')
plt.plot(n, O_n_squared, label='O(n^2)', linestyle='--')
plt.plot(n, O_2_power_n, label='O(2^n)', linestyle='--')

# etiquetas
plt.xlabel('Tamaño del problema (n)')
plt.ylabel('Complejidad')
plt.title('Escala de notación Big O')
plt.legend()

# mostrar gráfica
plt.grid(True)
plt.show()
