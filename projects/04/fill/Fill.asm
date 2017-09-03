// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

@16384
D=A
@base
M=D // base=16384

(LOOP)

@24576
D=M // 取键盘的值

@CLEAR
D;JEQ // 如果等于0，说明没有按键，那么执行clear

@i
M=0
(BLACKLOOP)
@i
D=M
@8192
D=D-A

@LOOP
D;JGE

@i
D=M
@base
D=D+M // D=i+16384
A=D // 神来之笔，哈哈哈
M=1 // M[i]=1

@i
M=M+1
@BLACKLOOP
0;JMP

(CLEAR)
@i
M=0

(CLEARLOOP) // 把屏幕像素的设为白色
@i
D=M

@8192
D=D-A

@LOOP
D;JGE

@i
D=M
@base
D=D+M // D=i+16384
A=D
M=0 // M[i]=0

@i
M=M+1 // i++

@CLEARLOOP
0;JMP

@LOOP
0;JMP