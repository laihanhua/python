
stack = []
def pushit():
	data = input("输入加入的字符串:")
	stack.append(data.strip())
def popit():
	if(len(stack)>0):
		print(stack.pop()+" 出栈")
	else:
		print("该栈已经为空")
def viewstack():
	print(stack)
cmd = {"u":pushit,"o":popit,"v":viewstack}

def showmenu():
	pr = """
		p(U)sh
		p(O)p
		(V)iew
		(Q)uit
		
		enter choice:
	"""
	while True:
		while True:
			try:
				choice = input(pr).lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			print ("\n your pick :[%s]" % choice)
			
			if(choice not in 'uovq'):
				print("输入无效")
			else:
				break
		if choice == 'q':
			break
		cmd[choice]()
			
if __name__=="__main__":
	showmenu()
			