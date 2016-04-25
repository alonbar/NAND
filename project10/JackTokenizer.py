import re
class JackTokernizer:

    KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char',
                'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while',
                'return']
    SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']

    IDENTIFIERS = []
    KEYWORD_START = "<keyword>"
    KEYWORD_END = "</keyword>\n"
    IDENTIFIER_START = "<identifier>"
    IDENTIFIER_END = "</identifier>\n"
    SYMBOL_START = "<symbol>"
    SYMBOL_END = "</symbol>\n"
    INTEGET_CONSTANT_START = "<integerConstant>"
    INTEGET_CONSTANT_END = "</integerConstant>\n"
    STRING_CONSTANT_START = "<stringConstant>"
    STRING_CONSTANT_END = "</stringConstant>\n"


    def __init__(self, input_file_path_):
        self._input_file_path = input_file_path_
        self._raw_program = []
        self.tokens= []
        self.token_cnt = 0

    def init(self):
        str = ""
        with open(self._input_file_path,'r') as f:
            lines = [line for line in f if line.strip()]
            for line in lines:
                if (line.lstrip().startswith("//")):
                    continue
                line = re.sub(re.compile("//.*?\n" ) ,"" ,line) # remove all occurance singleline comments (//COMMENT\n ) from string
                line = line.strip()
                str += " " + line
        str = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,str) # remove all occurance streamed comments (/*COMMENT */) from string
        # str = re.sub(re.compile("/\*\*.*?\*/",re.DOTALL ) ,"" ,str) # remove all occurance streamed comments (/*COMMENT */) from string

        # str = str.replace("{", " { ").replace("}", " } ").replace("(", " ( ").replace(")", " ) ").replace("[", " [ ")\
        #     .replace("]", " ] ").replace(".", " . ").replace(";", " ; ").replace(",", " , ").replace(";", " ; ")\
        #     .replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").replace("&", " & ")\
        #     .replace("|", " | ").replace("<", " < ").replace(">", " > ").replace("=", " = ").replace("~"," ~ ")
        arr_temp = re.split('({)*(})*(\()*(\)+?)(\[)*(\])*(\.)*(,)*(;)*(\+)*(-)*(\*)*(/)*(&)*(|)*(<)*(>)*(=)*(\~)*(class )*(constructor )*(function )*(method )*(field)*(static )*(var )*(int )*(char )*(boolean )*(void )*(Array )*(true)*(false)*(null)*(this)*(let )*(do )*(if)*(else)*(while)*(return)*', str)
        arr = []
        for item in arr_temp:
            if item != None and bool(item.strip()):
                arr.append(item)
        cnt = 0
        while (cnt < len(arr)):
            if arr[cnt] != None and arr[cnt].strip() != "":
                print (cnt)
                print (arr[cnt] )
                self._raw_program.append(arr[cnt].strip())
                if arr[cnt].strip() in ["constructor", "function", "method", "field", "static", "var"] and arr[cnt+1].strip() not in ["int", "char", "boolean","void", "Array"]:
                    identifiers = arr[cnt+1].split()
                    self._raw_program.append(identifiers[0].strip())
                    self._raw_program.append(identifiers[1].strip())
                    cnt += 2
                else:
                    cnt+=1
            else:
                cnt +=1

        #
        # for item in arr:
        #     if item != None and item.strip() != "":
        #         if item in [""]
        #         item_arr = item.split()
        #         if (len(item_arr) > 1):
        #             print ("asdf")
        #         self._raw_program.append(item.strip())
        print (self._raw_program)

    def tokenize(self):
        output_file = open(self._input_file_path.replace(".jack", "T.xml"), "w")
        tokens = []
        tokens += ["<tokens>\n"]
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
                else:
                    tokens += self.get_identifier_line()
        tokens += ["</tokens>\n"]
        for token in tokens:
            output_file.write(token)

        output_file.close()


    def increase_token_count(self):
        self.token_cnt += 1

    def get_next_token(self):
        token = self._raw_program[self.token_cnt]
        self.increase_token_count()
        return token

    def get_keyword_line(self):
        return [self.KEYWORD_START + " " + self.get_next_token() + " " + self.KEYWORD_END]

    def get_symbol_line(self):
        return [self.SYMBOL_START+ " " + self.get_next_token().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") + " " + self.SYMBOL_END]

    def get_int_constant_line(self):
        return [self.INTEGET_CONSTANT_START + " " + self.get_next_token() + " " + self.INTEGET_CONSTANT_END]

    def get_string_constant_line(self):
        token = self.get_next_token()
        token = token[1:-1]
        token = token.replace('"', "&quot;")
        return [self.STRING_CONSTANT_START + " " + token + " " + self.STRING_CONSTANT_END]

    def get_identifier_line(self):
        return [self.IDENTIFIER_START + " " + self.get_next_token() + " " + self.IDENTIFIER_END]
    # def get_keyword_line(self):
    #     ret_lines = [self.KEYWORD_START + self.get_next_token() + self.KEYWORD_END,
    #                  self.IDENTIFIER_START+ self.get_next_token() + self.IDENTIFIER_END,
    #                  self.SYMBOL_START + self.get_next_token() + self.SYMBOL_END]
    #     ret_lines += self.tokenize()
    #     ret_lines += [self.SYMBOL_START + self.get_next_token() + self.SYMBOL_END
    #     return ret_lines



        print (self.raw_program)
