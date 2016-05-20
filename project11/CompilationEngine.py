import JackTokenizer
import VMWriter
import SymbolTable
class CompilationEngine:
    CONSTANT = "constant"
    POINTER = "pointer"
    ARGUMENT = "argument"
    THAT = "that"
    TEMP = "temp"

    def __init__(self, input_file_):
        self._input_file = input_file_
        self._compiled_lines = []
        self._tokenizer = JackTokenizer.JackTokernizer(self._input_file)
        self._vm_writer = VMWriter.VMwriter()
        self._symbol_table = SymbolTable.SymbolTable()
        self._labe_cnt = -1

    def initialize(self):
        self._tokenizer.init()
        self._tokenizer.tokenize()


    def compile_clase(self):
        output_file = open(self._input_file.replace(".jack", ".vm"), "w")
        while self._tokenizer.get_next_token_content() in ["\n",""]:
            self._tokenizer.advance_token_ptr()

        if self._tokenizer.get_next_token_content() != "class":
            return
        self._tokenizer.advance_token_ptr()
        self._class_name = self._tokenizer.get_next_token_content()
        # {

        self._tokenizer.advance_token_ptr()
        self._tokenizer.advance_token_ptr()

        #getting var declerations
        while self._tokenizer.get_next_token_content()in ["static", "field"]:
            self.compile_class_var_dec()

        while self._tokenizer.get_next_token_content()in ["constructor", "function", "method"]:
            subroutine_type = self._tokenizer.get_next_token_content()
            self.compile_subroutine(subroutine_type)

        self._compiled_lines += self.get_next_line()
        self._tokenizer.advance_token_ptr()
        self._compiled_lines += [self.get_brackets_end_line("class") + "\n"]

        for item in self._compiled_lines:
            output_file.write(item)
        output_file.close()

    def compile_class_var_dec(self):
        var_kind = ""
        if self._tokenizer.get_next_token_content() == "static":
            var_kind = "static"
        elif self._tokenizer.get_next_token_content() == "field":
            var_kind = "field"

        self._tokenizer.advance_token_ptr()
        var_type = self._tokenizer.get_next_token_content()
        self._tokenizer.advance_token_ptr()
        self._symbol_table.define(self._tokenizer.get_next_token_content(), var_type, var_kind)
        self._tokenizer.advance_token_ptr()
        while self._tokenizer.get_next_token_content() == ",":
            #getting ,
            self._tokenizer.advance_token_ptr()
            #getting the var name
            self._symbol_table.define(self._tokenizer.get_next_token_content(), var_type, var_kind)
            self._tokenizer.advance_token_ptr()
        #;
        self._tokenizer.advance_token_ptr()


    def compile_subroutine(self, subroutine_type_):

        self._symbol_table.start_subroutine(self._class_name, subroutine_type_)
        self._tokenizer.advance_token_ptr()

        #subroutine name
        self._tokenizer.advance_token_ptr()

        subroutine_name = self._class_name + "." + self._tokenizer.get_next_token_content()
        # (
        self._tokenizer.advance_token_ptr()
        self._tokenizer.advance_token_ptr()

        if subroutine_type_ == "method":
            self._symbol_table.define("this",  self._class_name, self.ARGUMENT)

        self.compile_parameter_list()

        #{
        self._tokenizer.advance_token_ptr()
        self._tokenizer.advance_token_ptr()

        #subroutine body
        self.compile_subroutine_body(subroutine_name, subroutine_type_)

        #
        # #get subroutine start: constructor|unction|method then void|type the subrioutine name then (
        # for i in range(0,4):
        #     self._analysis_tokens += self.get_next_line()
        #     self._tokenizer.advance_token_ptr()
        # self.compile_parameter_list()
        #
        # #writing ) to end parameter list
        # self._analysis_tokens += self.get_next_line()
        # self._tokenizer.advance_token_ptr()
        #
        # #subroutine body
        # self.compile_subroutine_body()
        #
        # self._analysis_tokens += [self.get_brackets_end_line("subroutineDec") + "\n"]

    def compile_parameter_list(self):

        var_kind = self.ARGUMENT
        while self._tokenizer.get_next_token_content() != ")":
            if self._tokenizer.get_next_token_content() == ",":
                self._tokenizer.advance_token_ptr()
            var_type = self._tokenizer.get_next_token_content()
            self._tokenizer.advance_token_ptr()
            var_name = self._tokenizer.get_next_token_content()
            self._symbol_table.define(var_name, var_type, var_kind)
            self._tokenizer.advance_token_ptr()

    #compiling subroutine body
    def compile_subroutine_body(self, subroutine_name_, subroutine_type_):
          #getting subroutine body
        local_var_cnt = 0
        while self._tokenizer.get_next_token_content() == "var":
            local_var_cnt += self.compile_var_dec()

        self._compiled_lines+= self._vm_writer.write_function(subroutine_name_, local_var_cnt)

        if subroutine_type_ == self.CONSTANT:
            fields_cnt = self._symbol_table.var_count("field")
            self._compiled_lines+= self._vm_writer.write_push(self.CONSTANT, fields_cnt + 1)
            self._compiled_lines+= self._vm_writer.write_call("Memory.alloc", 1)
            self._compiled_lines+= self._vm_writer.write_pop(self.POINTER, 0)
        elif subroutine_type_ == "method":
            self._compiled_lines+= self._vm_writer.write_push(self.ARGUMENT, 0)
            self._compiled_lines+= self._vm_writer.write_pop(self.POINTER, 0)

        self.compile_statement()

    #compiling subroutine var declerations
    def compile_var_dec(self):
        var_cnt = 0
        var_kind = "var"
        self._tokenizer.advance_token_ptr()
        var_type = self._tokenizer.get_next_token_content()
        self._tokenizer.advance_token_ptr()
        self._symbol_table.define(self._tokenizer.get_next_token_content(), var_type, var_kind)
        var_cnt += 1
        self._tokenizer.advance_token_ptr()
        #getting var deceleration
        while self._tokenizer.get_next_token_content() != ";":
            self._tokenizer.advance_token_ptr()
            self._compiled_lines += self.get_next_line()
            self._symbol_table.define(self._tokenizer.get_next_token_content(), var_type, var_kind)
            self._tokenizer.advance_token_ptr()

        self._tokenizer.advance_token_ptr()
        return var_cnt

    #compiling subroutine statements
    def compile_statement(self):
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

    def compile_return(self):
        self._tokenizer.advance_token_ptr()
        if (self._tokenizer.get_next_token_content() != ";"):
            self.compile_expression()
        else:
            self._compiled_lines += self._vm_writer.write_push(self.CONSTANT, 0)

        self._compiled_lines += self._vm_writer.write_return()
        self._tokenizer.advance_token_ptr()

    def compile_do(self):

        self._tokenizer.advance_token_ptr()
        token_1 = self._tokenizer.get_next_token_content()
        self._tokenizer.advance_token_ptr()
        token_2 = self._tokenizer.get_next_token_content()
        self.compile_call_subroutine(token_1, token_2)
        self._compiled_lines += self._vm_writer.write_pop(self.TEMP, 0)
        self._tokenizer.advance_token_ptr()

    def compile_while(self):
        self._labe_cnt += 1
        while_start = self._class_name + ".LABEL_" + str(self._labe_cnt)
        self._labe_cnt += 1
        while_end = self._class_name + ".LABEL_" + str(self._labe_cnt)
        self._compiled_lines += self._vm_writer.write_label(while_start)
        self._tokenizer.advance_token_ptr()
        self._tokenizer.advance_token_ptr()
        self.compile_expression()
        self._compiled_lines += self._vm_writer.write_arithmatic("not")
        self._compiled_lines += self._vm_writer.write_if(while_end)
        self._tokenizer.advance_token_ptr()
        self._tokenizer.advance_token_ptr()
        self.compile_statement()
        self._tokenizer.advance_token_ptr()
        self._compiled_lines += self._vm_writer.write_go_to(while_start)
        self._compiled_lines += self._vm_writer.write_label(while_end)

    def compile_if(self):
        self._labe_cnt += 1
        else_start =  self._class_name + ".LABEL_" + str(self._labe_cnt)
        self._labe_cnt += 1
        else_end = self._class_name + ".LABEL_" + str(self._labe_cnt)
        self._tokenizer.advance_token_ptr()
        self._tokenizer.advance_token_ptr()
        self.compile_expression()
        # }
        self._tokenizer.advance_token_ptr()
        self._compiled_lines += self._vm_writer.write_go_to(else_end)
        self._compiled_lines += self._vm_writer.write_go_to(else_start)
        if self._tokenizer.get_next_token_content() == "else":
            self._tokenizer.advance_token_ptr()
            self._tokenizer.advance_token_ptr()
            self.compile_statement()
        self._compiled_lines += self._vm_writer.write_label(else_end)

    def compile_let(self):
        self._tokenizer.advance_token_ptr()
        var_name = self._tokenizer.get_next_token_content()
        self._tokenizer.advance_token_ptr()
        array_flag = False
        if self._tokenizer.get_next_token_content() == "[":
            array_flag = True
            self._tokenizer.advance_token_ptr()
            self.compile_expression()
            self._compiled_lines += self._vm_writer.write_push(self._symbol_table.kind_of(var_name), self._symbol_table.index_of(var_name))
            self._compiled_lines += self._vm_writer.write_arithmatic("add")
            self._tokenizer.advance_token_ptr()

        self._tokenizer.advance_token_ptr()
        self.compile_expression()

        if array_flag:
            self._compiled_lines += self._vm_writer.write_pop("temp", 0)
            self._compiled_lines += self._vm_writer.write_pop(self.POINTER, 1)
            self._compiled_lines += self._vm_writer.write_push("temp", 0)
            self._compiled_lines += self._vm_writer.write_push("that", 0)
        else:
            self._compiled_lines += self._vm_writer.write_pop(self._symbol_table.kind_of(var_name), self._symbol_table.index_of(var_name))
        self._tokenizer.advance_token_ptr()

    def compile_expression(self):
        self.compile_term()

        while self._tokenizer.get_next_token_content() in ["*", "&lt;", "&gt;", "=", "-", "+", "/", "|", "&amp;"]:
            op = self._tokenizer.get_next_token_content()
            self._tokenizer.advance_token_ptr()
            self.compile_term()

            if op == "|":
                self._compiled_lines += self._vm_writer.write_arithmatic("or")
            elif op == "&":
                self._compiled_lines += self._vm_writer.write_arithmatic("and")
            elif op == "/":
                self._compiled_lines += self._vm_writer.write_call("Math.divide", 2)
            elif op == "*":
                self._compiled_lines += self._vm_writer.write_call("Math.multiply", 2)
            elif op == ">":
                self._compiled_lines += self._vm_writer.write_arithmatic("gt")
            elif op == "=":
                self._compiled_lines += self._vm_writer.write_arithmatic("eq")
            elif op == "<":
                self._compiled_lines += self._vm_writer.write_arithmatic("lt")
            elif op == "-":
                self._compiled_lines += self._vm_writer.write_arithmatic("sub")
            elif op == "+":
                self._compiled_lines += self._vm_writer.write_arithmatic("add")


    def compile_term(self):
        if self._tokenizer.get_next_token_content() == "(":
            self._tokenizer.advance_token_ptr()
            self.compile_expression()
            self._tokenizer.advance_token_ptr()
        elif self._tokenizer.get_next_token_content() in ["-", "~"]:
            unary_operator = self._tokenizer.get_next_token_content()
            self._tokenizer.advance_token_ptr()
            self.compile_term()
            self._compiled_lines += self._vm_writer.write_arithmatic(unary_operator)
        else:
            #getting the token
            token_1 = self._tokenizer.get_next_token_content()
            if self._tokenizer.get_next_token_type() == "keyword":
                if token_1 == "true":
                   self._compiled_lines += self._vm_writer.write_push(self.CONSTANT, 0)
                   self._compiled_lines += self._vm_writer.write_arithmatic("not")
                elif token_1 in ["null", "false"]:
                   self._compiled_lines += self._vm_writer.write_push(self.CONSTANT, 0)
                elif token_1 == "this":
                   self._compiled_lines += self._vm_writer.write_push(self.POINTER, 0)
                self._tokenizer.advance_token_ptr()
                return
            elif token_1 == "integerConstant":
                self._compiled_lines += self._vm_writer.write_push(self.CONSTANT, int(token_1))
                self._tokenizer.advance_token_ptr()
                return
            elif token_1 == "stringConstant":
                self._compiled_lines += self._vm_writer.write_push(self.CONSTANT, len(token_1) -2)
                self._compiled_lines += self._vm_writer.write_call("String.new", 1);
                for i, c in enumerate(token_1):
                    if i in [0, len(token_1) -1]:
                        continue
                    self._compiled_lines += self._vm_writer.write_push(self.CONSTANT, c)
                    self._compiled_lines += self._vm_writer.write_call("String.appendChar", 2)
                self._tokenizer.advance_token_ptr()
                return


            #if we got here then self._tokenizer.get_next_token_type() is identifier
            self._tokenizer.advance_token_ptr()
            token_2 = self._tokenizer.get_next_token_content()
            if self._tokenizer.get_next_token_content() == "[":
                self._tokenizer.advance_token_ptr()
                self.compile_expression()
                # ]
                self._compiled_lines += self._vm_writer.write_push(self._symbol_table.kind_of(token_1), self._symbol_table.index_of(token_1))
                self._compiled_lines += self._vm_writer.write_arithmatic("add")
                self._compiled_lines += self._vm_writer.write_pop(self.POINTER, 1)
                self._compiled_lines += self._vm_writer.write_push(self.THAT, 0)
                self._tokenizer.advance_token_ptr()
            elif token_2 == "(" or token_2 == ".":
                self.compile_call_subroutine(token_1, token_2)
            else:
                self._compiled_lines += self._vm_writer.write_push(self._symbol_table.kind_of(token_1), self._symbol_table.index_of(token_1))


    def compile_expression_list(self):
        args_cnt = 0

        if self._tokenizer.get_next_token_content() != ")":
            args_cnt += 1
            self.compile_expression()
            while self._tokenizer.get_next_token_content() == ",":
                args_cnt += 1
                self._tokenizer.advance_token_ptr()
                self.compile_expression()
        return args_cnt

    def compile_call_subroutine(self, token_1, token_2):
        token = ""
        if self._tokenizer.get_next_token_content() != "(":
            self._tokenizer.advance_token_ptr()
            token = self._tokenizer.get_next_token_content()
            self._tokenizer.advance_token_ptr()
        args_cnt = 0
        function_name = ""
        if token_2 == ".":
            function_name = self._class_name + "." + token_1
            self._compiled_lines += self._vm_writer.write_push(self.POINTER, 0)
            args_cnt += 1
        elif self._symbol_table.kind_of(token_1 != None):
            function_name = self._symbol_table.type_of(token_1) + "." + token
            self._compiled_lines += self._vm_writer.write_push(self._symbol_table.kind_of(token_1), self._symbol_table.index_of(token_1))
            args_cnt +=1
        else:
            function_name = token_1 + "." + token
        self._tokenizer.advance_token_ptr()
        args_cnt += self.compile_expression_list()
        # )
        self._compiled_lines += self._vm_writer.write_call(function_name, args_cnt)
        self._tokenizer.advance_token_ptr()
