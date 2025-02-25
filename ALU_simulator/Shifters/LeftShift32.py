from ALU_simulator.Shifters.LeftShift1 import LeftShift1
from ALU_simulator.Shifters.LeftShift2 import LeftShift2
from ALU_simulator.Shifters.LeftShift4 import LeftShift4
from ALU_simulator.Shifters.LeftShift8 import LeftShift8
from ALU_simulator.Shifters.LeftShift16 import LeftShift16
from ALU_simulator.Plexers import Mux
from ALU_simulator.utils import InvalidType,  ALU_BIT_LENGTH, BIT_VALUE, SHIFT_AMOUNT_BIT_LENGTH


class LeftShift32:
    def __init__(self, input_a: str, carry_in: str, shift_amount: str):
        self.__output = ""
        self.__input_a = input_a
        self.__carry_in = carry_in
        self.__shift_amount = shift_amount
        self.__validate_input()
        self.__execute()
        
        
    def __execute(self):
        shift1_output = LeftShift1(self.__input_a, self.__carry_in).get_output()
        self.__output = Mux([self.__input_a, shift1_output], self.__shift_amount[4]).get_output()
        shift2_output = LeftShift2(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift2_output], self.__shift_amount[3]).get_output()
        shift4_output = LeftShift4(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift4_output], self.__shift_amount[2]).get_output()
        shift8_output = LeftShift8(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift8_output], self.__shift_amount[1]).get_output()
        shift16_output = LeftShift16(self.__output, self.__carry_in).get_output()
        self.__output = Mux([self.__output, shift16_output], self.__shift_amount[0]).get_output()
    
    
    def __validate_input(self):
        if len(self.__input_a) != ALU_BIT_LENGTH:
            raise InvalidType("LeftShift32")
        if self.__carry_in not in BIT_VALUE:
            raise InvalidType("LeftShift32")
        if len(self.__shift_amount) != SHIFT_AMOUNT_BIT_LENGTH:
            raise InvalidType("LeftShift32")
        for bit in self.__input_a:
            if bit not in BIT_VALUE:
                raise InvalidType("LeftShift32")
        for bit in self.__shift_amount:
            if bit not in BIT_VALUE:
                raise InvalidType("LeftShift32")
    
    
    def get_output(self) -> str:
        return str(self.__output)