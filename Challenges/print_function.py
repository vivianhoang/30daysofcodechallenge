# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

print "%s" % ("".join([repr(i+1) for i in range(n)]))
