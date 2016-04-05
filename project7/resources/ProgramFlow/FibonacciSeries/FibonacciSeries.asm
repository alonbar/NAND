@1
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
A = M - 1
D = M
@THAT
M = D
@SP
M = M - 1
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1
@0
D = A
@THAT
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
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1
@1
D = A
@THAT
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
(FibonacciSeries::MAIN_LOOP_START)
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
@FibonacciSeries::COMPUTE_ELEMENT
D;JNE
@FibonacciSeries::END_PROGRAM
0:jmp
(FibonacciSeries::COMPUTE_ELEMENT)
@0
D = A
@THAT
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
@THAT
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
@2
D = A
@THAT
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
@THAT
D = M
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
M = M + D
@SP
M = M - 1
@SP
A = M - 1
D = M
@THAT
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
@FibonacciSeries::MAIN_LOOP_START
0:jmp
(FibonacciSeries::END_PROGRAM)
