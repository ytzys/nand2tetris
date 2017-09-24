from jackanalyzer.jacktokenizer import JackTokenizer
class CompilationEngine(object):

	def __init__(self, filename):
		self.jacktokenizer = JackTokenizer(filename)
		self.outputFileName = filename[:filename.find(".")] + ".xml"
		self.outputfile = open(self.outputFileName, "w")

	def write(self, tokenType):
		if tokenType == "KEYWORD":
			self.outputfile.write("<keyword> " + self.jacktokenizer.advance + " </keyword>\n")
		elif tokenType == "SYMBOL":
			if self.jacktokenizer.advance == "<":
				self.outputfile.write("<symbol> &lt; </symbol>\n")
			elif self.jacktokenizer.advance == ">":
				self.outputfile.write("<symbol> &gt; </symbol>\n")
			elif self.jacktokenizer.advance == "&":
				self.outputfile.write("<symbol> &amp; </symbol>\n")
			else:
				self.outputfile.write("<symbol> " + self.jacktokenizer.advance + " </symbol>\n")
		elif tokenType == "INT_CONST":
			self.outputfile.write("<integerConstant> " + self.jacktokenizer.advance + " </integerConstant>\n")
		elif tokenType == "STRING_CONST":
			self.outputfile.write("<stringConstant> " + self.jacktokenizer.advance + " </stringConstant>\n")
		elif tokenType == "IDENTIFIER":
			self.outputfile.write("<identifier> " + self.jacktokenizer.advance + " </identifier>\n")

	def compileClass(self):
		self.outputfile.write("<class>\n")
		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # class
		
		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # class name

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # {

		self.jacktokenizer.hasMoreTokens()
		if self.jacktokenizer.advance == "field" \
			or self.jacktokenizer.advance == "static":
			self.compileClassVarDec()
		elif self.jacktokenizer.advance == "function" \
			or self.jacktokenizer.advance == "method" \
			or self.jacktokenizer.advance == "consturctor":
			self.compileSubrutine()

		# self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # }
		self.outputfile.write("</class>\n")

	def compileClassVarDec(self):
		self.outputfile.write("<classVarDec>\n")
		self.write(self.jacktokenizer.tokenType()) # field

		# self.jacktokenizer.hasMoreTokens()
		# self.write(self.jacktokenizer.tokenType()) # field Type

		# self.jacktokenizer.hasMoreTokens()
		# self.write(self.jacktokenizer.tokenType()) # field name

		# self.jacktokenizer.hasMoreTokens()
		# self.write(self.jacktokenizer.tokenType()) # ;
		while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == ";":
			self.write(self.jacktokenizer.tokenType())
		self.write(self.jacktokenizer.tokenType())

		self.outputfile.write("</classVarDec>\n") # over

		self.jacktokenizer.hasMoreTokens()
		if self.jacktokenizer.advance == "field" \
			or self.jacktokenizer.advance == "static":
			self.compileClassVarDec()
		elif self.jacktokenizer.advance == "function" \
			or self.jacktokenizer.advance == "method" \
			or self.jacktokenizer.advance == "constructor":
			self.compileSubrutine()

	def compileSubrutine(self):
		self.outputfile.write("<subroutineDec>\n")
		self.write(self.jacktokenizer.tokenType()) # function | method | constructor

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # return type

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # name

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # (

		self.jacktokenizer.hasMoreTokens()
		self.compileParameterList()
		self.write(self.jacktokenizer.tokenType()) # )

		self.outputfile.write("<subroutineBody>\n")

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # {

		self.jacktokenizer.hasMoreTokens()
		if self.jacktokenizer.advance == "var":
			self.compileVarDec()
		elif self.jacktokenizer.advance == "let" \
			or self.jacktokenizer.advance == "do" \
			or self.jacktokenizer.advance == "while" \
			or self.jacktokenizer.advance == "if" \
			or self.jacktokenizer.advance == "return":
			self.compileStatements()

		# 	compileLet()
		# elif self.jacktokenizer.advance == "do":
		# 	compileDo()
		# elif self.jacktokenizer.advance == "return":
		# 	compileReturn()

		# self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # }

		self.outputfile.write("</subroutineBody>\n")
		self.outputfile.write("</subroutineDec>\n")

		self.jacktokenizer.hasMoreTokens()
		if self.jacktokenizer.advance == "function" \
			or self.jacktokenizer.advance == "method":
			self.compileSubrutine()

	def compileParameterList(self):
		self.outputfile.write("<parameterList>\n")
		if not self.jacktokenizer.advance == ")":
			self.write(self.jacktokenizer.tokenType()) # first param type
			while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == ")":
				self.write(self.jacktokenizer.tokenType())
		self.outputfile.write("</parameterList>\n")

	def compileVarDec(self):
		self.outputfile.write("<varDec>\n")
		self.write(self.jacktokenizer.tokenType()) # var
		while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == ";":
			self.write(self.jacktokenizer.tokenType())
		self.write(self.jacktokenizer.tokenType())
		self.outputfile.write("</varDec>\n")

		self.jacktokenizer.hasMoreTokens()
		if self.jacktokenizer.advance == "var":
			self.compileVarDec()
		elif self.jacktokenizer.advance == "let" \
			or self.jacktokenizer.advance == "do" \
			or self.jacktokenizer.advance == "while" \
			or self.jacktokenizer.advance == "if" \
			or self.jacktokenizer.advance == "return":
			self.compileStatements()

	def compileStatements(self):
		self.outputfile.write("<statements>\n")

		# self.jacktokenizer.hasMoreTokens()
		self.compileStatement()

		self.outputfile.write("</statements>\n")

	def compileStatement(self):
		if self.jacktokenizer.advance == "do":
			self.compileDo()
		elif self.jacktokenizer.advance == "let":
			self.compileLet()
		elif self.jacktokenizer.advance == "while":
			self.compileWhile()
		elif self.jacktokenizer.advance == "return":
			self.compileReturn()
		elif self.jacktokenizer.advance == "if":
			self.compileIf()

	def compileDo(self):
		self.outputfile.write("<doStatement>\n")
		self.write(self.jacktokenizer.tokenType()) # do
		while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == "(":
			self.write(self.jacktokenizer.tokenType())
		self.write(self.jacktokenizer.tokenType()) # (

		# self.jacktokenizer.hasMoreTokens()
		# if not self.jacktokenizer.advance == ")"
		self.compileExpressionList()
		self.write(self.jacktokenizer.tokenType()) # )

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # ;

		self.outputfile.write("</doStatement>\n")

		self.jacktokenizer.hasMoreTokens()
		if self.jacktokenizer.advance == "var":
			self.compileVarDec()
		elif self.jacktokenizer.advance == "let" \
			or self.jacktokenizer.advance == "do" \
			or self.jacktokenizer.advance == "while" \
			or self.jacktokenizer.advance == "if" \
			or self.jacktokenizer.advance == "return":
			self.compileStatement()

		# self.jacktokenizer.hasMoreTokens()
		# compileStatement()

	def compileLet(self):
		self.outputfile.write("<letStatement>\n")
		self.write(self.jacktokenizer.tokenType()) # do
		while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == "=":
			self.write(self.jacktokenizer.tokenType())
		self.write(self.jacktokenizer.tokenType()) # =

		self.jacktokenizer.hasMoreTokens()
		self.compileExpression()

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # ;
		self.outputfile.write("</letStatement>\n")

		self.jacktokenizer.hasMoreTokens()
		self.compileStatement()

	def compileReturn(self):
		self.outputfile.write("<returnStatement>\n")
		self.write(self.jacktokenizer.tokenType()) # return

		self.jacktokenizer.hasMoreTokens()
		if not self.jacktokenizer.advance == ";":
			self.compileExpression()
			self.jacktokenizer.hasMoreTokens()
			self.write(self.jacktokenizer.tokenType()) # ;
		else:
			self.write(self.jacktokenizer.tokenType()) # ;
		self.outputfile.write("</returnStatement>\n")
		self.jacktokenizer.hasMoreTokens()
	
	def compileWhile(self):
		self.outputfile.write("<whileStatement>\n")
		self.write(self.jacktokenizer.tokenType()) # while
		while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == "(":
			self.write(self.jacktokenizer.tokenType())
		self.write(self.jacktokenizer.tokenType()) # (

		self.jacktokenizer.hasMoreTokens()
		if not self.jacktokenizer.advance == ")": # todo unnessisary
			self.compileExpression()
			self.jacktokenizer.hasMoreTokens()
			self.write(self.jacktokenizer.tokenType()) # )
		else:
			self.write(self.jacktokenizer.tokenType()) # )

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # {

		self.jacktokenizer.hasMoreTokens()
		if not self.jacktokenizer.advance == "}":
			self.compileStatements()
		self.write(self.jacktokenizer.tokenType()) # }

		self.outputfile.write("</whileStatement>\n")

		self.jacktokenizer.hasMoreTokens()
		self.compileStatement()

	def compileIf(self):
		self.outputfile.write("<ifStatement>\n")
		self.write(self.jacktokenizer.tokenType()) # if
		# while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == "(":
		# 	self.write(self.jacktokenizer.tokenType())
		self.jacktokenizer.hasMoreTokens() 
		self.write(self.jacktokenizer.tokenType()) # (

		self.jacktokenizer.hasMoreTokens()
		if not self.jacktokenizer.advance == ")":
			self.compileExpression()
			self.jacktokenizer.hasMoreTokens()
			self.write(self.jacktokenizer.tokenType()) # )
		else:
			self.write(self.jacktokenizer.tokenType()) # )

		self.jacktokenizer.hasMoreTokens()
		self.write(self.jacktokenizer.tokenType()) # {

		self.jacktokenizer.hasMoreTokens()
		if not self.jacktokenizer.advance == "}":
			self.compileStatements()
		self.write(self.jacktokenizer.tokenType()) # }

		self.outputfile.write("</ifStatement>\n")

		self.jacktokenizer.hasMoreTokens()
		self.compileStatement()

	def compileExpression(self):
		self.outputfile.write("<expression>\n")
		self.compileTerm()
		self.outputfile.write("</expression>\n")

	def compileTerm(self):
		tokenType = self.jacktokenizer.tokenType()
		# if tokenType == "STRING_CONST" \
		# 	or tokenType == "INT_CONST":
		# 	self.outputfile.write("<Term>\n")
		# 	self.write(tokenType)
		# 	self.outputfile.write("</Term>\n")
		# else:
		# 	pass
		self.outputfile.write("<term>\n")
		self.write(tokenType)
		self.outputfile.write("</term>\n")

	def compileExpressionList(self):
		self.outputfile.write("<expressionList>\n")
		while self.jacktokenizer.hasMoreTokens() and not self.jacktokenizer.advance == ")":
			if not self.jacktokenizer.advance == ",":
				self.compileExpression()
			else:
				self.write(self.jacktokenizer.tokenType()) # ,
		self.outputfile.write("</expressionList>\n")
		
			
