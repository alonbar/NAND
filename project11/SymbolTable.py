class SymbolTable:
    STATIC = "static"
    FIELD = "this"
    ARGUEMENT = "argument"
    VAR = "local"

    def __init__(self):
        self._class_table = {}
        self._subroutine_talbe = {}
        self._static_index = -1
        self._field_index = -1
        self._arg_index = -1
        self._var_index = -1

    #starting a new subroutine, reseting class vars
    def start_subroutine(self, class_name_, subroutine_type):
        self._var_index = -1
        self._arg_index = -1
        self._subroutine_talbe = {}


    def define(self, name_, type_, kind_):
        kind_index = 0
        var_kind = ""
        if kind_ == "static":
            self._static_index += 1
            kind_index = self._static_index
            var_kind = self.STATIC
        elif kind_ == "var":
            self._var_index += 1
            kind_index = self._var_index
            var_kind = self.VAR
        elif kind_ == "argument":
            self._arg_index += 1
            kind_index = self._arg_index
            var_kind = self.ARGUEMENT
        elif kind_ == "field":
            self._field_index += 1
            kind_index = self._field_index
            var_kind = self.FIELD


        new_identifier = {"type": type_, "kind": var_kind, "kind_index": kind_index}
        if kind_ == "static" or kind_ == "field":
            self._class_table[name_] = new_identifier
        else:
            self._subroutine_talbe[name_] = new_identifier

    def var_count(self, kind_):
        if kind_ == self.STATIC:
            return self._static_index
        elif kind_ == self.FIELD:
            return self._field_index
        elif kind_ == self.ARGUEMENT:
            return self._arg_index
        elif kind_ == self.VAR:
            return self._var_index

    def index_of(self, name_):
        if name_ in self._subroutine_talbe:
            return self._subroutine_talbe[name_]["kind_index"]
        elif name_ in self._class_table:
            return self._class_table[name_]["kind_index"]
        else:
            return None

    def kind_of(self, name_):
        if name_ in self._subroutine_talbe:
            return self._subroutine_talbe[name_]["kind"]
        elif name_ in self._class_table:
            return self._class_table[name_]["kind"]
        else:
            return None

    def type_of(self, name_):
        if name_ in self._subroutine_talbe:
            return self._subroutine_talbe[name_]["type"]
        elif name_ in self._class_table:
            return self._class_table[name_]["type"]
        else:
            return None
