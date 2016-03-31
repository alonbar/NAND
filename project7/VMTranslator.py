import sys
import os
import Parser
import CodeWriter
if __name__ == "__main__":

    if os.path.isdir(sys.argv[1]):
        file_list = os.listdir(sys.argv[1])
        for file in file_list:
            if str(file).endswith(".vm") == True:
                writer = CodeWriter.CodeWriter(file[:-3])
                parser = Parser.Parser(sys.argv[1]+ file, writer)
                parser.parse_vm()

    else:
        print("parse")
