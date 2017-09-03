import sys
import getopt
from assembler.parser import Parser
from assembler.code import Code
from assembler.symboltable import SymbolTable

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        filename = args[0][:args[0].find(".")]
        cCommandBase = 0xe000 # 1110 0000 0000 0000

        table = SymbolTable()
        p = Parser(args[0])
        instructionAdress = 0
        ramIndex = 16
        while p.hasMoreCommands():
            if p.commandType() == "L_COMMAND":
                table.addEntry(p.symbol(), instructionAdress)
            else:
                instructionAdress = instructionAdress + 1
        p.close()
        print(table.getTable())

        with open(filename + ".hack", "w") as outputfile:
            # outputfile.write("//Hello world!!")
            p = Parser(args[0])
            code = Code()
            while p.hasMoreCommands():
                # print(p.commandType(), ":", p.advance)
                if p.commandType() == "C_COMMAND":
                    print('%s %s %s' % (p.dest(), p.comp(), p.jump()))
                    instruction = cCommandBase | code.dest(p.dest()) | code.comp(p.comp()) | code.jump(p.jump())
                    outputfile.write('{0:b}'.format(instruction) + "\n")
                elif p.commandType() == "A_COMMAND":
                    if p.symbol().isdigit():
                        outputfile.write('{0:b}'.format(0x8000 | int(p.symbol())).replace("1", "0", 1) + "\n")
                    elif table.contains(p.symbol()):
                        outputfile.write('{0:b}'
                            .format(0x8000 | table.getAddress(p.symbol())).replace("1", "0", 1) + "\n")
                    else:
                        table.addEntry(p.symbol(), ramIndex)
                        # print(table.getTable())
                        outputfile.write('{0:b}'.format(0x8000 | ramIndex).replace("1", "0", 1) + "\n")
                        ramIndex = ramIndex + 1
            p.close()
    except Exception as e:
        print(e)
        raise e
    

if __name__ == "__main__":
    main()