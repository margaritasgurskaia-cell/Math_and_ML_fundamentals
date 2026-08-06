import numpy as np

#Перший стовпчик - висота, другий - ширина листків, третій - кількість листків
plants = np.array([
    [30, 3, 5],
    [40, 6, 2],
    [10, 2, 7]
])

print(plants.shape[0])
print(plants.shape[1])