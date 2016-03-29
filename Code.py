import os

class Code:
    # TODO - josh need to change get functions to use these dictionaries
    comp_table = {"1": "1110111111", "-1": "1110111010","A": "1110110000","M": "1111110000", "!M": "1111110001", "D+1": "1110011111","-M":  "1111110011",
                  "D": "1110001100", "!D":  "1110001101", "!A": "1110110001",  "-D": "1110001111", "0": "1110101010", "-A": "1110110011",
                  "A+1":  "1110110111", "A-1", "1110110010" , "M+1": "1111110111", "D-A": "1110010011", "D-M": "1111010011", "A-D": "1110000111",
                  "D-1":  "1110001110", "M-D": "1111000111","M-1": "1111110010", "D<<": "1010110000",
                 "D>>": "1010010000",  "A<<": "1010100000","A>>": "1010000000",  "M<<": "1011100000", "M>>": "1011000000", "D+A": "1110000010", "A+D": "1110000010",
                "D+M": "1111000010", "M+D": "1111000010","D&A": "1110000000", "A&D":  "1110000000", "D&M": "1111000000","M&D": "1111000000",  "D|A":  "1110010101",
                 "A|D": "1110010101","D|M": "1111010101" ,"M|D": "1111010101"   }

    dest_table = {"D": "010", "AD": "110", "MD": "011", "A": "100", "M": "001", "AM": "101", "AMD": "111", }
    jump_table = {"JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111", }


    def __init__(self, dest_str, comp_str, jump_str):
        self.dest_mnemonic = dest_str
        self.comp__mnemonic = comp_str
        self.jump__mnemonic = jump_str

    def get_dest_code(self):
        return self.dest_table.get(self.dest__mnemonic, "000")
        

    def get_comp_code(self):
        return self.comp_table.get(self.comp__mnemonic)


    def get_jump_code(self):
        return self.jump_table.get(self.jump__mnemonic, "000")

