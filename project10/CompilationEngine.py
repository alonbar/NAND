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
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()

        #getting var declerations
        while self._tokenizer.get_next_token_content()in ["static", "field"]:
            self.compile_class_var_dec()

        while self._tokenizer.get_next_token_content()in ["constructor", "function", "method"]:
            self.compile_subroutine()

        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("class") + "\n"]

        for item in self._analysis_tokens:
            output_file.write(item)
        output_file.close()

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

    #compiling subroutine body
    def compile_subroutine_body(self):
          #getting subroutine body
        self._analysis_tokens += [self.get_brackets_start_line("subroutineBody") + "\n"]

        #getting "{"
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()

        while self._tokenizer.get_next_token_content() == "var":
            self.compile_var_dec()

        self.compile_statement()

        #get }
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("subroutineBody")  + "\n"]

    #compiling subroutine var declerations
    def compile_var_dec(self):
        self._analysis_tokens += [self.get_brackets_start_line("varDec") + "\n" ]

        #getting var deceleration
        while self._tokenizer.get_next_token_content() != ";":
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()

        #getting ";"
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("varDec") + "\n"]

    #compiling subroutine statements
    def compile_statement(self):
        self._analysis_tokens += [self.get_brackets_start_line("statements") + "\n"]
        statement = self._tokenizer.get_next_token_content()
        while statement != "}":
            if statement == "let":
                self.compile_let()
            elif statement =="if":
                self.compile_if()
            elif statement == "while":
                self.compile_while()
            elif statement == "do":
                self.compile_do()
            elif statement == "return":
                self.compile_return()
            statement = self._tokenizer.get_next_token_content()
        self._analysis_tokens += [self.get_brackets_end_line("statements") + "\n"]

    def compile_return(self):
        self._analysis_tokens += [self.get_brackets_start_line("returnStatement") + "\n"]
        #get return
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        if self._tokenizer.get_next_token_content() != ";":
            self.compile_expression()
        #get ;
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("returnStatement") + "\n"]


    def compile_do(self):
        self._analysis_tokens += [self.get_brackets_start_line("doStatement") + "\n"]
        #get do
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        #get the next token after do
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()

        #get . and the name of function
        while self._tokenizer.get_next_token_content() == ".":
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()

        #get (
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()

        self.compile_expression_list()
        #get )
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        #get ;
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("doStatement") + "\n"]

    def compile_while(self):
        self._analysis_tokens += [self.get_brackets_start_line("whileStatement") + "\n"]
        #get while
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        #get (
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self.compile_expression()
        #get )
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        #get {
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self.compile_statement()
        #get }
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("whileStatement") + "\n"]

    def compile_if(self):
        self._analysis_tokens += [self.get_brackets_start_line("ifStatement") + "\n"]
        #write if
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        #write (
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self.compile_expression()
        #get )
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        #get {
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self.compile_statement()
        # get }
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        if self._tokenizer.get_next_token_content() == "else":
            #write else
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            # write {
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            self.compile_statement()
            #get }
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()

        self._analysis_tokens += [self.get_brackets_end_line("ifStatement") + "\n"]

    def compile_let(self):
        self._analysis_tokens += [self.get_brackets_start_line("letStatement") + "\n"]
        #writing let and the var name
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        if self._tokenizer.get_next_token_content() == "[":
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            self.compile_expression()
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()

        #getting "="
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self.compile_expression()
        #get ";"
        self._analysis_tokens += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._analysis_tokens += [self.get_brackets_end_line("letStatement") + "\n"]

    def compile_expression(self):
        self._analysis_tokens += [self.get_brackets_start_line("expression") + "\n"]
        self.compile_term()
        while self._tokenizer.get_next_token_content() in ["*", "&lt;", "&gt;", "=", "-", "+", "/", "|", "&amp;"]:
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            self.compile_term()
        self._analysis_tokens += [self.get_brackets_end_line("expression") + "\n"]

    def compile_term(self):
        self._analysis_tokens += [self.get_brackets_start_line("term") + "\n"]
        if self._tokenizer.get_next_token_content() == "(":
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            self.compile_expression()
            #writing ")"
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
        elif self._tokenizer.get_next_token_content() in ["-", "~"]:
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            self.compile_term()
        else:
            #getting the token
            self._analysis_tokens += self.get_next_line()
            self._tokenizer.advance_token_ptr()
            if self._tokenizer.get_next_token_content() == "[":
                #getting the "["
                self._analysis_tokens += self.get_next_line()
                self._tokenizer.advance_token_ptr()
                self.compile_expression()
                #getting the "]"
                self._analysis_tokens += self.get_next_line()
                self._tokenizer.advance_token_ptr()

            if self._tokenizer.get_next_token_content() == "(":
                self._analysis_tokens += self.get_next_line()
                self._tokenizer.advance_token_ptr()
                self.compile_expression_list()
                self._analysis_tokens += self.get_next_line()
                self._tokenizer.advance_token_ptr()

            if self._tokenizer.get_next_token_content() == ".":
                while self._tokenizer.get_next_token_content() == ".":
                    #write .
                    self._analysis_tokens += self.get_next_line()
                    self._tokenizer.advance_token_ptr()
                    #write method name
                    self._analysis_tokens += self.get_next_line()
                    self._tokenizer.advance_token_ptr()
                #write (
                self._analysis_tokens += self.get_next_line()
                self._tokenizer.advance_token_ptr()
                self.compile_expression_list()
                #write )
                self._analysis_tokens += self.get_next_line()
                self._tokenizer.advance_token_ptr()

        self._analysis_tokens += [self.get_brackets_end_line("term") + "\n"]


    def compile_expression_list(self):
        self._analysis_tokens += [self.get_brackets_start_line("expressionList") + "\n"]
        if self._tokenizer.get_next_token_content() != ")":
            self.compile_expression()
            while self._tokenizer.get_next_token_content() == ",":
                self._analysis_tokens += self.get_next_line()
                self._tokenizer.advance_token_ptr()
                self.compile_expression()
        self._analysis_tokens += [self.get_brackets_end_line("expressionList") + "\n"]

    def get_next_line(self):
        return [self.get_brackets_start_line(self._tokenizer.get_next_token_type()) + " " +
                                      self._tokenizer.get_next_token_content() + " " +
                                      self.get_brackets_end_line(self._tokenizer.get_next_token_type()) + "\n"]

    def get_brackets_start_line(self, str):
        return "<" + str + ">"

    def get_brackets_end_line(self, str):
        return self.get_brackets_start_line("/" + str)

