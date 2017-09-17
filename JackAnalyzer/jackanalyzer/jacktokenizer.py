import re
class JackTokenizer(object):
	"""docstring for JackTokenizer"""
	def __init__(self, filename):
		super(JackTokenizer, self).__init__()
		self.filename = filename
		self.f = open(filename, "r")
		self.lines = self.f.readlines()
		self.lineindex = 0
		self.currentline = ""
		self.tokenIndexPerLine = 0
		self.tokensPerLine = []
		self.tokencountPerLine = 0
		self.outputFileName = filename[:filename.find(".")] + "T.xml"
		self.outputfile = open(self.outputFileName, "w")
		print("outputfile:" + self.outputFileName)
		self.outputfile.write("<tokens>\n")
		self.keywordList = ["field", "class" , "method" , "int" , "function" , "boolean" , "constructor" , "char" , \
						"void" , "var" , "static" , "let" , "do" , "if" , "else" , "while" , "return", \
						"true" , "false" , "null" , "this"]
		self.symbolList = ["{", "}", "(", ")", "[", "]", ".", ",", ";", "+", "-", "*", "/", \
						"&", "|", "<", ">", "=", "~"]
		self.symbolListNeedEsc = ["{", "}", "(", ")", "[", "]", ".", "+", "*", "|"]
		self.symbolListNotNeedEsc = [",", ";", "-", "/", "&", "<", ">", "=", "~"]

	def hasMoreTokens(self):
			if self.tokenIndexPerLine < self.tokencountPerLine:
				self.advance = self.tokensPerLine[self.tokenIndexPerLine]
				self.tokenIndexPerLine = self.tokenIndexPerLine + 1
				return True
			else:
				if self.hasMoreLines():
					self.tokenIndexPerLine = 0
					self.tokensPerLine = self.currentline.split()
					self.tokencountPerLine = len(self.tokensPerLine)
					self.advance = self.tokensPerLine[self.tokenIndexPerLine]
					self.tokenIndexPerLine = self.tokenIndexPerLine + 1
					return True
				else:
					return False

	def hasMoreLines(self):
		if self.lineindex < len(self.lines):
			self.currentline = self.lines[self.lineindex].strip()
			if self.currentline.startswith("//") or self.currentline == "" \
				or self.currentline.startswith("/*") or self.currentline.startswith("*"):
				self.lineindex = self.lineindex + 1
				return self.hasMoreLines()
			if "//" in self.currentline:
				self.currentline = self.currentline[:self.currentline.find("//")].strip()
			elif "/*" in self.currentline:
				self.currentline = self.currentline[:self.currentline.find("/*")].strip()
			self.lineindex = self.lineindex + 1
			self.handleCurrentLine()
			return True
		else:
			return False

	# def advance(self):
		# self.advance = self.tokensPerLine[self.tokenIndexPerLine]
		# self.tokenIndexPerLine = self.tokenIndexPerLine + 1
		# return self.advance

	def handleCurrentLine(self):
		# symbolList = [".", "(", ")", "[", "]", ";"]
		for symbol in self.symbolList:
			if symbol in self.currentline:
				self.insertSpace(symbol)

	def insertSpace(self, strparam):
		# index = self.currentline.find(strparam)
		if strparam in self.symbolListNotNeedEsc:
			self.currentline = re.sub(r"%s" % strparam, " %s " % strparam, self.currentline)
		else:
			self.currentline = re.sub(r"\%s" % strparam, " %s " % strparam, self.currentline)
			# print(self.currentline)
		# self.currentline = self.currentline[:index] + " " + strparam + " " + self.currentline[index:]

	def tokenType(self):
		if self.advance in self.keywordList:	
			return "KEYWORD"
		elif self.advance in self.symbolList:
			return "SYMBOL"
		elif self.advance.isdigit():
			value = int(self.advance)
			if  value >= 0 and value < 32767:
				return "INT_CONST"
		elif self.advance.startswith("\"") and self.advance.endswith("\""):
			return "STRING_CONST"
		elif not self.advance[0].isdigit():
			return "IDENTIFIER"


	def keyword(self):
		self.outputfile.write("<keyword> " + self.advance + " </keyword>\n")
		return self.advance

	def symbol(self):
		if self.advance == "<":
			self.outputfile.write("<symbol> &lt; </symbol>\n")
		elif self.advance == ">":
			self.outputfile.write("<symbol> &gt; </symbol>\n")
		elif self.advance == "&":
			self.outputfile.write("<symbol> &amp; </symbol>\n")
		else:
			self.outputfile.write("<symbol> " + self.advance + " </symbol>\n")
		return self.advance

	def identifier(self):
		self.outputfile.write("<identifier> " + self.advance + " </identifier>\n")
		return self.advance

	def intVal(self):
		self.outputfile.write("<integerConstant> " + self.advance + " </integerConstant>\n")
		return int(self.advance)

	def stringVal(self):
		self.outputfile.write("<stringConstant> " + self.advance + " </stringConstant>\n")
		return self.advance
		
	def close(self):
		self.f.close()
		self.outputfile.write("</tokens>\n")
		self.outputfile.close()
		