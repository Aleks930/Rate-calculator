# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp1 = (inp.upper())
print(inp1.rstrip('\n'))
