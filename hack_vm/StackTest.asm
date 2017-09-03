//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算eq
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL0
D;JEQ
@SP
A=M
M=0
@END0
0;JMP
(LABEL0)
@SP
A=M
M=-1
(END0)
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算eq
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL1
D;JEQ
@SP
A=M
M=0
@END1
0;JMP
(LABEL1)
@SP
A=M
M=-1
(END1)
@SP
M=M+1

//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算eq
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL2
D;JEQ
@SP
A=M
M=0
@END2
0;JMP
(LABEL2)
@SP
A=M
M=-1
(END2)
@SP
M=M+1

//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算lt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL3
D;JLT
@SP
A=M
M=0
@END3
0;JMP
(LABEL3)
@SP
A=M
M=-1
(END3)
@SP
M=M+1

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算lt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL4
D;JLT
@SP
A=M
M=0
@END4
0;JMP
(LABEL4)
@SP
A=M
M=-1
(END4)
@SP
M=M+1

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算lt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL5
D;JLT
@SP
A=M
M=0
@END5
0;JMP
(LABEL5)
@SP
A=M
M=-1
(END5)
@SP
M=M+1

//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算gt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL6
D;JGT
@SP
A=M
M=0
@END6
0;JMP
(LABEL6)
@SP
A=M
M=-1
(END6)
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算gt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL7
D;JGT
@SP
A=M
M=0
@END7
0;JMP
(LABEL7)
@SP
A=M
M=-1
(END7)
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算gt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
D=M-D
@LABEL8
D;JGT
@SP
A=M
M=0
@END8
0;JMP
(LABEL8)
@SP
A=M
M=-1
(END8)
@SP
M=M+1

//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

//push constant 53
@53
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

//push constant 112
@112
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

//计算neg
@SP
M=M-1
@SP
A=M
M=-M
@SP
M=M+1
//计算neg结束

//计算and
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D&M
@SP
M=M+1
//计算and结束

//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

//计算or
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D|M
@SP
M=M+1
//计算or结束

//计算not
@SP
M=M-1
@SP
A=M
M=!M
@SP
M=M+1
//计算not结束

