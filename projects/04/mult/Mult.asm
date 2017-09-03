// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@i
M=1 // i=1

@j
M=1 // j=1

@0
D=M
@base
M=D // base = R0

@2
M=0 // R2=0

(LOOP)
@i
D=M // D=i

@15
D=D-A // D=D-15

@END
D;JGT // if (D-15)>0 goto END

@j
D=M // D=j
@1
D=M&D // D=R1&D

@NEXT
D;JEQ

@base
D=M // D=base
@2
M=M+D // R2=R2+base

(NEXT)
@base
D=M // D=base
M=D+M // base=base*2

@j
D=M
M=D+M // j=j*2

@i
M=M+1 // i++

@LOOP
0;JMP

(END)
@END
0;JMP