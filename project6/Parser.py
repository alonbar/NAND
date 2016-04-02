import sys
import os
import Code
#This class parse all ".asm" files. it will read the files line by line and will retreive the correct machine code from
#Code class
class Parser:
    ADDRESS_PREFIX = "@"
    LABEL_PREFIX = "("
    EQUAL_CHAR = '='
    JUMP_CHAR = ';'
    #Will contain all symbols
    symbol_table = {}
    VAR_START_ADDRESS = 16
    def __init__(self, root_name):
        self.root_name = root_name

    def parse(self):
        #Checking whether the path is a file or directory
        if os.path.isfile(self.root_name):
            self.parse_file(self.root_name)
        elif os.path.isdir(self.root_name):
            files_list = []
            files_list = os.listdir(self.root_name)
            for file in files_list:
                if file.endswith(".asm") and os.path.isfile(self.root_name + "/" + file):
                    self.parse_file(self.root_name + "/" + file)
    #parsing a single file
    def parse_file(self, file_name):
        with open(file_name, "r") as f:
            #reading the lines while ignoring whitespaces and comments
            lines = [line.replace(' ','').strip() for line in f if line.replace(' ','').strip() and line[0] != '/']
            counter = 0
            for line in lines:
                #ignoring comments at the end of the line
                if '/' in line:
                    lines[counter] = line[0:line.index('/')]
                counter += 1
        # creating symbols table
        symbols_table = self.create_symbol_table(lines)
        cur_var_address = self.VAR_START_ADDRESS
        output_file = open(str(file_name).replace(".asm", ".hack"), 'w')
        ji = 0
        #parsing file
        for line in lines:
            c_command = ""
            a_command = ""
            binary_command = ""
            if line[0] == self.ADDRESS_PREFIX:
                #it is a Address command
                symbol = line[1:]
                address = 0
                if symbol[0].isdigit():
                    address = int(symbol)
                    symbols_table[symbol] = address
                elif symbol in symbols_table:
                    address = symbols_table[symbol]
                else:
                    address = cur_var_address
                    symbols_table[symbol] = cur_var_address
                    cur_var_address += 1
                binary_address = format(address, '016b')
                output_file.write(binary_address + "\n")
            elif line[0] != self.ADDRESS_PREFIX and line[0] != self.LABEL_PREFIX:
            #it is a C_COMMAND
                c_command = self.parse_c_command(line)
                output_file.write(c_command + "\n")
        output_file.close()

    def create_symbol_table(self, lines):
        #intializing and creating symbol table
        symbols_table = {}
        symbols_table["SP"] = 0
        symbols_table["LCL"] = 1
        symbols_table["ARG"] = 2
        symbols_table["THIS"] = 3
        symbols_table["THAT"] = 4
        symbols_table["SCREEN"] = 16384
        symbols_table["KBD"] = 24576
        for i in range(16):
            symbols_table["R" + str(i)] = i
        lineNum = 0
        for line in lines:
            if line[0] == self.LABEL_PREFIX and line[1:-1] not in symbols_table:
                symbols_table[str(line)[1:-1]] = lineNum
            else:
                lineNum+=1
        return symbols_table

    def parse_c_command(self, c_command):
        dest_str = self.get_dest_mnemonic(c_command)
        comp_str = self.get_comp_mnemonic(c_command)
        jump_str = self.get_jump_mnemonic(c_command)
        return self.build_binary_command(dest_str, comp_str, jump_str)


    def get_dest_mnemonic(self, c_command):
        dest_str = ""
        if self.EQUAL_CHAR in c_command:
            dest_str = c_command[0:str(c_command).index(self.EQUAL_CHAR)]
        return dest_str

    def get_comp_mnemonic(self, c_command):
        comp_str = ""
        if self.EQUAL_CHAR in c_command:
            comp_str = c_command[c_command.index(self.EQUAL_CHAR)+ 1:]
            if self.JUMP_CHAR in comp_str:
                comp_str = comp_str[0:comp_str.index(self.JUMP_CHAR)]
            return comp_str
        if self.JUMP_CHAR in c_command:
            comp_str = c_command[0:c_command.index(self.JUMP_CHAR)]
        return comp_str

    def get_jump_mnemonic(self, c_command):
        jump_str = ""
        if self.JUMP_CHAR in c_command:
            jump_str = c_command[c_command.index(self.JUMP_CHAR) + 1:]
        return jump_str

    def build_binary_command(self, dest_str, comp_str, jump_str):
        #getting the correct machine code
        code = Code.Code(dest_str, comp_str, jump_str)
        dest_code = code.get_dest_code()
        comp_code = code.get_comp_code()
        jump_code = code.get_jump_code()
        return comp_code + dest_code +  jump_code


