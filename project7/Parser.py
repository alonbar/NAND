import os
import sys
import CodeWriter
class Parser:
    def __init__(self, input_file_str_ , writer_):
        self._input_file_path = input_file_str_
        self._writer = writer_


    def parse_vm(self, file_name_, output_file_):
        with open(self._input_file_path+  file_name_, "r") as f:
            lines = [line.strip() for line in f if line.strip() and line[0] != '/']
            counter = 0
            for line in lines:
                if '/' in line:
                    lines[counter] = line[0:line.index('/')]
                counter += 1
        for line in lines:
            asm_lines = self._writer.write_line(line.split())
            for asm_line in asm_lines:
                output_file_.write(asm_line + "\n")


    def parse(self):
        if os.path.isdir(self._input_file_path):
            output_file_path = self._input_file_path +"/" + os.path.basename(os.path.normpath(self._input_file_path)) + ".asm"
            output_file = open(output_file_path, "w")
            file_list = os.listdir(self._input_file_path)
            for file in file_list:
                if str(file).endswith(".vm") == True:
                    self._writer.set_program_name(file[:-3])
                    self.parse_vm("/" + file, output_file)

        else:
            output_file_path = self._input_file_path.replace(".vm", ".asm")
            output_file = open(output_file_path, "w")
            self._writer.set_program_name(os.path.basename(os.path.normpath(self._input_file_path))[:-3])
            self.parse_vm("", output_file)

if __name__ == "__main__":
    
    print ("main")
