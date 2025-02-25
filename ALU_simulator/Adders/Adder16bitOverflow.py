from ALU_simulator.Adders.Adder4bitOverflow import Adder4bitOverflow
from ALU_simulator.Adders.Adder4bit import Adder4bit
from ALU_simulator.utils import InvalidType, BIT_VALUE


class Adder16bitOverflow:
    def __init__(self, a: str, b: str, carry_in: str):
        self.__BIT_LENGTH = 16
        self.__a = a
        self.__b = b
        self.__carry_in = carry_in
        self.__output = ""
        self.__overflow = 0
        self.__validate_input()
        self.__execute()
        
    
    def __validate_input(self):
        if len(self.__a) != self.__BIT_LENGTH or len(self.__b) != self.__BIT_LENGTH:
            raise InvalidType("Adder16bitOverflow")
        for i in range(self.__BIT_LENGTH):
            if self.__a[i] not in BIT_VALUE or self.__b[i] not in BIT_VALUE:
                raise InvalidType("Adder16bitOverflow")
        if self.__carry_in not in BIT_VALUE:
            raise InvalidType("Adder16bitOverflow")
        
        
    
    def get_output(self) -> str:
        return str(self.__output)
    
    
    def get_overflow(self) -> str:
        return str(self.__overflow)
    
    
    def __execute(self):
        for i in range(self.__BIT_LENGTH - 1, -1, -4):
            a = self.__a[i - 3:i + 1]
            b = self.__b[i - 3:i + 1]
            carry_in = self.__carry_in
            if i != 3:
                adder = Adder4bit(a, b, carry_in)
                self.__output += adder.get_output()[::-1]
                self.__carry_in = adder.get_carry_out()
            else:
                adder = Adder4bitOverflow(a, b, carry_in)
                self.__output += adder.get_output()[::-1]
                self.__overflow = adder.get_overflow()
        self.__output = str(self.__output)[::-1]
        