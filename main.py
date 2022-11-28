from database import DataBase
import keys
from load_data import LoadData
from statistic_data import Statistic
from security import Security


PATH = f'mongodb+srv://Filip_PK:{keys.PASSWORD}@cluster0.ypawun1.mongodb.net/?retryWrites=true&w=majority'
PATH_AES = 'key_aes.bin'

if __name__ == "__main__":
   secur = Security(PATH_AES)

   db = DataBase(secur)
   db.conect(PATH)

   # ladniejszy wyglad
   db.clear()

   # pobieranie http
   http = LoadData()
   data = http.load()

   # zapis danych
   db.push(data)

   # statystyki
   Statistic().describe(db.load_data())
