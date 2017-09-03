//push argument 1
@1
D=A
@ARG
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@R4
M=D
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop that 0
@0
D=A
@THAT
M=D+M
@SP
M=M-1
@SP
A=M
D=M
@THAT
A=M
M=D
@0
D=A
@THAT
M=M-D

//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop that 1
@1
D=A
@THAT
M=D+M
@SP
M=M-1
@SP
A=M
D=M
@THAT
A=M
M=D
@1
D=A
@THAT
M=M-D

//push argument 0
@0
D=A
@ARG
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算sub
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1
//计算sub结束

//pop argument 0
@0
D=A
@ARG
M=D+M
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@0
D=A
@ARG
M=M-D

//label
(MAIN_LOOP_START)

//push argument 0
@0
D=A
@ARG
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//if-goto
@SP
M=M-1
@SP
A=M
D=M
@COMPUTE_ELEMENT
D;JNE

//goto
@END_PROGRAM
0;JMP
//label
(COMPUTE_ELEMENT)

//push that 0
@0
D=A
@THAT
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//push that 1
@1
D=A
@THAT
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//计算add
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=D+M
@SP
A=M
M=D
@SP
M=M+1
//计算add结束

//pop that 2
@2
D=A
@THAT
M=D+M
@SP
M=M-1
@SP
A=M
D=M
@THAT
A=M
M=D
@2
D=A
@THAT
M=M-D

//push pointer 1
@R4
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算add
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=D+M
@SP
A=M
M=D
@SP
M=M+1
//计算add结束

//pop pointer 1
@SP
M=M-1
@SP
A=M
D=M
@R4
M=D
//push argument 0
@0
D=A
@ARG
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算sub
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1
//计算sub结束

//pop argument 0
@0
D=A
@ARG
M=D+M
@SP
M=M-1
@SP
A=M
D=M
@ARG
A=M
M=D
@0
D=A
@ARG
M=M-D

//goto
@MAIN_LOOP_START
0;JMP
//label
(END_PROGRAM)

