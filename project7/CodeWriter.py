import classWriterLogicWriter
class CodeWriter:
    PUSH = "push"
    POP = "pop"
    CONSTANT = "constant"
    SP = "SP"
    ADDRESS_SIGN = "@"
    EQ = "eq"
    NEG = "neg"
    GT = "gt"
    NOT = "not"
    LT = "lt"
    logic_table = {EQ : "JEQ", GT : "JGT", LT : "JLT"}
    binary_table = {"add": "+", "sub" : "-", "eq" : "=", "and": "&", "or" : "|"}
    segment_table = {"local" : "LCL", "argument" : "ARG", "this": "THIS", "that" : "THAT"}
    label_counter = 0
    _function_counter = 0
    def __init__(self):
        self._program_name = "Sys.init"
        self._vm_name = ""

    def set_program_name(self,program_name_):
        self._vm_name = program_name_

    def write_bootstrap(self):
        ret_lines = [self.ADDRESS_SIGN + "256", "D = A", self.ADDRESS_SIGN + self.SP, "M = D"]
        ret_lines += self.get_call_line('Sys.init', str(0))
        return  ret_lines

    def get_call_line(self, function_name_, parameter_):
        callback_add = "callback_"
        label = "(" + callback_add+ str(self._function_counter) + ")"
        ret_lines = [self.ADDRESS_SIGN + callback_add+ str(self._function_counter), "D = A", self.ADDRESS_SIGN + self.SP,
                     "A = M", "M = D"]
        ret_lines += self.increase_SP()
        ret_lines += [self.ADDRESS_SIGN + "1", "A = M", "D = A", self.ADDRESS_SIGN + "R14", "M = D", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
        ret_lines += self.increase_SP()
        ret_lines += [self.ADDRESS_SIGN + "2", "A = M", "D = A", self.ADDRESS_SIGN + "R14", "M = D", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
        ret_lines += self.increase_SP()
        ret_lines += [self.ADDRESS_SIGN + "3", "A = M", "D = A", self.ADDRESS_SIGN + "R14", "M = D", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
        ret_lines += self.increase_SP()
        ret_lines += [self.ADDRESS_SIGN + "4", "A = M", "D = A", self.ADDRESS_SIGN + "R14", "M = D", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
        ret_lines += self.increase_SP()
        ret_lines += [self.ADDRESS_SIGN + "SP", "D = M", self.ADDRESS_SIGN + parameter_, "D = D - A", self.ADDRESS_SIGN + "5", "D = D - A", self.ADDRESS_SIGN + "ARG", "M = D",
                      self.ADDRESS_SIGN + self.SP, "D = M", self.ADDRESS_SIGN + "R14", "A = M", self.ADDRESS_SIGN + "LCL", "M = D", self.ADDRESS_SIGN + "ARG", "D = M", self.ADDRESS_SIGN + function_name_, "0;JMP", label]
        self._function_counter +=1
        return ret_lines

    def write_line(self, line):
         if self.PUSH == line[0]:
            return self.get_push_line(line[1], line[2])
         elif self.POP == line[0]:
            return self.get_pop_value(line[1], line[2])
         elif line[0] == self.NOT:
             return self.get_not_line()
         elif line[0] == self.NEG:
             return self.get_neg_line()
         elif line[0] in [self.GT, self.LT, self.EQ]:
             return self.get_logic_line(line[0])
         elif line[0] in self.binary_table:
             return self.get_arithmatic_binary_operator(line[0])
         elif "label" in line[0]:
             return self.get_label_line(line[1])
         elif "if-goto" in line[0]:
             return self.get_if_line(line[1])
         elif "goto" in line[0]:
             return self.get_goto_line(line[1])
         elif "function" in line[0]:
             return self.get_function_line(line[1], line[2])
         elif "call" in line[0]:
             return self.get_call_line(line[1], line[2])
         elif "return" in line[0]:
             return  self.get_return_line()


    def get_return_line(self):

        ret_lines = [self.ADDRESS_SIGN + "1", "D = M", self.ADDRESS_SIGN +"5", "A = D - A", "D = M", self.ADDRESS_SIGN +"R15", "M = D", self.ADDRESS_SIGN + "2", "D = M", self.ADDRESS_SIGN + "R13", "M = D",
                     self.ADDRESS_SIGN + "R14", "A = M", self.ADDRESS_SIGN +"SP", "A = M - 1", "D = M", self.ADDRESS_SIGN +"R13", "A = M", "M = D", self.ADDRESS_SIGN +"R13", "D = M",
                     self.ADDRESS_SIGN +"SP", "M = D + 1", self.ADDRESS_SIGN + "1", "D = M", self.ADDRESS_SIGN + "R13", "M = D", self.ADDRESS_SIGN +"R13", "D = M",
                     self.ADDRESS_SIGN + "R14", "A =M", self.ADDRESS_SIGN +"4", "D = D - A", self.ADDRESS_SIGN +"R14", "M = D", "A = M","D = M", self.ADDRESS_SIGN + "1", "M = D",  "D = M", self.ADDRESS_SIGN + "R13", "M = D"]

        ret_lines += ["D = M", self.ADDRESS_SIGN +"R13", "M = D", self.ADDRESS_SIGN +"R14", "M = M + 1", self.ADDRESS_SIGN + "2", "D = M", self.ADDRESS_SIGN + "R13", "M = D", "A = M", "D = M", self.ADDRESS_SIGN +"R13", "M = D",
                      self.ADDRESS_SIGN + "R14", "A = M", "D = M", self.ADDRESS_SIGN + "2", "M = D", self.ADDRESS_SIGN +"R14", "M = M + 1", self.ADDRESS_SIGN + "3", "D = M", self.ADDRESS_SIGN + "R13", "M = D", "A = M", "D = M",
                      self.ADDRESS_SIGN +"R13", "M = D", self.ADDRESS_SIGN + "R14", "A = M", "D = M", self.ADDRESS_SIGN + "3", "M = D", self.ADDRESS_SIGN +"R14", "M = M + 1", self.ADDRESS_SIGN + "4", "D = M", self.ADDRESS_SIGN + "R13",
                      "M = D", "A = M", "D = M", self.ADDRESS_SIGN +"R13", "M = D", self.ADDRESS_SIGN + "R14", "A = M", "D = M", self.ADDRESS_SIGN + "4", "M = D", self.ADDRESS_SIGN +"R14", "M = M + 1", self.ADDRESS_SIGN +"R15",
                      "A = M", "0;JMP"]

        return ret_lines

    def get_function_line(self, function_name_, parameter_):
        self._program_name = function_name_
        ret_lines = ["(" + self._program_name + ")"]
        for i in range(int(parameter_)):
            ret_lines += [self.ADDRESS_SIGN + "0", "D = A"]
            ret_lines += [self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
            ret_lines += self.increase_SP()
        return ret_lines

    def get_if_line(self, value_):
        return [self.ADDRESS_SIGN + self.SP, "M = M - 1", "A = M", "D = M",
                self.ADDRESS_SIGN + self._program_name + "::" + value_, "D;JNE"]

    def get_goto_line(self, value_):
        return [self.ADDRESS_SIGN + self._program_name + "::" + value_, "0;JMP"]

    def get_label_line(self, value_):
        return ["(" + self._program_name + "::" + value_ + ")"]

    def get_push_line(self, memory_segment_, value_):
        if memory_segment_ == self.CONSTANT:
            return self.get_push_constant(value_)
        else:
            return self.get_push_segment(memory_segment_, value_)

    def get_pop_value(self, segment_, value_):
        ret_line = []
        if segment_ in self.segment_table:
            ret_line += [self.ADDRESS_SIGN + value_, "D = A", self.ADDRESS_SIGN + self.segment_table[segment_], "D = D + M",
                         self.ADDRESS_SIGN + "R15", "M = D", self.ADDRESS_SIGN + self.SP, "A = M - 1", "D = M",
                         self.ADDRESS_SIGN + "R15", "A = M", "M = D"]
            ret_line += self.decrease_SP()
            return ret_line
        elif segment_ == "pointer":
            choose_seg = ""
            if int(value_) == 1:
                choose_seg = "THAT"
            else:
                choose_seg = "THIS"
            ret_line += [self.ADDRESS_SIGN + self.SP, "A = M - 1", "D = M", self.ADDRESS_SIGN + choose_seg, "M = D"]
            ret_line += self.decrease_SP()
            return  ret_line
        elif segment_ == "static":
            ret_line += [self.ADDRESS_SIGN + self.SP, "A = M - 1", "D = M",self.ADDRESS_SIGN + self._vm_name + "." + value_,  "M = D"]
            ret_line += self.decrease_SP()
            return ret_line
        elif segment_ == "temp":
            ret_line += [self.ADDRESS_SIGN + self.SP, "A = M - 1", "D = M", self.ADDRESS_SIGN + str(int(value_) + 5),  "M = D"]
            ret_line += self.decrease_SP()
            return ret_line

    def get_push_constant(self, value_):
        ret_line = [self.ADDRESS_SIGN + value_, "D = A", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
        ret_line += self.increase_SP()
        return ret_line

    def get_push_segment(self, segment_, value_):
        ret_line = []
        if segment_ in self.segment_table:
            ret_line += [self.ADDRESS_SIGN + value_, "D = A", self.ADDRESS_SIGN + self.segment_table[segment_], "A = D + M","A = M" ,"D = A",
                        self.ADDRESS_SIGN + self.SP, "A = M", "M = D", "D = M"]
            ret_line += self.increase_SP()
            return  ret_line
        elif segment_ == "pointer":
            if int(value_) == 0:
                ret_line += [self.ADDRESS_SIGN + "THIS"]
            else:
                ret_line += [self.ADDRESS_SIGN + "THAT"]

            ret_line += ["D = M", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
            ret_line += self.increase_SP()
            return  ret_line
        elif segment_ == "static":
            ret_line += ["@" + self._vm_name + "." + value_]
            ret_line += ["D = M"]
            ret_line += [self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
            ret_line += self.increase_SP()
            return  ret_line
        elif segment_ == "temp":
            ret_line += [self.ADDRESS_SIGN + str(int(value_) + 5), "D = M"]
            ret_line += [self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
            ret_line += self.increase_SP()
            return ret_line


    def increase_SP(self):
        ret_line = [self.ADDRESS_SIGN + self.SP]
        ret_line += ["M = M + 1"]
        return ret_line


    def decrease_SP(self):
        ret_line = [self.ADDRESS_SIGN + self.SP]
        ret_line += ["M = M - 1"]
        return ret_line

    def get_arithmatic_line(self, value_):
        if value_ in self.binary_table:
            return self.get_arithmatic_binary_operator(value_)

    def get_arithmatic_binary_operator(self, value_):
        ret_line = [self.ADDRESS_SIGN + self.SP]
        ret_line += ["A = M - 1"]
        ret_line += ["D = M"]
        ret_line += ["A = A - 1"]
        ret_line += ["M = M " + self.binary_table[value_] + " D"]
        ret_line += self.decrease_SP()
        return ret_line

    def get_neg_line(self):
        ret_line = [self.ADDRESS_SIGN + self.SP]
        ret_line += ["A = M - 1"]
        ret_line += ["M = -M"]
        return ret_line

    def get_not_line(self):
        ret_line = [self.ADDRESS_SIGN + self.SP]
        ret_line += ["A = M - 1"]
        ret_line += ["M = !M"]
        return ret_line

    def get_logic_line(self, value_):
        jmp_val = self.logic_table[value_]
        ret_lines = self.decrease_SP()
        ret_lines += self.decrease_SP()
        ret_lines += [self.ADDRESS_SIGN + self.SP, "A = M", "D = M", self.ADDRESS_SIGN + "R13", "M = D"]
        ret_lines += self.increase_SP()
        ret_lines += classWriterLogicWriter.classWriterLogicWriter.check_signs(self.label_counter)
        ret_lines += classWriterLogicWriter.classWriterLogicWriter.first_case(value_,self.label_counter)
        ret_lines += classWriterLogicWriter.classWriterLogicWriter.second_case(value_,self.label_counter)
        ret_lines += classWriterLogicWriter.classWriterLogicWriter.get_true(self.label_counter)
        ret_lines += classWriterLogicWriter.classWriterLogicWriter.get_false(self.label_counter)
        ret_lines += classWriterLogicWriter.classWriterLogicWriter.get_end(self.label_counter)
        self.label_counter += 1
        return ret_lines

