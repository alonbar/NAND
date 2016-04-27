import JackTokenizer
class CompilationEngine:

    def __init__(self, input_file_):
        self._input_file = input_file_
        self._analysis_tokens = []
        self._tokenizer = JackTokenizer.JackTokernizer(self._input_file)

    def initialize(self):
        self._tokenizer.init()
        self._tokenizer.tokenize()


    def compile_clase(self):
        output_file = open(self._input_file.replace(".jack", ".xml"), "w")

        self._analysis_tokens += [self.get_brackets_start_line("class") + "\n"]
        self._tokenizer.advance_token_ptr()

        #getting class decleration
        for i in range(0,3):
            self._analysis_tokens += [self.get_brackets_start_line(self._tokenizer.get_next_token_type()) + " " +
                              self._tokenizer.get_next_token_content() + " " +
                              self.get_brackets_end_line(self._tokenizer.get_next_token_type()) + "\n"]
            self._tokenizer.advance_token_ptr()

        #getting var declerations
        while self._tokenizer.get_next_token_content()in ["static", "field"]:
            self.compile_class_var_dec()

        while self._tokenizer.get_next_token_content()in ["constructor", "function", "method"]:
            self.compile_subroutine()

        self._analysis_tokens += [self.get_brackets_end_line("class") + "\n"]

        for item in self._analysis_tokens:
            output_file.write(item)

    def compile_class_var_dec(self):
        self._analysis_tokens += [self.get_brackets_start_line("classVarDec") + "\n"]
        #static or field and then type and then var name
        for i in range(0,3):
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()

        #more than one var was declared
        while self._tokenizer.get_next_token_content() == ",":
            #getting ,
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            #getting the var name
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()

        #getting ;
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("classVarDec") + "\n"]

    def compile_subroutine(self):
        self._analysis_tokens += [self.get_brackets_start_line("subroutineDec") + "\n"]

        #get subroutine start: constructor|unction|method then void|type the subrioutine name then (
        for i in range(0,4):
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
        self.compile_parameter_list()

        #writing ) to end parameter list
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()

        #subroutine body
        self.compile_subroutine_body()

        self._analysis_tokens += [self.get_brackets_end_line("subroutineDec") + "\n"]

    def compile_parameter_list(self):
        self._analysis_tokens += [self.get_brackets_start_line("parameterList") + "\n"]
        #writing paramteres
        while self._tokenizer.get_next_token_content() != ")":
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("parameterList") + "\n"]


    def compile_subroutine_body(self):
          #getting subroutine body
        self.get_brackets_start_line("subroutineBody")

        #getting "{"
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()

        while self._tokenizer.get_next_token_content() == "var":
            self.
        self.get_brackets_end_line("subroutineBody")

    def compile_var_dec(self):


    def get_next_line(self):
        return [self.get_brackets_start_line(self._tokenizer.get_next_token_type()) + " " +
                                      self._tokenizer.get_next_token_content() + " " +
                                      self.get_brackets_end_line(self._tokenizer.get_next_token_type()) + "\n"]

    def get_brackets_start_line(self, str):
        return "<" + str + ">"

    def get_brackets_end_line(self, str):
        return self.get_brackets_start_line("/" + str)

