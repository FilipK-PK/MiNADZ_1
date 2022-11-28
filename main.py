from database import DataBase
import keys
from load_data import LoadData
from statistic_data import Statistic
from securyty import Securyty


PATH = f'mongodb+srv://Filip_PK:{keys.PASSWORD}@cluster0.ypawun1.mongodb.net/?retryWrites=true&w=majority'


if __name__ == "__main__":
   db = DataBase()
   db.conect(PATH)

   secur = Securyty()

   # ladniejszy wyglad
   db.clear()

   http = LoadData()
   data = http.load()

   db.push(data, secur.key)

   #print rekordów z bazy danych
   db.printAll()

   # statystyki
   Statistic().describe(db.load_data(secur.key))
