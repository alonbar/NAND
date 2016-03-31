import sys
import os
if __name__ == "__main__":

    if os.path.isdir(sys.argv[1]):
        file_list = os.listdir(sys.argv)
        for file in file_list:
            if str(file).endswith(".vm") == True:
                print("parse file")

    else:
        print("parse")
