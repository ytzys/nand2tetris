class Parser(object):
	
	def __init__(self, filename):
		self.f = open(filename, "r")
		self.lines = self.f.readlines()
		self.index = 0

	def hasMoreCommands(self):
		if self.index < len(self.lines):
			self.advance = self.lines[self.index].strip()
			self.index = self.index + 1
			if self.advance.startswith("//") or self.advance == "":
				return self.hasMoreCommands()
			else:
				if "//" in self.advance:
					# print(self.advance)
					tmp = self.advance.find("//")
					self.advance = self.advance[:tmp].strip()
				return True
		else:
			return False

	def commandType(self):
		if self.advance.startswith("@"):
			return "A_COMMAND"
		elif "(" in self.advance:
			return "L_COMMAND"
		else:
			return "C_COMMAND"

	def symbol(self):
		if "@" in self.advance:
			return self.advance[1:]  # @100这种形式的指令，返回100
		else:
			return self.advance[1:-1] # (LOOP)这种形式的指令，返回LOOP

	def dest(self):
		tmp = self.advance.find("=")
		if tmp == -1:
			return "null" # 没有“=”号的指令，dest为null
		else:
			return self.advance[0:tmp] # D=M 返回D

	def comp(self):
		tmp1 = self.advance.find("=")
		# if tmp1 == -1:
		# 	tmp1 = 0
		tmp2 = self.advance.find(";")
		if tmp2 == -1:
			tmp2 = len(self.advance)
		return self.advance[tmp1+1:tmp2] # dest=comp;jump “=”和“;”之间

	def jump(self):
		tmp = self.advance.find(";")
		if tmp == -1:
			return "null"
		else:
			return self.advance[tmp+1:]

	def close(self):
		self.f.close();

