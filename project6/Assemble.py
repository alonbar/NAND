import sys
import Parser

def main():
    print("in main")
    print(sys.argv[1])
    p = Parser.Parser("C:/temp/ex6")
    p.parse();





if __name__ == "__main__":
    main()