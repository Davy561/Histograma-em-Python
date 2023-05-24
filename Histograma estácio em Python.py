import numpy as np
import matplotlib.pyplot as plt

media = 20
desvio_padrao = 2

pontos = np.random.normal(media, desvio_padrao, 1000)

plt.hist(pontos, bins=30, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma - Estácio')
plt.show()