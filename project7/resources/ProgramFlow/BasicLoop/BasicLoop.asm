@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@LCL
D = D + M
@R15
M = D
@SP
A = M - 1
D = M
@R15
A = M
M = D
@SP
M = M - 1
(BasicLoop::LOOP_START)
@0
D = A
@ARG
A = D + M
A = M
D = A
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@LCL
A = D + M
A = M
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
@0
D = A
@LCL
D = D + M
@R15
M = D
@SP
A = M - 1
D = M
@R15
A = M
M = D
@SP
M = M - 1
@0
D = A
@ARG
A = D + M
A = M
D = A
@SP
A = M
M = D
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
@0
D = A
@ARG
D = D + M
@R15
M = D
@SP
A = M - 1
D = M
@R15
A = M
M = D
@SP
M = M - 1
@0
D = A
@ARG
A = D + M
A = M
D = A
@SP
A = M
M = D
@SP
M = M + 1
@SP
M = M - 1
A = M
D = M
@BasicLoop::LOOP_START
D;JNE
@0
D = A
@LCL
A = D + M
A = M
D = A
@SP
A = M
M = D
@SP
M = M + 1