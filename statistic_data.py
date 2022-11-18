import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Statistic:

    def describe(self, data):
        val = np.array([float(col['closingPrice']) for col in data])
        data = pd.DataFrame(val, columns=['Close'])

        plt.subplot(221)
        plt.title('Wykres ciągu')
        plt.ylabel('Wartosc Close')
        plt.xlabel('Dni')
        plt.plot(data.values)

        plt.subplot(222)
        plt.title('Wykres boxplot')
        plt.xlabel('Close')
        plt.boxplot(data)

        plt.subplot(223)
        plt.title('Histogram')
        plt.hist(data)

        plt.show()
