from pymongo import MongoClient
from securyty import Securyty


class DataBase:
    def __init__(self):
        self.__client = None
        self.__db = None
        self.__colect = None

    def conect(self, path):
        try:
            self.__client = MongoClient(
                path
            )

            self.__db = self.__client['db']
            self.__colect = self.__db['db']
        except Exception as ex:
            print(ex)
            exit(-1)

    def push(self, data, key):
        secury = Securyty()
        try:
            for i in range(len(data)):
                self.__colect.insert_one(
                    {
                        'day': secury.encrypt(data[i][0], key),
                        'closingPrice': secury.encrypt(data[i][1], key)
                    }
                )
        except Exception as ex:
                print(ex)
                exit(-1)

    def printAll(self):
        for doc in self.__colect.find():
            print(doc)

    def load_data(self, key):
        secur = Securyty()

        return list(
            {
                i[0], secur.decrypt(i[1], key)
            } for i in self.__colect.find()
        )

    def clear(self):
        try:
            db = self.__colect.find()
            if db:
                for row in db:
                    self.__colect.remove(row)
        except Exception as er:
            print(er)
            exit(-1)
