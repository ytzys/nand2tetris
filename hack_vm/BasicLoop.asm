//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

//pop local 0
@0
D=A
@LCL
M=D+M
@SP
M=M-1
@SP
A=M
D=M
@LCL
A=M
M=D
@0
D=A
@LCL
M=M-D

//label
(LOOP_START)

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
//push local 0
@0
D=A
@LCL
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

//pop local 0
@0
D=A
@LCL
M=D+M
@SP
M=M-1
@SP
A=M
D=M
@LCL
A=M
M=D
@0
D=A
@LCL
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
@LOOP_START
D;JNE

//push local 0
@0
D=A
@LCL
A=M
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
