class MemoryDecoder():

    def __init__(self, commands):
        self.__commands = commands

    def decode(self, data):
        #esto no está hecho ni nada
        if data in self.__commands:
            return self.__commands[data]
        else:
            return None