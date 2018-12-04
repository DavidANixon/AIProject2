import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_path = '..\irisdata.csv'

types = [float, float, float, float, str]
data = np.genfromtxt(data_path, delimiter=',', dtype=types,
                     names=['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'species'], skip_header=1)

isVirginicaOrVersicolor = [data['species'] != 'setosa']
dataframe = pd.Series(data)
relevantData = dataframe.loc[dataframe['species' != 'setosa']]

plt.scatter(relevantData['petalLength'], relevantData['petalWidth'])
plt.show()
