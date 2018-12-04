import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_path = '..\irisdata.csv'

types = [float, float, float, float, str]
data = np.genfromtxt(data_path, delimiter=',', dtype=types,
                     names=['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species'], skip_header=1)
isNotVirginicaOrVersicolor = [data.species == 'setosa']
relevantData = pd.DataFrame.filter(data)

plt.scatter(data['petalLength'], data['petalWidth'])
plt.show()
