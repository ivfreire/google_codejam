
def Reversort(L):
	cost = 0
	for i in range(len(L) - 1):
		j = L.index(min(L[i:]))
		L[i:j+1] = L[i:j+1][::-1]
		cost += j - (i - 1)
	return cost

t = int(input())
for i in range(t):
	length = int(input())
	L = [int(s) for s in input().split(" ")]
	cost = Reversort(L)
	print(f'Case #{i+1}: {cost}')