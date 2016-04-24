import re
class JackTokernizer:

    KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char',
                'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while',
                'return']
    SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']

    IDENTIFIERS = []
    KEYWORD_START = "<keyword>"
    KEYWORD_END = "</keyword>"
    IDENTIFIER_START = "<identifier>"
    IDENTIFIER_END = "</identifier>"
    SYMBOL_START = "<symbol>"
    SYMBOL_END = "</symbol>"
    INTEGET_CONSTANT_START = "<integerConstant>"
    INTEGET_CONSTANT_END = "</integerConstant>"
    STRING_CONSTANT_START = "<stringConstant>"
    STRING_CONSTANT_END = "</stringConstant>"

    def __init__(self, input_file_path_):
        self._input_file_path = input_file_path_
        self._raw_program = []
        self.tokens= []
        self.token_cnt = 0

    def init(self):
        with open(self._input_file_path,'r') as f:
            lines = [line.strip() for line in f if line.strip() and line[0] != '/']
            str = ""
            for line in lines:
                str += " " + line
            str = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,str) # remove all occurance streamed comments (/*COMMENT */) from string
            str = re.sub(re.compile("//.*?\n" ) ,"" ,str) # remove all occurance singleline comments (//COMMENT\n ) from string
            str.replace("{", " { ").replace("}", " } ").replace("(", " ( ").replace(")", " ) ").replace("[", " [ ")\
                .replace("]", " ] ").replace(".", " . ").replace(";", " ; ").replace(",", " , ").replace(";", " ; ")\
                .replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").replace("&", " & ")\
                .replace("|", " | ").replace("<", " < ").replace(">", " > ").replace("=", " = ").replace("~"," ~ ")
            self._raw_program = str.split()
            print (self._raw_program)

    def tokenize(self):
        output_file = open(self._input_file_path.replace(".jack", ".vm"), "w")
        tokens = []
        for word in self._raw_program:
            if word in self.KEYWORDS:
                tokens += self.get_keyword_line()
            elif word in self.SYMBOLS:
                tokens += self.get_symbol_line()
            else:
                integer_regex = re.compile('\d+')
                res = integer_regex.match(word)
                if (res != None):
                    tokens += self.get_int_constant_line()
                elif word[0] == '"':
                    tokens += self.get_string_constant_line()


        return tokens

    def increase_token_count(self):
        self.token_cnt += 1

    def get_next_token(self):
        token = self._raw_program[self.token_cnt]
        self.increase_token_count()
        return token

    def get_keyword_line(self):
        return [self.KEYWORD_START + " " + self.get_next_token() + " " + self.KEYWORD_END]

    def get_symbol_line(self):
        return [self.SYMBOL_START+ " " + self.get_next_token() + " " + self.SYMBOL_END]

    def get_int_constant_line(self):
        return [self.INTEGET_CONSTANT_START + " " + self.get_next_token() + " " + self.INTEGET_CONSTANT_END]

    def get_string_constant_line(self):
        return [self.STRING_CONSTANT_START + " " + self.get_next_token()]
    # def get_keyword_line(self):
    #     ret_lines = [self.KEYWORD_START + self.get_next_token() + self.KEYWORD_END,
    #                  self.IDENTIFIER_START+ self.get_next_token() + self.IDENTIFIER_END,
    #                  self.SYMBOL_START + self.get_next_token() + self.SYMBOL_END]
    #     ret_lines += self.tokenize()
    #     ret_lines += [self.SYMBOL_START + self.get_next_token() + self.SYMBOL_END
    #     return ret_lines



        print (self.raw_program)
