from pymongo import MongoClient
from security import Security


class DataBase:
    def __init__(self, security):
        self.__client = None
        self.__db = None
        self.__colect = None
        self.__security = security

    def conect(self, path):
        try:
            self.__client = MongoClient(
                path
            )

            self.__db = self.__client['db']
            self.__colect = self.__db['db']
        except Exception as ex:
            print(ex)
            exit(-6)

    def push(self, data):
        try:
            for i in range(len(data)):
                self.__colect.insert_one(
                    {
                        'day': self.__security.encrypt(data[i][0]),
                        'closingPrice': self.__security.encrypt(data[i][1])
                    }
                )
        except Exception as ex:
            print(ex)
            exit(-4)

    def load_data(self):
        data = []

        for row in self.__colect.find():
            try:
                new_row = {
                    'day': self.__security.decrypt(row['day']),
                    'closingPrice': float(self.__security.decrypt(row['closingPrice'])),
                    }
            except Exception:
                continue

            data.append(new_row)

        return data

    def clear(self):
        try:
            db = self.__colect.find()
            if db:
                for row in db:
                    self.__colect.remove(row)
        except Exception as er:
            print(er)
            exit(-5)
