class Parser(object):
	def __init__(self, filename):
		print("parser.py:" + filename)
		self.f = open(filename, "r")
		self.lines = self.f.readlines()
		self.index = 0
		self.function = ""

	def hasMoreCommands(self):
		if self.index < len(self.lines):
			self.advance = self.lines[self.index].strip()
			self.index = self.index + 1
			if self.advance.startswith("//") or self.advance == "":
				return self.hasMoreCommands()
			elif "//" in self.advance:
					self.advance = self.advance[:self.advance.find("//")].strip()
			return True
		else:
			return False

	def commandType(self):
		if self.advance == "add" or self.advance == "sub" or self.advance == "neg" or self.advance == "eq" or self.advance == "gt" or self.advance == "lt" or self.advance == "and" or self.advance == "or" or self.advance == "not":
			return "C_ARITHMETIC"
		elif self.advance.startswith("push"):
			return "C_PUSH"
		elif self.advance.startswith("pop"):
			return "C_POP"
		elif self.advance.startswith("label"):
			return "C_LABEL"
		elif self.advance.startswith("goto"):
			return "C_GOTO"
		elif self.advance.startswith("if-goto"):
			return "C_IF"
		elif self.advance.startswith("function"):
			return "C_FUNCTION"
		elif self.advance.startswith("return"):
			return "C_RETURN"
		elif self.advance.startswith("call"):
			return "C_CALL"

	def arg1(self, commandType):
		if commandType == "C_ARITHMETIC":
			return self.advance
		elif commandType == "C_PUSH" or commandType == "C_POP" or commandType == "C_FUNCTION" or commandType == "C_CALL":
			if commandType == "C_FUNCTION":
				self.function = self.advance.split()[1]
			return self.advance.split()[1]
		elif commandType == "C_LABEL" or commandType == "C_GOTO" or commandType == "C_IF":
			if self.function == "":
				return self.advance.split()[1]
			else:
				return  self.function + "$" + self.advance.split()[1]

	def arg2(self, commandType):
		if commandType == "C_PUSH" or commandType == "C_POP" or commandType == "C_FUNCTION" or commandType == "C_CALL":
			return self.advance.split()[2]

	def close(self):
		self.f.close()


