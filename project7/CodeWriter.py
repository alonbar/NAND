
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

    def __init__(self):
        self._program_name = ""

    def set_program_name(self,program_name_):
        self._program_name = program_name_


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


    def get_push_line(self, memory_segment_, value_):
        if memory_segment_ == self.CONSTANT:
            return self.get_push_constant(value_)
        else:
            return self.get_push_segment(memory_segment_, value_)

    def get_pop_value(self, segment_, value_):
        ret_line = []
        if segment_ in self.segment_table:
            ret_line += [self.ADDRESS_SIGN + value_, "D = A", self.ADDRESS_SIGN + self.segment_table[segment_], "D = D + M", \
                         self.ADDRESS_SIGN + "R15", "M = D", self.ADDRESS_SIGN + self.SP, "A = M - 1", "D = M", \
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
            ret_line += [self.ADDRESS_SIGN + self.SP, "A = M - 1", "D = M","@" + self._program_name + "." + value_, "M = D"]
            ret_line += self.decrease_SP()
            return ret_line
        elif segment_ == "temp":
            ret_line += [self.ADDRESS_SIGN + self.SP, "A = M - 1", "D = M", self.ADDRESS_SIGN + str(int(value_) + 5), "M = D"]
            ret_line += self.decrease_SP()
            return ret_line

    def get_push_constant(self, value_):
        ret_line = [self.ADDRESS_SIGN + value_, "D = A", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
        ret_line += self.increase_SP()
        return ret_line

    def get_push_segment(self, segment_, value_):
        ret_line = []
        if segment_ in self.segment_table:
            ret_line += [self.ADDRESS_SIGN + value_, "D = A", self.ADDRESS_SIGN + self.segment_table[segment_], "A = D + M","A = M" ,"D = A", \
                        self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
            ret_line += self.increase_SP()
            return  ret_line
        elif segment_ == "pointer":
            #determining if it is @THIS or @THAT
            if int(value_) == 0:
                ret_line += [self.ADDRESS_SIGN + "THIS"]
            else:
                ret_line += [self.ADDRESS_SIGN + "THAT"]

            ret_line += ["D = M", self.ADDRESS_SIGN + self.SP, "A = M", "M = D"]
            ret_line += self.increase_SP()
            return  ret_line
        elif segment_ == "static":
            ret_line += ["@" + self._program_name + "." + value_]
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
        ret_lines += [self.ADDRESS_SIGN + self.SP, "A = M", "D = M", "@R13", "M = D"]
        ret_lines += self.increase_SP()

        #calculating different signs
        ret_lines += [self.ADDRESS_SIGN + self.SP, "A = M" ,"D = M", "@R14", "M = D", "@R13", "D = M & D", "D = !D", "@R15", "M = D", \
                     "@R14", "D = M", "@R13", "D = M | D", "@R15", "D = M & D", "@LABEL_DIFF" + str(self.label_counter), \
                     "D;" + self.logic_table[self.LT]]

        #IF we here it mean that they have same sign or one is 0 and second is positivie
        ret_lines += ["@R13", "D = M", "@R14", "D = D - M", "@T" + str(self.label_counter), "D;" + self.logic_table[value_], \
                      "@F" + str(self.label_counter), "0;JMP"]

        # IF WE here it mean that they have dif sign or one is 0 and second is negetive
        ret_lines += ["(LABEL_DIFF_" + str(self.label_counter) + ")", "@R13", "D = M", "@T" + str(self.label_counter), \
                      "D;" + self.logic_table[value_], "@F" + str(self.label_counter), "0;JMP"]
        #TRUE case
        ret_lines += ["(T" + str(self.label_counter) + ")", "@0", "D = !A"]
        ret_lines += self.decrease_SP()
        ret_lines += ["A = M", "M = D", "@FINISH" + str(self.label_counter), "0;JMP"]


        # FALSE case

        ret_lines += ["(F" + str(self.label_counter) + ")"]
        ret_lines += self.decrease_SP()
        ret_lines += ["A = M", "M = 0", "@FINISH" + str(self.label_counter), "0;JMP"]

        # END Case
        ret_lines += ["(FINISH" + str(self.label_counter) + ")", self.ADDRESS_SIGN + self.SP, "M = M + 1", ""]

        self.label_counter += 1

        return ret_lines

