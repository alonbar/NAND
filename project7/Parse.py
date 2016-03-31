import os
import sys
class Parse:
    def __init__(self, input_file_str_):
        self._input_file_path = input_file_str_


    def parse_vm(self):
        output_file_path = self._input_file_path.replace(".asm", ".vm")
        with open(output_file_path, "r") as f:
            lines = [line.replace(' ','').strip() for line in f if line.replace(' ','').strip() and line[0] != '/']
            counter = 0
            for line in lines:
                if '/' in line:
                    lines[counter] = line[0:line.index('/')]
                counter += 1
        for line in lines:
            self.parse_line(line)


    def parse_line(self, line):
        

if __name__ == "__main__":
    
    print ("main")
