import getopt
import sys
import os
from jackanalyzer.jacktokenizer import JackTokenizer

def main():
	opt, args = getopt.getopt(sys.argv[1:], "h", ["help"])
	if os.path.isfile(args[0]):
		jacktokenizer = JackTokenizer(args[0])
	while jacktokenizer.hasMoreTokens():
		# Involve tokenType() only once, or string constants will not work, i.e. :
		#
		# if jacktokenizer.tokenType() == "KEYWORD":
		# 	jacktokenizer.keyword()
		# elif jacktokenizer.tokenType() == "SYMBOL":
		# 	jacktokenizer.symbol()
		# elif jacktokenizer.tokenType() == "INT_CONST":
		# 	jacktokenizer.intVal()
		# elif jacktokenizer.tokenType() == "STRING_CONST":
		# 	print("is string constant")
		# 	jacktokenizer.stringVal()
		# elif jacktokenizer.tokenType() == "IDENTIFIER":
		# 	jacktokenizer.identifier()
		#
		# This will cause string constant to be identifier.

		tokenType = jacktokenizer.tokenType()
		if tokenType == "KEYWORD":
			jacktokenizer.keyword()
		elif tokenType == "SYMBOL":
			jacktokenizer.symbol()
		elif tokenType == "INT_CONST":
			jacktokenizer.intVal()
		elif tokenType == "STRING_CONST":
			print("is string constant")
			jacktokenizer.stringVal()
		elif tokenType == "IDENTIFIER":
			jacktokenizer.identifier()
	jacktokenizer.close()

if __name__ == "__main__":
	main()