from database import DataBase
import keys, numpy as np
from load_data import LoadData
from statistic_data import Statistic

PATH = f"mongodb+srv://MiNADZ:{keys.PASSWORD}@atlascluster.y8etfyq.mongodb.net/?retryWrites=true&w=majority"


if __name__ == "__main__":
   db = DataBase()
   db.conect(PATH)

   http = LoadData()
   data = http.load()

   db.push(data)

   #print rekordów z bazy danych
   db.printAll()

   # statystyki
   Statistic().describe(db.load_data())
