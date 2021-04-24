t, p = int(input()), int(input())

for c in range(t):
	players = [ [0] * 10000 ] * 100
	hardness = [0] * 10000
	ranking = [0] * 100

	for i in range(100):
		anwsers = input()
		for j in range(10000):
			if anwsers[j] == '1':
				players[i][j] = 1
			else:
				hardness[j] += 1

	for i in range(100):
		for j in range(10000):
			ranking[i] += players[i][j] * hardness[j] / 100
	
	print(f'Case #{c+1}: {ranking.index(max(ranking))+1}')
