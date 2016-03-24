import sys
import os

class Parser:
    C_COMMAND = "C_COMMAND"
    L_COMMAND = "L_COMMAND"
    A_COMMAND = "A_COMMAND"
    ADDRESS_PREFIX = "@"
    LABEL_PREFIX = "("
    def __init__(self, root_name):
        self.root_name = root_name



    def parse(self):
        if os.path.isfile(self.root_name):
            self.parse_file(self.root_name)
        elif os.path.isdir(self.root_name):
            files_list = []
            files_list = os.listdir(self.root_name)
            for file in files_list:
                if file.endswith(".asm") and os.path.isfile(self.root_name + "/" + file):
                    self.parse_file(self.root_name + "/" + file)

    def parse_file(self, file_name):
        print(file_name)
        with open(file_name) as f:
            lines =[line.rstrip() for line in f]

        symbols_table = self.create_symbol_table(lines)
        output_file = self.root_name + "/" + str(file_name).replace(".asm", ".hack")
        for line in lines:
        


    def create_symbol_table(self, lines):
        table = {}
        lineNum = 0
        for line in lines:
            if line[0] == self.ADDRESS_PREFIX:
                table[str(line)[1:]] = lineNum
            if line[0] == self.LABEL_PREFIX:
                table[str(line)[1:-1]] = lineNum
            lineNum+=1
        return table;




