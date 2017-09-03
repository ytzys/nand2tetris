import sys
import getopt
import os
from vm.parser import Parser
from vm.codewriter import CodeWriter

def main():
	try:
		opt, args = getopt.getopt(sys.argv[1:], "h", ["help"])
		if os.path.isfile(args[0]):
			print("is file\n")
			parser = Parser(args[0])
			filename = args[0][:args[0].find(".")]
			codeWriter = CodeWriter(filename + ".asm")
			codeWriter.setFileName(filename)
			while parser.hasMoreCommands():
				commandType = parser.commandType()
				if commandType  == "C_ARITHMETIC":
					print(parser.advance, parser.commandType(), "arg1:", parser.arg1(commandType))
					codeWriter.writeArithmetic(parser.advance)
				elif commandType == "C_PUSH" or commandType == "C_POP":
					print(parser.advance, parser.commandType(), "arg1:", parser.arg1(commandType), 
						"arg2:", parser.arg2(commandType))
					codeWriter.writePushPop(commandType, parser.arg1(commandType), parser.arg2(commandType))
				elif commandType == "C_GOTO":
					codeWriter.writeGoto(parser.arg1(commandType))
				elif commandType == "C_IF":
					codeWriter.writeIf(parser.arg1(commandType))
				elif commandType == "C_LABEL":
					codeWriter.writeLabel(parser.arg1(commandType))
				elif commandType == "C_CALL":
					codeWriter.writeCall(parser.arg1(commandType), int(parser.arg2(commandType)))
				elif commandType == "C_RETURN":
					codeWriter.writeReturn()
				elif commandType == "C_FUNCTION":
					codeWriter.writeFunction(parser.arg1(commandType), int(parser.arg2(commandType)))
					
			parser.close()
			codeWriter.close()
		else:
			print("is dir\n")
			# print(os.path.dirname(args[0]))
			print(args[0] + "\n")
			outputfilename = args[0].split("/")[len(args[0].split("/")) - 1]
			outputfiledir = os.path.abspath(args[0])
			print("outputfiledir:" + outputfiledir + "\n")
			outputfile = outputfilename + ".asm"
			print(outputfile + "\n")
			codeWriter = CodeWriter(outputfiledir + "/" + outputfile)
			files = [f for f in os.listdir(args[0])]
			print(files)
			codeWriter.writeInit() # 初始化操作
			for f in files:
				if ".vm" in f:
					print(f)
					parser = Parser(outputfiledir + "/" + f)
					codeWriter.setFileName(f)
					while parser.hasMoreCommands():
						commandType = parser.commandType()
						if commandType  == "C_ARITHMETIC":
							print(parser.advance, parser.commandType(), "arg1:", parser.arg1(commandType))
							codeWriter.writeArithmetic(parser.advance)
						elif commandType == "C_PUSH" or commandType == "C_POP":
							print(parser.advance, parser.commandType(), "arg1:", parser.arg1(commandType), 
								"arg2:", parser.arg2(commandType))
							codeWriter.writePushPop(commandType, parser.arg1(commandType), parser.arg2(commandType))
						elif commandType == "C_GOTO":
							codeWriter.writeGoto(parser.arg1(commandType))
						elif commandType == "C_IF":
							codeWriter.writeIf(parser.arg1(commandType))
						elif commandType == "C_LABEL":
							codeWriter.writeLabel(parser.arg1(commandType))
						elif commandType == "C_CALL":
							codeWriter.writeCall(parser.arg1(commandType), int(parser.arg2(commandType)))
						elif commandType == "C_RETURN":
							codeWriter.writeReturn()
						elif commandType == "C_FUNCTION":
							codeWriter.writeFunction(parser.arg1(commandType), int(parser.arg2(commandType)))
					parser.close()
			codeWriter.close()		
	except Exception as e:
		print(e)
		raise e

if __name__ == "__main__":
	main()