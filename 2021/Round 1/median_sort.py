def median_sort(L):
	secs = [[], [], []]
	a, b = L[0], L[-1]
	for i in L:
		if (i != a) and (i != b):
			print(f'{a} {b} {i}')
			r = int(input())
			if r == a: secs[0].append(i)
			if r == i: secs[1].append(i)
			if r == b: secs[2].append(i)
			
	
	return secs




t, n, q = [int(s) for s in input().split(" ")]
for c in range(t):
	L = list(range(1, n + 1))
	L = median_sort(L)

	print(' '.join([ str(n) for n in L ]))