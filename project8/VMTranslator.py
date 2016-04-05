import sys
import os
import Parser
import CodeWriter
if __name__ == "__main__":

    writer = CodeWriter.CodeWriter()
    parser = Parser.Parser(sys.argv[1],writer)
    parser.parse()