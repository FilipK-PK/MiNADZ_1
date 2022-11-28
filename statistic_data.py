import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m

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

        plt.subplot(224)
        plt.title('Autokorelacja')
        plt.plot(self.corel(data))

        plt.show()

    def corel(self, data_old, abs=False, len_w=False):
        correlation_data = []

        data = data_old.copy()
        data = data.values.reshape(-1)
        data = self.__norm(self.__steps(data))

        if not len_w:
            if abs:
                [correlation_data.append(np.corrcoef(np.absolute(data[0:-1 - i]), np.absolute(data[i:-1]))[0, 1]) for i
                 in
                 range(data.shape[0] // 2)]

            else:
                [correlation_data.append(np.corrcoef(data[0:-1 - i], data[i:-1])[0, 1]) for i in
                 range(data.shape[0] // 2)]
        else:
            if abs:
                [correlation_data.append(np.corrcoef(np.absolute(data[0:-1 - i]), np.absolute(data[i:-1]))[0, 1]) for i
                 in
                 range(len_w)]

            else:
                [correlation_data.append(np.corrcoef(data[0:-1 - i], data[i:-1])[0, 1]) for i in range(len_w)]

        return correlation_data
    def __steps(self, data, rand=False):
        if rand:
            d = []
            for i in range(1, data.size):
                try:
                    d.append(m.log(data[i + 1] - data[i]))
                except Exception:
                    d.append(0.0)

            return np.array(d)

        return np.log(data[1:] / data[:-1])

    def __norm(self, data):
        return (data - data.mean()) / data.std()
