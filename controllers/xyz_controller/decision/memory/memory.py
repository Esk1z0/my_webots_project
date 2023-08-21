from utils.EData import EData
from memory_decoders.memory_decoder import MemoryDecoder
from memory_decoders.security_commands import SecurityDecoder
from memory_decoders.received_decoder import ReceivedDecoder
from memory_decoders.other_decoder import OtherDecoder

class MemoryDecoder():

    def __init__(self):
        self.__security_decoder = MemoryDecoder(SecurityDecoder.COMMANDS)
        self.__command_decoder = MemoryDecoder(ReceivedDecoder.COMMANDS)
        self.__other_decoder = MemoryDecoder(OtherDecoder.COMMANDS)

    def decode_command(self, command: dict):
        key, value = dict.popitem()
        if EData.RECEIVEDED_DATA == key:
            return self.__security_decoder.decode(value)
        elif EData.SECURITY_DATA == key:
            return self.__command_decoder.decode(value)
        elif EData.OTHER == key:
            return self.__other_decoder.decode(value)
        else:
            print('error memory decode')
            return None
