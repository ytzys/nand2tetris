class Code(object):

	def dest(self, symbol):
		if symbol == "A":
			return 0x0020 # 0000 0000 0010 0000
		elif symbol == "D":
			return 0x0010 # 0000 0000 0001 0000
		elif symbol == "M":
			return 0x0008 # 0000 0000 0000 1000
		elif symbol == "AD":
			return 0x0030 # 0000 0000 0011 0000
		elif symbol == "AM":
			return 0x0028 # 0000 0000 0010 1000
		elif symbol == "MD":
			return 0x0018 # 0000 0000 0001 1000
		elif symbol == "AMD":
			return 0x0038 #0000 0000 0011 1000
		else: # null
			return 0

	def comp(self, symbol):
		if symbol == "1":
			return 0x0fc0 # 0000 1111 1100 0000
		elif symbol == "-1":
			return 0x0e80 # 0000 1110 1000 0000
		elif symbol == "D":
			return 0x0300 # 0000 0011 0000 0000
		elif symbol == "A":
			return 0x0c00 # 0000 1100 0000 0000
		elif symbol == "M":
			return 0x1c00 # 0001 1100 0000 0000
		elif symbol == "!D":
			return 0x0340 # 0000 0011 0100 0000
		elif symbol == "!A":
			return 0x0c40 # 0000 1100 0100 0000
		elif symbol == "!M":
			return 0x1c40 # 0001 1100 0100 0000
		elif symbol == "-D":
			return 0x03c0 #0000 0011 1100 0000
		elif symbol == "-A":
			return 0x0cc0 #0000 1100 1100 0000
		elif symbol == "-M":
			return 0x1cc0 #0001 1100 1100 0000
		elif symbol == "D+1":
			return 0x07c0 # 0000 0111 1100 0000
		elif symbol == "A+1":
			return 0x0dc0 # 0000 1101 1100 0000
		elif symbol == "M+1":
			return 0x1dc0 # 0001 1101 1100 0000
		elif symbol == "D-1":
			return 0x0380 # 0000 0011 1000 0000
		elif symbol == "A-1":
			return 0x0c80 # 0000 1100 1000 0000
		elif symbol == "M-1":
			return 0x1c80 # 0001 1100 1000 0000
		elif symbol == "D+A":
			return 0x0080 # 0000 0000 1000 0000
		elif symbol == "D+M":
			return 0x1080 # 0001 0000 1000 0000
		elif symbol == "D-A":
			return 0x04c0 # 0000 0100 1100 0000
		elif symbol == "D-M":
			return 0x14c0 # 0001 0100 1100 0000
		elif symbol == "A-D":
			return 0x01c0 # 0000 0001 1100 0000
		elif symbol == "M-D":
			return 0x11c0 # 0001 0001 1100 0000
		elif symbol == "D&A":
			return 0x0000 # 0000 0000 0000 0000
		elif symbol == "D&M":
			return 0x1000 # 0001 0000 0000 0000
		elif symbol == "D|A":
			return 0x0540 # 0000 0101 0100 0000
		elif symbol == "D|M":
			return 0x1540 # 0001 0101 0100 0000
		else:  # 0
			return 0x0a80 # 0000 1010 1000 0000

	def jump(self, symbol):
		if symbol == "JMP":
			return 0x0007 # 0000 0000 0000 0111
		elif symbol == "JLT":
			return 0x0004 # 0000 0000 0000 0100
		elif symbol == "JEQ":
			return 0x0002 # 0000 0000 0000 0010
		elif symbol == "JGT":
			return 0x0001 # 0000 0000 0000 0001
		elif symbol == "JLE":
			return 0x0006 # 0000 0000 0000 0110
		elif symbol == "JNE":
			return 0x0005 # 0000 0000 0000 0101
		elif symbol == "JGE":
			return 0x0003 # 0000 0000 0000 0011
		else: # null
			return 0x0000