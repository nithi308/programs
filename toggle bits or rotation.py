def toggle(n):
	temp = 1
	while (temp <= n):
		n = n ^ temp # ^ represents xor 
		temp = temp << 1 
	return n
n = int(input())
n=toggle(n)
print(n)
'''10=1010 
will be toggle in to 0101 (i.e) 5
