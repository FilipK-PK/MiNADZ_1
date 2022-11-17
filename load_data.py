import requests
from bs4 import BeautifulSoup
import matplotlib.pylab as plt
import numpy as np
import csv


PATH = "https://www.biznesradar.pl/notowania-historyczne/CD-PROJEKT"


class LoadData:
    def __init__(self):
        pass

    def load(self):
        data = []

        # pobieranie danych z pod stron
        for index in range(1, 2):
            try:
                # pobieranie strony
                file_html = requests.get(PATH + ',' + str(index))

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
                    float(tab_data[i + 4].text)
                ])

        return data
