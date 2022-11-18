from pymongo import MongoClient


class DataBase:
    def __init__(self):
        self.__client = None
        self.__db = None
        self.__colect = None

    def conect(self, path):
        try:
            self.__client = MongoClient(path)
        except Exception as ex:
            print(f'Bład połaczenia sie z baza [{ex}]')
            exit(-1)

        self.__db = self.__client['Projekt_1']
        self.__colect = self.__db['projekt_1']

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
