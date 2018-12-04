import matplotlib.pyplot as plt
import numpy as np

irisData = np.genfromtxt('..\irisdata.csv', delimiter=',', skip_header=1,
                         names=['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species'])

plt.plot(irisData['sepalLength'], irisData['species'])
plt.show()
