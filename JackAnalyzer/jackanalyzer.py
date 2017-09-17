import getopt
import sys
import os
from jackanalyzer.jacktokenizer import JackTokenizer

def main():
	opt, args = getopt.getopt(sys.argv[1:], "h", ["help"])
	if os.path.isfile(args[0]):
		jacktokenizer = JackTokenizer(args[0])
	while jacktokenizer.hasMoreTokens():
		if jacktokenizer.tokenType() == "KEYWORD":
			jacktokenizer.keyword()
		elif jacktokenizer.tokenType() == "SYMBOL":
			jacktokenizer.symbol()
		elif jacktokenizer.tokenType() == "INT_CONST":
			jacktokenizer.intVal()
		elif jacktokenizer.tokenType() == "STRING_CONST":
			jacktokenizer.stringVal()
		elif jacktokenizer.tokenType() == "IDENTIFIER":
			jacktokenizer.identifier()
	jacktokenizer.close()

if __name__ == "__main__":
	main()