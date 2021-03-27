def Reversort(L):
	cost = 0
	for i in range(len(L) - 1):
		j = L.index(min(L[i:]))
		L[i:j+1] = L[i:j+1][::-1]
		cost += j - (i - 1)
	return cost

def MaxCost(n):
	return (n**2 + n - 2) / 2

t = int(input())
for i in range(t):
	n, c = [int(s) for s in input().split(" ")]

	if (c > MaxCost(n)) or (c < (n - 1)):
		print(f'Case #{i+1}: IMPOSSIBLE')
	else:
		L = list(range(1, n+1))
		c -= (n - 1)

		index = 0
		band = n
		while c > 0:
			d = min(c + 1, band)
			L[index//2:index//2+d] = L[index//2:index//2+d][::-1]
			c -= (d - 1)
			index += 1
			band -= 1

		print('Case #{}: {}'.format(i+1, ' '.join([ str(n) for n in L ])))	