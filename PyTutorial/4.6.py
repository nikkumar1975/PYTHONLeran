def fib(n):
	"""print a fib series uptil n"""
	n=n*2
	a,b=0,1
	while a<n:
		print(a,end=' ')
		a,b=b,a+b
	print()

def main():
	n=int(input("enter a number "))
	print("n in main beforen call to fib:",n)
	print()
	fib(n)	
	print("n in main after call to fib:",n)
	print()

main()