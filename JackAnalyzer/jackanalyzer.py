import getopt

def main():
	opt, args = getopt.getopt(sys.argv[1:], "h", ["help"])
	if os.path.isfile(args[0]):
		jacktokenizer = JackTokenizer(args[0])

if __name__ == "__main__":
	main()