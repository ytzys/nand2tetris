class JackTokenizer(object):
	"""docstring for JackTokenizer"""
	def __init__(self, filename):
		super(JackTokenizer, self).__init__()
		self.filename = filename
		self.f = open(filename, "r")
		self.lines = self.f.readlines()
		self.index = 0

	def hasMoreTokens(self):
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


	def keyword(self):
		
		