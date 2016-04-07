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
A = M - 1
D = M
@R14
A = M
M = D
@SP
M = M - 1
(Sys.init$LOOP_START)
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
@SP
A = M - 1
D = M
A = A - 1
M = D + M
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
A = M - 1
D = M
@R14
A = M
M = D
@SP
M = M - 1
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
@1
D = A
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
@ARG
D = M
@0
D = D + A
@R14
M = D
A = M
D = M
@SP
A = M - 1
D = M
@R14
A = M
M = D
@SP
M = M - 1
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
M = M - 1
A = M
D = M
@Sys.init$LOOP_START
D;JNE
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
