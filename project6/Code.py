import os

class Code:
    # TODO - josh need to change get functions to use these dictionaries
    comp_table = {}
    dest_table = {}
    jump_table = {"JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111", }
    def __init__(self, dest_str, comp_str, jump_str):
        self.dest_mnemonic = dest_str
        self.comp__mnemonic = comp_str
        self.jump__mnemonic = jump_str

    def get_dest_code(self):
        if self.dest_mnemonic == "A":
            return "100"
        elif self.dest_mnemonic == "D":
            return "010"
        elif self.dest_mnemonic == "M":
            return "001"
        elif self.dest_mnemonic == "AD":
            return "110"
        elif self.dest_mnemonic == "AM":
            return "101"
        elif self.dest_mnemonic == "MD":
            return "011"
        elif self.dest_mnemonic == "AMD":
            return "111"
        else:
            return "000"

    def get_comp_code(self):
        if self.comp__mnemonic == "0":
            return "1110101010"
        elif self.comp__mnemonic == "1":
            return "1110111111"
        elif self.comp__mnemonic == "-1":
            return "1110111010"
        elif self.comp__mnemonic == "D":
            return "1110001100"
        elif self.comp__mnemonic == "!D":
            return "1110001101"
        elif self.comp__mnemonic == "-D":
            return "1110001111"
        elif self.comp__mnemonic == "A":
            return "1110110000"
        elif self.comp__mnemonic == "!A":
            return "1110110001"
        elif self.comp__mnemonic == "-A":
            return "1110110011"
        elif self.comp__mnemonic == "M":
            return "1111110000"
        elif self.comp__mnemonic == "!M":
            return "1111110001"
        elif self.comp__mnemonic == "-M":
            return "1111110011"
        elif self.comp__mnemonic == "D+1":
            return "1110011111"
        elif self.comp__mnemonic == "M+1":
            return "1111110111"
        elif self.comp__mnemonic == "A+1":
            return "1110110111"
        elif self.comp__mnemonic == "D-1":
            return "1110001110"
        elif self.comp__mnemonic == "A-1":
            return "1110110010"
        elif self.comp__mnemonic == "M-1":
            return "1111110010"
        elif self.comp__mnemonic == "D+A" or self.comp__mnemonic == "A+D":
            return "1110000010"
        elif self.comp__mnemonic == "D+M" or self.comp__mnemonic == "M+D":
            return "1111000010"
        elif self.comp__mnemonic == "D-A":
            return "1110010011"
        elif self.comp__mnemonic == "D-M":
            return "1111010011"
        elif self.comp__mnemonic == "A-D":
            return "1110000111"
        elif self.comp__mnemonic == "M-D":
            return "1111000111"
        elif self.comp__mnemonic == "D&A" or self.comp__mnemonic == "A&D":
            return "1110000000"
        elif self.comp__mnemonic == "D&M" or self.comp__mnemonic == "M&D":
            return "1111000000"
        elif self.comp__mnemonic == "D|A" or self.comp__mnemonic == "A|D":
            return "1110010101"
        elif self.comp__mnemonic == "D|M" or self.comp__mnemonic == "M|D":
            return "1111010101"
        elif self.comp__mnemonic == "D<<":
            return "1010110000"
        elif self.comp__mnemonic == "D>>":
            return "1010010000"
        elif self.comp__mnemonic == "A<<":
            return "1010100000"
        elif self.comp__mnemonic =="A>>":
            return "1010000000"
        elif self.comp__mnemonic =="M<<":
            return "1011100000"
        elif self.comp__mnemonic =="M>>":
            return "1011000000"
        #to do - change to work like get_jump_code


    def get_jump_code(self):
        return self.jump_table.get(self.jump__mnemonic, "000")


