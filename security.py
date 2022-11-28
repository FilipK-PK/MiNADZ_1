from Crypto.Cipher import AES
import keys


class Security:
    def __init__(self, path_key):
        self.key = None

        self.__loadKey(path_key)

        self.__set_keys()

    def encrypt(self, data):
        return self.__cipher.encrypt(
            self.__to_len16(str(data)).encode()
        )

    def decrypt(self, data):
        return self.__cipher_d.decrypt(
            data
        ).rstrip().decode()

    def __loadKey(self, path):
        try:
            file = open(path, 'rb')
            self.key = file.read()
            file.close()
        except Exception as er:
            print(er)
            exit(-2)

        if not len(self.key):
            print('Bład: klucz 0 len')
            exit(-3)

    def __to_len16(self, data):
        while len(data) % 16 != 0:
            data = data + " "

        return data

    def __set_keys(self):
        self.__cipher = AES.new(self.key, AES.MODE_EAX, keys.IV)
        self.__cipher_d = AES.new(self.key, AES.MODE_EAX, keys.IV)
