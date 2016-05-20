
class VMwriter:

    #writing push
    def write_push(self, segment_name_, index_):
        return ["push", " ", segment_name_, " ", str(index_), "\n"]

    def write_function(self, subroutine_name_, local_var_cnt_):
        return ["function", " ", subroutine_name_, " ", str(local_var_cnt_), "\n"]

    def write_call(self, call_command_, args_cnt_):
        return ["call", " ", call_command_, " ", str(args_cnt_), "\n"]

    def write_pop(self, segment_name_, index_):
        return ["pop", " ", segment_name_, " ", str(index_), "\n"]

    def write_arithmatic(self, command_name_):
        return [command_name_ + "\n"]

    def write_go_to(self, label_):
        return ["goto", " ", label_, "\n"]

    def write_label(self, label_):
        return ["label", " ", label_, "\n"]

    def write_if(self, label_):
        return ["if-goto " + label_ + "\n"]

    def write_goto(self, label_):
        return ["goto " + label_ + "\n"]

    def write_return(self):
        return ["return" + "\n"]

