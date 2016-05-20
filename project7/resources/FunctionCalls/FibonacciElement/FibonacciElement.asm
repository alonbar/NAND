@256
D = A
@SP
M = D
@callback_0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@2
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@3
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@4
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@0
D = D - A
@5
D = D - A
@ARG
M = D
@SP
D = M
@R14
A = M
@LCL
M = D
@ARG
D = M
@Sys.init
0;JMP
(callback_0)
(Main.fibonacci)
@0
D = A
@ARG
A = D + M
A = M
D = A
@SP
A = M
M = D
D = M
@SP
M = M + 1
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1
@SP
M = M - 1
@SP
M = M - 1
@SP
A = M
D = M
@R13
M = D
@SP
M = M + 1
@SP
A = M
D = M
@R14
M = D
@R13
D = D & M
D = !D
@R15
M = D
@R14
D = M
@R13
D = M | D
@R15
D = D & M
@LABEL_DIFF0
D;JLT
@R13
D = M
@R14
D = D - M
@T0
D;JLT
@F0
0;JMP
(LABEL_DIFF_0)
@R13
D = M
@T0
D;JLT
@F0
0;JMP
(T0)
@0
D = !A
@SP
M = M - 1
A = M
M = D
@FINISH0
0;JMP
(F0)
@SP
M = M - 1
A = M
M = 0
@FINISH0
0;JMP
(FINISH0)
@SP
M = M + 1
@SP
M = M - 1
A = M
D = M
@Main.fibonacci::IF_TRUE
D;JNE
@Main.fibonacci::IF_FALSE
0;JMP
(Main.fibonacci::IF_TRUE)
@0
D = A
@ARG
A = D + M
A = M
D = A
@SP
A = M
M = D
D = M
@SP
M = M + 1
@1
D = M
@5
A = D - A
D = M
@R15
M = D
@2
D = M
@R13
M = D
@R14
A = M
@SP
A = M - 1
D = M
@R13
A = M
M = D
@R13
D = M
@SP
M = D + 1
@1
D = M
@R13
M = D
@R13
D = M
@R14
A =M
@4
D = D - A
@R14
M = D
A = M
D = M
@1
M = D
D = M
@R13
M = D
D = M
@R13
M = D
@R14
M = M + 1
@2
D = M
@R13
M = D
A = M
D = M
@R13
M = D
@R14
A = M
D = M
@2
M = D
@R14
M = M + 1
@3
D = M
@R13
M = D
A = M
D = M
@R13
M = D
@R14
A = M
D = M
@3
M = D
@R14
M = M + 1
@4
D = M
@R13
M = D
A = M
D = M
@R13
M = D
@R14
A = M
D = M
@4
M = D
@R14
M = M + 1
@R15
A = M
0;JMP
(Main.fibonacci::IF_FALSE)
@0
D = A
@ARG
A = D + M
A = M
D = A
@SP
A = M
M = D
D = M
@SP
M = M + 1
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1
@SP
A = M - 1
D = M
A = A - 1
M = M - D
@SP
M = M - 1
@callback_1
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@2
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@3
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@4
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@1
D = D - A
@5
D = D - A
@ARG
M = D
@SP
D = M
@R14
A = M
@LCL
M = D
@ARG
D = M
@Main.fibonacci
0;JMP
(callback_1)
@0
D = A
@ARG
A = D + M
A = M
D = A
@SP
A = M
M = D
D = M
@SP
M = M + 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1
@SP
A = M - 1
D = M
A = A - 1
M = M - D
@SP
M = M - 1
@callback_2
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@2
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@3
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@4
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@1
D = D - A
@5
D = D - A
@ARG
M = D
@SP
D = M
@R14
A = M
@LCL
M = D
@ARG
D = M
@Main.fibonacci
0;JMP
(callback_2)
@SP
A = M - 1
D = M
A = A - 1
M = M + D
@SP
M = M - 1
@1
D = M
@5
A = D - A
D = M
@R15
M = D
@2
D = M
@R13
M = D
@R14
A = M
@SP
A = M - 1
D = M
@R13
A = M
M = D
@R13
D = M
@SP
M = D + 1
@1
D = M
@R13
M = D
@R13
D = M
@R14
A =M
@4
D = D - A
@R14
M = D
A = M
D = M
@1
M = D
D = M
@R13
M = D
D = M
@R13
M = D
@R14
M = M + 1
@2
D = M
@R13
M = D
A = M
D = M
@R13
M = D
@R14
A = M
D = M
@2
M = D
@R14
M = M + 1
@3
D = M
@R13
M = D
A = M
D = M
@R13
M = D
@R14
A = M
D = M
@3
M = D
@R14
M = M + 1
@4
D = M
@R13
M = D
A = M
D = M
@R13
M = D
@R14
A = M
D = M
@4
M = D
@R14
M = M + 1
@R15
A = M
0;JMP
(Sys.init)
@4
D = A
@SP
A = M
M = D
@SP
M = M + 1
@callback_3
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@2
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@3
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@4
A = M
D = A
@R14
M = D
@SP
A = M
M = D
@SP
M = M + 1
@SP
D = M
@1
D = D - A
@5
D = D - A
@ARG
M = D
@SP
D = M
@R14
A = M
@LCL
M = D
@ARG
D = M
@Main.fibonacci
0;JMP
(callback_3)
(Sys.init::WHILE)
@Sys.init::WHILE
0;JMP
