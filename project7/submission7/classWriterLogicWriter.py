import CodeWriter
class classWriterLogicWriter:

    @staticmethod
    def check_signs(label_counter_):
        return [CodeWriter.CodeWriter.ADDRESS_SIGN + CodeWriter.CodeWriter.SP, "A = M" ,"D = M", CodeWriter.CodeWriter.ADDRESS_SIGN + "R14", "M = D", CodeWriter.CodeWriter.ADDRESS_SIGN + "R13", "D = D & M", "D = !D",
                CodeWriter.CodeWriter.ADDRESS_SIGN + "R15", "M = D", CodeWriter.CodeWriter.ADDRESS_SIGN + "R14", "D = M", CodeWriter.CodeWriter.ADDRESS_SIGN + "R13", "D = M | D", CodeWriter.CodeWriter.ADDRESS_SIGN + "R15",
                "D = D & M", CodeWriter.CodeWriter.ADDRESS_SIGN + "LABEL_DIFF" + str(label_counter_), "D;" + CodeWriter.CodeWriter.logic_table[CodeWriter.CodeWriter.LT]]
    @staticmethod
    def first_case(value_,label_counter_):
        return [CodeWriter.CodeWriter.ADDRESS_SIGN + "R13", "D = M", CodeWriter.CodeWriter.ADDRESS_SIGN + "R14", "D = D - M", CodeWriter.CodeWriter.ADDRESS_SIGN + "T" + str(label_counter_),
                "D;" + CodeWriter.CodeWriter.logic_table[value_], CodeWriter.CodeWriter.ADDRESS_SIGN + "F" + str(label_counter_), "0;JMP"]


    @staticmethod
    def second_case(value_,label_counter_):
        return ["(LABEL_DIFF_" + str(label_counter_) + ")", CodeWriter.CodeWriter.ADDRESS_SIGN + "R13", "D = M", CodeWriter.CodeWriter.ADDRESS_SIGN + "T" + str(label_counter_),
                "D;" + CodeWriter.CodeWriter.logic_table[value_], CodeWriter.CodeWriter.ADDRESS_SIGN + "F" + str(label_counter_), "0;JMP"]

    @staticmethod
    def get_false(label_counter_):
        ret_lines = ["(F" + str(label_counter_) + ")"]
        ret_lines += [CodeWriter.CodeWriter.ADDRESS_SIGN + CodeWriter.CodeWriter.SP]
        ret_lines += ["M = M - 1"]
        ret_lines += ["A = M", "M = 0", CodeWriter.CodeWriter.ADDRESS_SIGN + "FINISH" + str(label_counter_), "0;JMP"]
        return ret_lines

    @staticmethod
    def get_true(label_counter_):
        ret_lines = ["(T" + str(label_counter_) + ")", CodeWriter.CodeWriter.ADDRESS_SIGN + "0", "D = !A"]
        ret_lines += [CodeWriter.CodeWriter.ADDRESS_SIGN + CodeWriter.CodeWriter.SP]
        ret_lines += ["M = M - 1"]
        ret_lines += ["A = M", "M = D", CodeWriter.CodeWriter.ADDRESS_SIGN + "FINISH" + str(label_counter_), "0;JMP"]
        return ret_lines

    @staticmethod
    def get_end(label_counter_):
        return  ["(FINISH" + str(label_counter_) + ")", CodeWriter.CodeWriter.ADDRESS_SIGN + CodeWriter.CodeWriter.SP, "M = M + 1"]


