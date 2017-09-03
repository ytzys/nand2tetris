import sys
import getopt
from assembler.parser import Parser
from assembler.code import Code

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        filename = args[0][:args[0].find(".")]
        cCommandBase = 0xe000 # 1110 0000 0000 0000
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
                    print(p.symbol())
                    outputfile.write('{0:b}'.format(0x8000 | int(p.symbol())).replace("1", "0", 1) + "\n")
                    # outputfile.write('%x' % int(p.symbol()) + "\n")
    except Exception as e:
        print(e)
        raise e
    

if __name__ == "__main__":
    main()