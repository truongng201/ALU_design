from LeftShift2 import LeftShift2
from utils import InvalidType, InvalidOperation, ALU_BIT_LENGTH, BIT_VALUE


class LeftShift4:
    def __init__(self, input: str, carry_in: str):
        self.__output = None
        self.__input = input
        self.__carry_in = carry_in
        self.__validate_input()
        self.__execute()        


    def __execute(self):
        self.__output = LeftShift2(self.__input, self.__carry_in).get_output()
        self.__output = LeftShift2(self.__output, self.__carry_in).get_output()
    
    
    def __validate_input(self):
        if len(self.__input) != ALU_BIT_LENGTH:
            raise InvalidType("LeftShift4")
        if self.__carry_in not in BIT_VALUE:
            raise InvalidType("LeftShift4")
        for bit in self.__input:
            if bit not in BIT_VALUE:
                raise InvalidType("LeftShift4")
        
    
    def get_output(self) -> str:
        if self.__output == None:
            raise InvalidOperation("LeftShift4")
        return str(self.__output)