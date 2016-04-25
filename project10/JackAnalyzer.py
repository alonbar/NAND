import sys
import os
import JackTokenizer
import re
class JackAnalyzer:
    def __init__(self, input_path_):
        self._input_path = input_path_

    def analyze(self):
        if os.path.isdir(self._input_path):
            files_list = os.listdir(self._input_path)
            for file in files_list:
                if str(file).endswith(".jack"):
                    self.analyze_file(self._input_path + "/" + file)

        else:
            self.analyze_file(self._input_path)

    def analyze_file(self, input_file_path_):
        print("inside analyze_fle")
        tokenizer = JackTokenizer.JackTokernizer(input_file_path_)
        tokenizer.init()
        tokenizer.tokenize()



if __name__ == "__main__":
    analyzer = JackAnalyzer(sys.argv[1])
    analyzer.analyze()
