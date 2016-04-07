@256
D = A
@0
M = D
@RETURN_ADD0
D = A
@SP
A = M
M = D
@SP
 M = M + 1
@LCL
D = M
@SP
A = M
M = D
@SP
 M = M + 1
@ARG
D = M
@SP
A = M
M = D
@SP
 M = M + 1
@THIS
D = M
@SP
A = M
M = D
@SP
 M = M + 1
@THAT
D = M
@SP
A = M
M = D
@SP
 M = M + 1
@SP
D = M
@LCL
M = D
@LCL
D = M
@5
D = D - A
@ARG
M = D
@Sys.init
0;JMP
(RETURN_ADD0)
(SimpleFunction.test)
@0
D = A
@SP
A = M
M = D
D = A + 1
@SP
M = D
@0
D = A
@SP
A = M
M = D
D = A + 1
@SP
M = D
@LCL
D = M
@0
D = D + A
@R14
M = D
A = M
D = M
@SP
A = M
M = D
D = A + 1
@SP
M = D
@LCL
D = M
@1
D = D + A
@R14
M = D
A = M
D = M
@SP
A = M
M = D
D = A + 1
@SP
M = D
@SP
A = M - 1
D = M
A = A - 1
M = D + M
D = A + 1
@SP
M = D
@SP
A = M - 1
M = !M
@ARG
D = M
@0
D = D + A
@R14
M = D
A = M
D = M
@SP
A = M
M = D
D = A + 1
@SP
M = D
@SP
A = M - 1
D = M
A = A - 1
M = D + M
D = A + 1
@SP
M = D
@ARG
D = M
@1
D = D + A
@R14
M = D
A = M
D = M
@SP
A = M
M = D
D = A + 1
@SP
M = D
@SP
A = M - 1
D = M
A = A - 1
M = M - D
D = A + 1
@SP
M = D
@LCL
D = M
@5
A = D - A
D = M
@R14
M = D
@SP
A = M - 1
D = M
@ARG
A = M
M = D
@ARG
D = M
@SP
M = D + 1
@LCL
D = M
@4
D = D - A
@R13
M = D
@R13
A = M
D = M
@LCL
M = D
@R13
M = M + 1
@R13
A = M
D = M
@ARG
M = D
@R13
M = M + 1
@R13
A = M
D = M
@THIS
M = D
@R13
M = M + 1
@R13
A = M
D = M
@THAT
M = D
@R13
M = M + 1

@R14
A = M
0;JMP
