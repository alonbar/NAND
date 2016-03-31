import os
import sys
import CodeWriter
class Parser:
    def __init__(self, input_file_str_ , writer_):
        self._input_file_path = input_file_str_
        self._writer = writer_

    def parse_vm(self):
        output_file_path = self._input_file_path.replace(".vm", ".asm")
        output_file = open(output_file_path, "w")
        with open(self._input_file_path, "r") as f:
            lines = [line.strip() for line in f if line.strip() and line[0] != '/']
            counter = 0
            for line in lines:
                if '/' in line:
                    lines[counter] = line[0:line.index('/')]
                counter += 1
        for line in lines:
            asm_lines = self._writer.write_line(line.split())
            for asm_line in asm_lines:
                output_file.write(asm_line + "\n")

if __name__ == "__main__":
    
    print ("main")
