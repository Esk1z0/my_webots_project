
class Container():
    def __init__(self, dict = {}):
        self.__dict = dict

    def put(self, key, value):
        aux = {key, value}
        self.__dict.update(aux)

    def pop(self):
        return self.__dict.pop()

    def get(self, key):
        return self.__dict.get(key)