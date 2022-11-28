from pymongo import MongoClient


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

    def push(self, data):
        try:
            for i in range(len(data)):
                self.__colect.insert_one({'day': data[i][0], 'closingPrice': data[i][1]})
        except Exception as ex:
                print(ex)
                exit(-1)

    def printAll(self):
        for doc in self.__colect.find():
            print(doc)

    def load_data(self):
        return self.__colect.find()

    def clear(self):
        try:
            db = self.__colect.find()
            if db:
                for row in db:
                    self.__colect.remove(row)
        except Exception as er:
            print(er)
            exit(-1)
