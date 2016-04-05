import re
import sys
import os.path
import glob

class Parser:
    
    def __init__(self, file_path):
        self._lines = []
        self._currentLine = 0

        # open file and get all the text
        file_object = open(file_path, 'r')
        all_text = file_object.read()
        file_object.close()
        
        # remove all comments and spaces
        all_lines = all_text.split("\n")
        for line in all_lines:
            line = re.sub(re.compile("//.*?$"), "", line)
            line = " ".join(line.split())
            if line != "":
                self._lines.append(line)
                
#     Return true if there are more commands in the file            
    def hasMoreCommands(self):
        if self._currentLine >= len(self._lines):
            return False
        else:
            return True

    def advance(self):
        self._current_command = self._lines[self._currentLine]
        self._currentLine += 1
        
    def commandType(self):
        if self._current_command.strip() in ["add","sub","neg","eq","gt","lt","and","or","not"]:
            return "C_ARITHMETIC"
        elif "push" in self._current_command:
            return "C_PUSH"
        elif "pop" in self._current_command:
            return "C_POP"
        elif "label" in self._current_command:
            return "C_LABEL"
        elif "if" in self._current_command:
            return "C_IF"
        elif "goto" in self._current_command:
            return "C_GOTO"
        elif "function" in self._current_command:
            return "C_FUNCTION"
        elif "return" in self._current_command:
            return "C_RETURN"
        elif "call" in self._current_command:
            return "C_CALL"
        return "ERROR"

        
#   Returns the first argument of the current command. 
#   In the case of C_ARITHMETIC, the command itself (add, sub, etc.) is returned.
#   Should not be called if the current command is C_RETURN.
    def arg1(self):
        split_command = self._current_command.split()
        if self.commandType() == "C_ARITHMETIC":
            return self._current_command
        else:
            return split_command[1]
        
    def arg2(self):
        split_command = self._current_command.split()
        return split_command[2]

    def arg0(self):
        split_command = self._current_command.split()
        return split_command[0]


class CodeWriter:
    def __init__(self, output_file_path):
        self._file_to_write = open(output_file_path, "w")
        self._arith_dic = {"add": "M = D + M", "sub": "M = M - D", "and": "M = D & M", "or": "M = D|M", "neg": "M = - M", "eq": "D;JEQ", "gt": "D;JGT", "lt": "D;JLT", "not": "M = !M"}
        self._logic_dic = {"eq" : "", "gt": "D;JGE", "lt": "D;JLT"}
        self._logic_counter = 0
        self.VMName = ''
        self.currentFunc = "Sys.init"
    
    def setFileName(self, fileName):
        self.VMName = os.path.basename(fileName[:-3])
    
    def writeInit(self):
        lines_to_return = []
        
        #Set SP = 256
        lines_to_return += ["@256", "D = A", "@0", "M = D",""]
        
        self._file_to_write.write('\n'.join(lines_to_return))
        
        self.writeCall('Sys.init', 0)
    
    def writeLabel(self, label):
        self._file_to_write.write("(" + self.currentFunc + "$" + label + ')\n')
    
    def writeGoto(self, label):
        lines_to_return = []

        lines_to_return += ["@" +  self.currentFunc + "$" + label, "0;JMP", ""]
        
        self._file_to_write.write('\n'.join(lines_to_return))
        
    def writeIf(self, label):
        lines_to_return = []

        lines_to_return += ["@SP", "M = M - 1", "A = M", "D = M", "@" + self.currentFunc + "$" + label, "D;JNE", ""]

        self._file_to_write.write('\n'.join(lines_to_return))
        
        
    def writeCall(self, functionName, numArgs):
        lines_to_return = []
        
        # PUSH RETURN ADDRESS
        lines_to_return += ["@RETURN_ADD" + str(self._logic_counter), "D = A", "@SP", "A = M", "M = D", "@SP", " M = M + 1"]
        
        # PUSH LCL
        lines_to_return += ["@LCL", "D = M", "@SP", "A = M", "M = D", "@SP", " M = M + 1"]
        
        # PUSH ARG
        lines_to_return += ["@ARG", "D = M", "@SP", "A = M", "M = D", "@SP", " M = M + 1"]
        
        # PUSH THIS
        lines_to_return += ["@THIS", "D = M", "@SP", "A = M", "M = D", "@SP", " M = M + 1"]
        
        # PUSH THAT
        lines_to_return += ["@THAT", "D = M", "@SP", "A = M", "M = D", "@SP", " M = M + 1"]
        
        # SET NEW POINTERS
        lines_to_return += ["@SP", "D = M", "@LCL", "M = D"]
        
        arg_new_pointer = 5 + int(numArgs)
        lines_to_return += ["@LCL", "D = M", "@" + str(arg_new_pointer), "D = D - A", "@ARG", "M = D"]
        
        # JUMP TO FUNCTION
        lines_to_return += ["@" + functionName, "0;JMP"]
        
        # WHERE TO REUTRN
        lines_to_return += ["(RETURN_ADD" + str(self._logic_counter) + ")", ""]
        
        self._file_to_write.write('\n'.join(lines_to_return))

        self._logic_counter += 1
        
    def writeReturn(self):
        lines_to_return = []

        # SAVE RETURN ADDRES IN R14
        lines_to_return += ["@LCL", "D = M", "@5", "A = D - A", "D = M", "@R14", "M = D"]

        # SET REUTRN VALUE AND RESET SP
        lines_to_return += ["@SP", "A = M - 1", "D = M", "@ARG", "A = M", "M = D", "@ARG", "D = M", "@SP", "M = D + 1"]
        
        # LCL ADD IN R13 FOR CALC
        lines_to_return += ["@LCL", "D = M", "@4", "D = D - A", "@R13", "M = D"]
        
        # SET LCL
        lines_to_return += ["@R13", "A = M", "D = M", "@LCL", "M = D", "@R13", "M = M + 1"]
        
        # SET ARG
        lines_to_return += ["@R13", "A = M", "D = M", "@ARG", "M = D", "@R13", "M = M + 1"]
        
        # SET THIS
        lines_to_return += ["@R13", "A = M", "D = M", "@THIS", "M = D", "@R13", "M = M + 1"]
        
        # SET THAT
        lines_to_return += ["@R13", "A = M", "D = M", "@THAT", "M = D", "@R13", "M = M + 1", ""]
        
        # GOTO RETURN STATMENT
        lines_to_return += ["@R14", "A = M", "0;JMP", ""]
        
        self._file_to_write.write('\n'.join(lines_to_return))
    
    def writeFunction(self, functionName, numLocals):
        self.currentFunc = functionName
        self._file_to_write.write("(" + functionName + ")\n")
        
        for i in range(int(numLocals)):
            self.WritePushPop("push", "constant", "0")
        
    
    def writeArithmetic(self, command):
        lines_to_return = []
        
        if any((x in command) for x in ["add","sub","and","or"]):
            lines_to_return += ["@SP","A = M - 1","D = M","A = A - 1", self._arith_dic[command],\
            "D = A + 1","@SP","M = D",'']
            
        elif any((x in command) for x in ["eq", "gt", "lt"]):
            # Check if sign is different
            lines_to_return += ['@SP', 'A = M - 1', 'A = A - 1', 'D = M', '@R13', 'M = D', '@SP', \
            'A = M - 1', 'D = M', '@R14', 'M = D', '@R13', 'D = M & D', 'D = !D', '@R15', 'M = D',\
            '@R13', 'D = M', '@R14', 'D = D | M', '@R15', 'D = M & D', '@DIFFERENT_SIGN_' \
            + str(self._logic_counter), 'D;JLT']
            
            #IF we here it mean that they have same sign or one is 0 and second is positivie    
            lines_to_return += ['@R13', 'D = M', '@R14', 'D = D - M', "@TRUE" + \
            str(self._logic_counter), self._arith_dic[command], '@FALSE'+ str(self._logic_counter)\
            , '0;JMP']
            
            # IF WE here it mean that they have dif sign or one is 0 and second is negetive
            lines_to_return += ['(DIFFERENT_SIGN_' + str(self._logic_counter) + ')', '@R13', \
            'D = M', '@TRUE' + str(self._logic_counter), self._logic_dic[command], '@FALSE' + \
            str(self._logic_counter), '0;JMP']
            
            #TRUE case
            lines_to_return += ["(TRUE" + str(self._logic_counter) + ")",  "@0", "D = !A", "@SP", \
            "A = M - 1", "A = A - 1", "M = D", "@END"+ str(self._logic_counter), "0;JMP"]

            # FALSE case
            lines_to_return += ['(FALSE'+ str(self._logic_counter) + ")", '@SP', 'A = M - 1', \
            'A = A - 1', 'M = 0', '@END' + str(self._logic_counter), '0;JMP'] 
            
            # END Case
            lines_to_return +=  ["(END" + str(self._logic_counter) + ")", "@SP", "M = M - 1", '']
            
            self._logic_counter += 1
            
        else:  # neg or not
            lines_to_return += ["@SP", "A = M - 1", self._arith_dic[command], '']

        self._file_to_write.write('\n'.join(lines_to_return))
        
    def WritePushPop(self, command, segment, index):
        # for stage 1 - only constant
        function_specific_segments = {'local' : '@LCL', 'argument' : '@ARG', 'this' : '@THIS', \
        'that' : '@THAT'}
        lines_to_return = []
        
        # Handle segment
        # keep address in R14, value in D
        if (segment == "constant"):
            lines_to_return += ["@" + index, "D = A"]
        elif (segment == "static"):
            lines_to_return += ["@" + self.VMName + "." + index, "D = A", "@R14", "M = D", \
            "A = M", "D = M"]
        elif (segment == "temp"):
            lines_to_return += ['@' + str(5 + int(index)), "D = A", "@R14", "M = D", "A = M",\
            "D = M"]
        elif (segment == "pointer"):
            lines_to_return += ['@THIS']
            if (index == "1"):
                lines_to_return += ['D = A + 1']
            else:
                lines_to_return += ['D = A']
            
            lines_to_return += ['@R14', 'M = D', 'A = M', 'D = M']
        else:
            # Must be local, argument, this or that
            lines_to_return += [function_specific_segments[segment]]
            lines_to_return += ['D = M', '@' + index, 'D = D + A', '@R14', 'M = D', "A = M",\
            "D = M"]
        
        # Handle push or pop        
        if (command == 'push'):   
            lines_to_return += ["@SP", "A = M", "M = D", "D = A + 1", "@SP", "M = D"]
        elif (command == 'pop'):
            lines_to_return += [ "@SP", "A = M - 1", "D = M", "@R14", "A = M", "M = D", "@SP", \
            "M = M - 1"]
            
        lines_to_return += ['']
        self._file_to_write.write('\n'.join(lines_to_return))

    
    def Close(self):
        self._file_to_write.close()

def main():
    input_file = sys.argv[1]
    files_to_translate = []
    output_path = ""
    if os.path.isdir(input_file):
        files_to_translate = glob.glob(os.path.realpath(input_file + "/*.vm"))
        output_path = os.path.realpath(input_file) + "/" + \
		      os.path.basename(os.path.normpath(input_file)) + ".asm"
    else:
        files_to_translate.append(input_file)
        output_path = os.path.realpath(input_file).replace(".vm", ".asm")       
        
    codeWriter = CodeWriter(output_path)
    codeWriter.writeInit()
    
    for vm_file in files_to_translate:
        parser = Parser(vm_file)
        codeWriter.setFileName(vm_file)
        while parser.hasMoreCommands():
            parser.advance()
            if parser.commandType() == "C_ARITHMETIC":
                codeWriter.writeArithmetic(parser.arg1())
            elif parser.commandType() == "C_PUSH" or parser.commandType() == "C_POP":
                codeWriter.WritePushPop(parser.arg0(), parser.arg1(), parser.arg2())
            elif parser.commandType() == "C_LABEL":
                codeWriter.writeLabel(parser.arg1())
            elif parser.commandType() == "C_IF":
                codeWriter.writeIf(parser.arg1())
            elif parser.commandType() == "C_GOTO":
                codeWriter.writeGoto(parser.arg1())
            elif parser.commandType() == "C_FUNCTION":
                codeWriter.writeFunction(parser.arg1(), parser.arg2())    
            elif parser.commandType() == "C_RETURN":
                codeWriter.writeReturn()
            elif parser.commandType() == "C_CALL":
                codeWriter.writeCall(parser.arg1(), parser.arg2())          
            
    codeWriter.Close()


if __name__ == '__main__':
    main()
    
    
    
    
    
