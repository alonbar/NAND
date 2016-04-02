import sys
import Parser

def main():
    p = Parser.Parser(sys.argv[1])
    p.parse();

if __name__ == "__main__":
    main()