@17
D = A
@SP
A = M
M = D
@SP
M = M + 1
@17
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
D = M & D
D = !D
@R15
M = D
@R14
D = M
@R13
D = M | D
@R15
D = M & D
@LABEL_DIFF0
D;JLT
@R13
D = M
@R14
D = D - M
@T0
D;JEQ
@F0
0;JMP
(LABEL_DIFF_0)
@R13
D = M
@T0
D;JEQ
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

@892
D = A
@SP
A = M
M = D
@SP
M = M + 1
@891
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
D = M & D
D = !D
@R15
M = D
@R14
D = M
@R13
D = M | D
@R15
D = M & D
@LABEL_DIFF1
D;JLT
@R13
D = M
@R14
D = D - M
@T1
D;JLT
@F1
0;JMP
(LABEL_DIFF_1)
@R13
D = M
@T1
D;JLT
@F1
0;JMP
(T1)
@0
D = !A
@SP
M = M - 1
A = M
M = D
@FINISH1
0;JMP
(F1)
@SP
M = M - 1
A = M
M = 0
@FINISH1
0;JMP
(FINISH1)
@SP
M = M + 1

@32767
D = A
@SP
A = M
M = D
@SP
M = M + 1
@32766
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
D = M & D
D = !D
@R15
M = D
@R14
D = M
@R13
D = M | D
@R15
D = M & D
@LABEL_DIFF2
D;JLT
@R13
D = M
@R14
D = D - M
@T2
D;JGT
@F2
0;JMP
(LABEL_DIFF_2)
@R13
D = M
@T2
D;JGT
@F2
0;JMP
(T2)
@0
D = !A
@SP
M = M - 1
A = M
M = D
@FINISH2
0;JMP
(F2)
@SP
M = M - 1
A = M
M = 0
@FINISH2
0;JMP
(FINISH2)
@SP
M = M + 1

@56
D = A
@SP
A = M
M = D
@SP
M = M + 1
@31
D = A
@SP
A = M
M = D
@SP
M = M + 1
@53
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
M = M + D
@SP
M = M - 1
@112
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
@SP
A = M - 1
M = -M
@SP
A = M - 1
D = M
A = A - 1
M = M & D
@SP
M = M - 1
@82
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
M = M | D
@SP
M = M - 1
