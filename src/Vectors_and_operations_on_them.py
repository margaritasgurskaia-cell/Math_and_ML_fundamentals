import numpy as np

plants = np.array([40, 15, 10]) #перший компонент - висота, другий - кіл-сть листків, третій - ширина листка
remake = np.array([2, 1, 0]) #поправки

print(plants + remake)