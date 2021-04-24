
def clear_string(S):
	_S = S[0]
	last = S[0]
	for char in S:
		if char != last:
			_S += char
			last = char
	return _S

t = int(input())
for i in range(t):
	x, y, S = str(input()).split(' ')
	x, y = int(x), int(y)
	S = clear_string(S)

	S = S.replace('?', '')
	cost = 0

	for j in range(len(S) - 1):
		if S[j:j+2] == 'CJ': cost += x
		if S[j:j+2] == 'JC': cost += y

	print(f'Case #{i+1}: {cost}')
