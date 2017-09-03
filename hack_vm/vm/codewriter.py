class CodeWriter(object):
	"""docstring for CodeWriter"""
	def __init__(self, file):
		self.file = file
		self.f = open(self.file, "w")
		self.labelindex = 0
		self.endindex = 0
		self.fucntionReturnAddressLabelIndex = 0
		print(self.file)

	def setFileName(self, filename):
		self.filename = filename

	def  writeInit(self):
		self.f.write("@256\n")
		self.f.write("D=A\n")
		self.f.write("@SP\n")
		self.f.write("M=D\n")
		self.writeCall("Sys.init", 0)

	def writeArithmetic(self, command):
		if command == "add":
			self.f.write("//计算add\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M\n") # D=RAM[sp]，至此取到了堆栈里的第一个值

			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=D+M\n") # 取到堆栈的第二个值，并加法

			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=D\n") # 加法结果进入堆栈（可以简化，参加sub过程）

			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("//计算add结束\n")
			self.f.write("\n")
		elif command == "sub":
			self.f.write("//计算sub\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M\n") # D=RAM[sp]，至此取到了堆栈里的第一个值

			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=M-D\n") # 取到堆栈的第二个值，并减法，结果进入堆栈

			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("//计算sub结束\n")
			self.f.write("\n")
		elif command == "neg":
			self.f.write("//计算neg\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=-M\n")

			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("//计算neg结束\n")
			self.f.write("\n")
		elif command == "eq":
			self.f.write("//计算eq\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M\n") # D=RAM[sp]，至此取到了堆栈里的第一个值

			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M-D\n") # 取到堆栈的第二个值，相减

			self.f.write("@LABEL" + str(self.labelindex) + "\n")
			self.f.write("D;JEQ\n")

			self.f.write("@SP\n") # 栈顶压入false
			self.f.write("A=M\n")
			self.f.write("M=0\n")

			self.f.write("@END" + str(self.endindex) + "\n")
			self.f.write("0;JMP\n")
			

			self.f.write("(LABEL" + str(self.labelindex) + ")\n") # 栈顶压入true
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=-1\n")

			self.f.write("(END" + str(self.endindex) + ")\n")
			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("\n")
			self.labelindex = self.labelindex + 1
			self.endindex = self.endindex + 1

		elif command == "gt":
			self.f.write("//计算gt\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M\n") # D=RAM[sp]，至此取到了堆栈里的第一个值

			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M-D\n") # 取到堆栈的第二个值，相减

			self.f.write("@LABEL" + str(self.labelindex) + "\n")
			self.f.write("D;JGT\n")

			self.f.write("@SP\n") # 栈顶压入false
			self.f.write("A=M\n")
			self.f.write("M=0\n")

			self.f.write("@END" + str(self.endindex) + "\n")
			self.f.write("0;JMP\n")
			

			self.f.write("(LABEL" + str(self.labelindex) + ")\n") # 栈顶压入true
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=-1\n")

			self.f.write("(END" + str(self.endindex) + ")\n")
			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("\n")
			self.labelindex = self.labelindex + 1
			self.endindex = self.endindex + 1
		elif command == "lt":
			self.f.write("//计算lt\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M\n") # D=RAM[sp]，至此取到了堆栈里的第一个值

			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M-D\n") # 取到堆栈的第二个值，相减

			self.f.write("@LABEL" + str(self.labelindex) + "\n")
			self.f.write("D;JLT\n")

			self.f.write("@SP\n") # 栈顶压入false
			self.f.write("A=M\n")
			self.f.write("M=0\n")

			self.f.write("@END" + str(self.endindex) + "\n")
			self.f.write("0;JMP\n")
			

			self.f.write("(LABEL" + str(self.labelindex) + ")\n") # 栈顶压入true
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=-1\n")

			self.f.write("(END" + str(self.endindex) + ")\n")
			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("\n")
			self.labelindex = self.labelindex + 1
			self.endindex = self.endindex + 1
		elif command == "and":
			self.f.write("//计算and\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M\n") # D=RAM[sp]，至此取到了堆栈里的第一个值

			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=D&M\n") # 取到堆栈的第二个值，&，结果进入堆栈

			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("//计算and结束\n")
			self.f.write("\n")
		elif command == "or":
			self.f.write("//计算or\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("D=M\n") # D=RAM[sp]，至此取到了堆栈里的第一个值

			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=D|M\n") # 取到堆栈的第二个值，|，结果进入堆栈

			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("//计算or结束\n")
			self.f.write("\n")
		elif command == "not":
			self.f.write("//计算not\n")
			self.f.write("@SP\n")
			self.f.write("M=M-1\n") # sp-1
			self.f.write("@SP\n")
			self.f.write("A=M\n")
			self.f.write("M=!M\n")

			self.f.write("@SP\n")
			self.f.write("M=M+1\n") # sp+1
			self.f.write("//计算not结束\n")
			self.f.write("\n")

	def writePushPop(self, commandType, segment, index):
		if commandType == "C_PUSH":
			if segment == "constant":
				self.f.write("//push constant " + index + "\n")
				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
				self.f.write("\n")
			elif segment == "local":
				self.f.write("//push local " + index +"\n")
				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@LCL\n")
				self.f.write("A=M\n")
				self.f.write("A=D+A\n")
				self.f.write("D=M\n") # 取到local[index]的值
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
			elif segment == "argument":
				self.f.write("//push argument " + index +"\n")
				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@ARG\n")
				self.f.write("A=M\n")
				self.f.write("A=D+A\n")
				self.f.write("D=M\n") # 取到argument[index]的值
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
			elif segment == "this":
				self.f.write("//push this " + index +"\n")
				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@THIS\n")
				self.f.write("A=M\n")
				self.f.write("A=D+A\n")
				self.f.write("D=M\n") # 取到this[index]的值
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
			elif segment == "that":
				self.f.write("//push that " + index +"\n")
				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@THAT\n")
				self.f.write("A=M\n")
				self.f.write("A=D+A\n")
				self.f.write("D=M\n") # 取到that[index]的值
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
			elif segment == "temp":
				self.f.write("//push temp " + index +"\n")
				tmp = 5 + int(index)
				self.f.write("@R" + str(tmp) + "\n")
				self.f.write("D=M\n") # 取到temp[index]的值
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
			elif segment == "pointer":
				self.f.write("//push pointer " + index +"\n")
				tmp = 3 + int(index)
				self.f.write("@R" + str(tmp) + "\n")
				self.f.write("D=M\n") # 取到pointer[index]的值
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
			elif segment == "static":
				self.f.write("//push static " + index + "\n")
				self.f.write("@" + self.filename + "." + index + "\n")
				self.f.write("D=M\n")

				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				self.f.write("@SP\n")
				self.f.write("M=M+1\n")
				self.f.write("\n")

		elif commandType == "C_POP":
			if segment == "local":
				self.f.write("//pop local " + index +"\n")

				################ 一个崭新的算法start ###########################
				# 把LCL指针指向ARG+index
				self.f.write("@" + index +"\n")
				self.f.write("D=A\n")
				self.f.write("@LCL\n")
				self.f.write("M=D+M\n")

				# 堆栈指针减1
				self.f.write("@SP\n")
				self.f.write("M=M-1\n")

				# 取栈顶的值
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("D=M\n")

				# 写入LCL+index中
				self.f.write("@LCL\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")

				# 把ARG指针指向原来的位置
				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@LCL\n")
				self.f.write("M=M-D\n")
				self.f.write("\n")
				################ 一个崭新的算法end ###########################


				################ 旧算法，比较低效 ###########################
				# # 先取到栈顶的值，放入D
				# self.f.write("@SP\n")
				# self.f.write("M=M-1\n")
				# self.f.write("@SP\n")
				# self.f.write("A=M\n")
				# self.f.write("D=M\n")

				# # 通过连续的使用A=A+1，把A指向需要修改的ARG的位置，ARG[index]
				# self.f.write("@LCL\n")
				# self.f.write("A=M\n")
				# if int(index) != 0:
				# 	for i in range(1, int(index) + 1):
				# 		self.f.write("A=A+1\n")
				# self.f.write("M=D\n")

			elif segment == "argument":

				self.f.write("//pop argument " + index + "\n")
				self.f.write("@" + index +"\n")
				self.f.write("D=A\n")
				self.f.write("@ARG\n")
				self.f.write("M=D+M\n")


				self.f.write("@SP\n")
				self.f.write("M=M-1\n")
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("D=M\n")

				self.f.write("@ARG\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")
				
				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@ARG\n")
				self.f.write("M=M-D\n")
				self.f.write("\n")

			elif segment == "this":
				self.f.write("//pop this " + index +"\n")
				self.f.write("@" + index +"\n")
				self.f.write("D=A\n")
				self.f.write("@THIS\n")
				self.f.write("M=D+M\n")

				self.f.write("@SP\n")
				self.f.write("M=M-1\n")
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("D=M\n")

				self.f.write("@THIS\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")

				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@THIS\n")
				self.f.write("M=M-D\n")
				self.f.write("\n")
			elif segment == "that":
				self.f.write("//pop that " + index +"\n")
				self.f.write("@" + index +"\n")
				self.f.write("D=A\n")
				self.f.write("@THAT\n")
				self.f.write("M=D+M\n")

				self.f.write("@SP\n")
				self.f.write("M=M-1\n")
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("D=M\n")

				self.f.write("@THAT\n")
				self.f.write("A=M\n")
				self.f.write("M=D\n")

				self.f.write("@" + index + "\n")
				self.f.write("D=A\n")
				self.f.write("@THAT\n")
				self.f.write("M=M-D\n")
				self.f.write("\n")
			elif segment == "temp":
				self.f.write("//pop temp " + index +"\n")

				self.f.write("@SP\n")
				self.f.write("M=M-1\n")
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("D=M\n")

				tmp = 5 + int(index)
				self.f.write("@R" + str(tmp) + "\n") # 对，R0-R15是可以直接用的
				self.f.write("M=D\n")

				# self.f.write("@SP\n")
				# self.f.write("M=M-1\n")
				# self.f.write("@SP\n")
				# self.f.write("A=M\n")
				# self.f.write("D=M\n")

				# self.f.write("@5\n")
				# self.f.write("A=M\n")
				# if int(index) != 0:
				# 	for i in range(1, int(index) + 1):
				# 		self.f.write("A=A+1\n")
				# self.f.write("M=D\n")
			elif segment == "pointer":
				self.f.write("//pop pointer " + index +"\n")

				self.f.write("@SP\n")
				self.f.write("M=M-1\n")
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("D=M\n")

				tmp = 3 + int(index)
				self.f.write("@R" + str(tmp) + "\n") # 对，R0-R15是可以直接用的
				self.f.write("M=D\n")
			elif segment == "static":
				self.f.write("//pop static " + index +"\n")
				self.f.write("@SP\n")
				self.f.write("M=M-1\n")
				self.f.write("@SP\n")
				self.f.write("A=M\n")
				self.f.write("D=M\n")

				self.f.write("@" + self.filename + "." + index + "\n")
				self.f.write("M=D\n")
				self.f.write("\n")

	def writeLabel(self, label):
		self.f.write("//label\n")
		self.f.write("(" + label + ")\n")
		self.f.write("\n")


	def writeGoto(self, label):
		self.f.write("//goto\n")
		self.f.write("@" + label + "\n")
		self.f.write("0;JMP")
		self.f.write("\n")

	def writeIf(self, label):
		self.f.write("//if-goto\n")
		self.f.write("@SP\n")
		self.f.write("M=M-1\n")
		self.f.write("@SP\n")
		self.f.write("A=M\n")
		self.f.write("D=M\n")
		self.f.write("@" + label + "\n")
		self.f.write("D;JNE\n")
		self.f.write("\n")

	def writeCall(self, functionName, numArgs):
		self.f.write("//call\n")
		self.f.write("@return-address" + str(self.fucntionReturnAddressLabelIndex) + "\n")
		self.f.write("D=A\n")
		self.f.write("@SP\n")
		self.f.write("A=M\n")
		self.f.write("M=D\n")
		self.f.write("@SP\n")
		self.f.write("M=M+1\n")

		self.f.write("@LCL\n")
		self.f.write("D=M\n")
		self.f.write("@SP\n")
		self.f.write("A=M\n")
		self.f.write("M=D\n")
		self.f.write("@SP\n")
		self.f.write("M=M+1\n")

		self.f.write("@ARG\n")
		self.f.write("D=M\n")
		self.f.write("@SP\n")
		self.f.write("A=M\n")
		self.f.write("M=D\n")
		self.f.write("@SP\n")
		self.f.write("M=M+1\n")

		self.f.write("@THIS\n")
		self.f.write("D=M\n")
		self.f.write("@SP\n")
		self.f.write("A=M\n")
		self.f.write("M=D\n")
		self.f.write("@SP\n")
		self.f.write("M=M+1\n")

		self.f.write("@THAT\n")
		self.f.write("D=M\n")
		self.f.write("@SP\n")
		self.f.write("A=M\n")
		self.f.write("M=D\n")
		self.f.write("@SP\n")
		self.f.write("M=M+1\n")

		self.f.write("@" + str(numArgs) + "\n")
		self.f.write("D=A\n")
		self.f.write("@SP\n")
		self.f.write("D=M-D\n")
		self.f.write("@5\n")
		self.f.write("D=D-A\n")
		self.f.write("@ARG\n")
		self.f.write("M=D\n")

		self.f.write("@SP\n")
		self.f.write("D=M\n")
		self.f.write("@LCL\n")
		self.f.write("M=D\n")

		self.writeGoto(functionName)
		self.f.write("(return-address" + str(self.fucntionReturnAddressLabelIndex) + ")\n")
		self.f.write("\n")
		self.fucntionReturnAddressLabelIndex = self.fucntionReturnAddressLabelIndex + 1

	def writeReturn(self):
		self.f.write("//return\n")
		self.f.write("@LCL\n")
		self.f.write("D=M\n")
		self.f.write("@13\n")
		self.f.write("M=D\n")

		self.f.write("@5\n")
		self.f.write("D=A\n")
		self.f.write("@13\n")
		self.f.write("D=M-D\n")
		self.f.write("A=D\n")
		self.f.write("D=M\n")
		self.f.write("@14\n")
		self.f.write("M=D\n")

		self.f.write("@SP\n")
		self.f.write("M=M-1\n")
		self.f.write("@SP\n")
		self.f.write("A=M\n")
		self.f.write("D=M\n")
		self.f.write("@ARG\n")
		self.f.write("A=M\n")
		self.f.write("M=D\n")

		self.f.write("@ARG\n")
		self.f.write("D=M\n")
		self.f.write("@SP\n")
		self.f.write("M=D+1\n")

		self.f.write("@13\n")
		self.f.write("A=M\n")
		self.f.write("A=A-1\n")
		self.f.write("D=M\n")
		self.f.write("@THAT\n")
		self.f.write("M=D\n")

		self.f.write("@2\n")
		self.f.write("D=A\n")
		self.f.write("@13\n")
		self.f.write("A=M\n")
		self.f.write("A=A-D\n")
		self.f.write("D=M\n")
		self.f.write("@THIS\n")
		self.f.write("M=D\n")

		self.f.write("@3\n")
		self.f.write("D=A\n")
		self.f.write("@13\n")
		self.f.write("A=M\n")
		self.f.write("A=A-D\n")
		self.f.write("D=M\n")
		self.f.write("@ARG\n")
		self.f.write("M=D\n")

		self.f.write("@4\n")
		self.f.write("D=A\n")
		self.f.write("@13\n")
		self.f.write("A=M\n")
		self.f.write("A=A-D\n")
		self.f.write("D=M\n")
		self.f.write("@LCL\n")
		self.f.write("M=D\n")

		self.f.write("@14\n")
		self.f.write("A=M\n")
		self.f.write("0;JMP\n")
		self.f.write("\n")

	def writeFunction(self, functionName, numArgs):
		self.f.write("//function\n")
		self.f.write("(" + functionName + ")\n")
		for i in range(numArgs):
			self.writePushPop("C_PUSH", "constant", "0")
		self.f.write("\n")

	def close(self):
		self.f.close()


