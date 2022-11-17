import requests
from bs4 import BeautifulSoup
import matplotlib.pylab as plt
import numpy as np
import csv
# mongodb+srv://MiNADZ:<password>@cluster0.cr3iapl.mongodb.net/?retryWrites=true&w=majority

if __name__ == "__main__":
    path = "https://www.biznesradar.pl/notowania-historyczne/CD-PROJEKT"

    data = []

    # pobieranie danych z pod stron
    for index in range(1, 1000):
        try:
            # pobieranie strony
            file_html = requests.get(path + ',' + str(index))

            # wyciaganie danych i separowanie
            soup = BeautifulSoup(file_html.text, 'html.parser')
            table = soup.find_all("table", class_="qTableFull")[0]
            print(index)
        except Exception:
            break

        # wyciaganie tabeli tabeli z data i w.close
        tab_data = table.select('td')

        # zapis odpowiednich kolumn
        for i in range(0, len(tab_data), 7):
            data.append([
                    tab_data[i].text,
                    float(tab_data[i+4].text)
                ])

    if len(data):
        data = data[::-1]
        # zapisanie danych doo csv
        with open('data.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Close'])
            writer.writerows(data)

        # wyswietlanie danych
        plt.plot([i[0] for i in data], [i[1] for i in data])
        plt.xticks(np.arange(0, len(data), len(data) // 5))
        plt.show()
