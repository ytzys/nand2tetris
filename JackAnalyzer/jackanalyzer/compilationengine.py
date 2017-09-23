class CompilationEngine(objcect):

	def __init__(self, filename):
		jacktokenizer = JackTokenizer(filename)
		self.outputFileName = filename[:filename.find(".")] + ".xml"
		self.outputfile = open(self.outputFileName, "w")

	def write(self, tokenType):
		if tokenType == "KEYWORD":
			self.outputfile.write("<keyword> " + jacktokenizer.advance + " </keyword>\n")
		elif tokenType == "SYMBOL":
			if self.advance == "<":
			self.outputfile.write("<symbol> &lt; </symbol>\n")
			elif self.advance == ">":
				self.outputfile.write("<symbol> &gt; </symbol>\n")
			elif self.advance == "&":
				self.outputfile.write("<symbol> &amp; </symbol>\n")
			else:
				self.outputfile.write("<symbol> " + jacktokenizer.advance + " </symbol>\n")
		elif tokenType == "INT_CONST":
			self.outputfile.write("<integerConstant> " + jacktokenizer.advance + " </integerConstant>\n")
		elif tokenType == "STRING_CONST":
			self.outputfile.write("<stringConstant> " + jacktokenizer.advance + " </stringConstant>\n")
		elif tokenType == "IDENTIFIER":
			self.outputfile.write("<identifier> " + jacktokenizer.advance + " </identifier>\n")

	def compileClass(self):
		self.outputfile.write("<class>\n")
		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # class
		
		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # class name

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # {

		jacktokenizer.hasMoreTokens()
		if jacktokenizer.advance == "field":
			compileClassVarDec()
		elif jacktokenizer.advance == "function" \
			or jacktokenizer.advance == "method" \
			or jacktokenizer.advance == "consturctor":
			compileSubrutine()

		self.outputfile.write("</class>\n")

	def compileClassVarDec(self):
		self.outputfile.write("<classVarDec>\n")
		write(jacktokenizer.tokenType()) # field

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # field Type

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # field name

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # ;

		self.outputfile.write("</classVarDec>\n") # over

		jacktokenizer.hasMoreTokens()
		if jacktokenizer.advance == "field":
			compileClassVarDec()
		elif jacktokenizer.advance == "function" \
			or jacktokenizer.advance == "method" \
			or jacktokenizer.advance == "consturctor":
			compileSubrutine()

	def compileSubrutine(self):
		self.outputfile.write("<subroutineDec>\n")
		write(jacktokenizer.tokenType()) # function | method | constructor

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # return type

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # name

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # (

		jacktokenizer.hasMoreTokens()
		if not jacktokenizer.advance == ")"
			compileParameterList()
		write(jacktokenizer.tokenType()) # )

		self.outputfile.write("<subroutineBody>\n")

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # {

		jacktokenizer.hasMoreTokens()
		if jacktokenizer.advance == "var":
			compileVarDec()
		elif jacktokenizer.advance == "let" \
			or jacktokenizer.advance == "do" \
			or jacktokenizer.advance == "while" \
			or jacktokenizer.advance == "if" \
			or jacktokenizer.advance == "return":
			compileStatements()

		# 	compileLet()
		# elif jacktokenizer.advance == "do":
		# 	compileDo()
		# elif jacktokenizer.advance == "return":
		# 	compileReturn()

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # }

		self.outputfile.write("</subroutineBody>\n")

	def compileParameterList(self):
		self.outputfile.write("<parameterList>\n")
		while jacktokenizer.hasMoreTokens() and not jacktokenizer.advance == ")":
			write(jacktokenizer.tokenType())
		self.outputfile.write("</parameterList>\n")

	def compileVarDec(self):
		self.outputfile.write("<varDec>\n")
		while jacktokenizer.hasMoreTokens() and not jacktokenizer.advance == ";"
			write(jacktokenizer.tokenType())
		write(jacktokenizer.tokenType())
		self.outputfile.write("</varDec>\n")

		jacktokenizer.hasMoreTokens()
		if jacktokenizer.advance == "var":
			compileVarDec()
		elif jacktokenizer.advance == "let" \
			or jacktokenizer.advance == "do" \
			or jacktokenizer.advance == "while" \
			or jacktokenizer.advance == "if" \
			or jacktokenizer.advance == "return":
			compileStatements()

	def compileStatements(self):
		self.outputfile.write("<statements>\n")

		jacktokenizer.hasMoreTokens()
		compileStatement()

		self.outputfile.write("</statements>\n")

	def compileStatement(self):
		if jacktokenizer.advance == "do":
			compileDo()
		elif jacktokenizer.advance == "let":
			compileLet()
		elif jacktokenizer.advance == "while":
			compileWhile()
		elif jacktokenizer.advance == "return":
			compileReturn()
		elif jacktokenizer.advance == "if":
			compileIf()

	def compileDo(self):
		self.outputfile.write("<doStatement>\n")
		while jacktokenizer.hasMoreTokens() and not jacktokenizer.advance == "(":
			write(jacktokenizer.tokenType())
		write(jacktokenizer.tokenType()) # (

		jacktokenizer.hasMoreTokens()
		if not jacktokenizer.advance == ")"
			compileExpression()
		write(jacktokenizer.tokenType()) # )

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.tokenType()) # ;

		jacktokenizer.hasMoreTokens()
		if jacktokenizer.advance == "var":
			compileVarDec()
		elif jacktokenizer.advance == "let" \
			or jacktokenizer.advance == "do" \
			or jacktokenizer.advance == "while" \
			or jacktokenizer.advance == "if" \
			or jacktokenizer.advance == "return":
			compileStatement()

		self.outputfile.write("</doStatement>\n")

	def compileLet(self):
		self.outputfile.write("<letStatement>\n")
		while jacktokenizer.hasMoreTokens() and not jacktokenizer.advance == "=":
			write(jacktokenizer.tokenType())
		write(jacktokenizer.tokenType()) # =

		jacktokenizer.hasMoreTokens()
		compileExpression()
		self.outputfile.write("</letStatement>\n")

	def compileExpression(self):
		pass

	def compileReturn(self):
		self.outputfile.write("<returnStatement>\n")
		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.advance) # return

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.advance) # ;
		self.outputfile.write("</returnStatement>\n")
	
	def compileWhile(self):
		self.outputfile.write("<whileStatement>\n")
		while jacktokenizer.hasMoreTokens() and not jacktokenizer.advance == "(":
			write(jacktokenizer.tokenType())
		write(jacktokenizer.advance) # (

		jacktokenizer.hasMoreTokens()
		if not jacktokenizer.advance == ")":
			compileExpression()
		write(jacktokenizer.advance) # )

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.advance) # {

		jacktokenizer.hasMoreTokens()
		if not jacktokenizer.advance == "}":
			compileStatements()
		write(jacktokenizer.advance) # }

		self.outputfile.write("</whileStatement>\n")

	def compileIf(self):
		self.outputfile.write("<ifStatement>\n")

		while jacktokenizer.hasMoreTokens() and not jacktokenizer.advance == "(":
			write(jacktokenizer.tokenType())
		write(jacktokenizer.advance) # (

		jacktokenizer.hasMoreTokens()
		if not jacktokenizer.advance == ")":
			compileExpression()
		write(jacktokenizer.advance) # )

		jacktokenizer.hasMoreTokens()
		write(jacktokenizer.advance) # {

		jacktokenizer.hasMoreTokens()
		if not jacktokenizer.advance == "}":
			compileStatements()
		write(jacktokenizer.advance) # }

		self.outputfile.write("</ifStatement>\n")

	def compileTerm(self):
		pass

	def compileExpressionList(self):
		# self.outputfile.write("<expressionList>\n")

		# self.outputfile.write("</expressionList>\n")
		pass
			
