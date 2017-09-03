class SymbolTable(object):
	"""docstring for symbolTable"""
	def __init__(self):
		self.table = {}
		self.table["R0"] = 0x0000;
		self.table["R1"] = 0x0001;
		self.table["R2"] = 0x0002;
		self.table["R3"] = 0x0003;
		self.table["R4"] = 0x0004;
		self.table["R5"] = 0x0005;
		self.table["R6"] = 0x0006;
		self.table["R7"] = 0x0007;
		self.table["R8"] = 0x0008;
		self.table["R9"] = 0x0009;
		self.table["R10"] = 0x000a;
		self.table["R11"] = 0x000b;
		self.table["R12"] = 0x000c;
		self.table["R13"] = 0x000d;
		self.table["R14"] = 0x000e;
		self.table["R15"] = 0x000f;
		self.table["SCREEN"] = 0x4000;
		self.table["KEY"] = 0x6000;
		self.table["SP"] = 0x0000;
		self.table["LCL"] = 0x0001;
		self.table["ARG"] = 0x0002;
		self.table["THIS"] = 0x0003;
		self.table["THAT"] = 0x0004;

	def addEntry(self, symbol, address):
		self.table[symbol] = address;

	def contains(self, symbol):
		return symbol in self.table

	def getAddress(self, symbol):
		return self.table[symbol]

	def getTable(self):
		return self.table