import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
	return 1 / (1 + np.e**(-x) )

print('Generating questions and players...')
Q = np.random.uniform(low=-3, high=3, size=10000)
S = np.random.uniform(low=-3, high=3, size=1000)

honest, cheater = np.zeros((2, 1000))

print('Calculating...')
for i in range(1000):
	for j in range(10000):
		x, y = np.random.uniform(low=0, high=1, size=2)

		if x < sigmoid(S[i] - Q[j]): honest[i] += 1

		if x >= 0.5: cheater[i] += 1
		else:
			if y < sigmoid(S[i] - Q[j]): cheater[i] += 1

print('Regular player: {:.5f} # {:.5f} %'.format( honest.mean() / 10000, (honest.std() / 10000) / 100 ))
print('Cheater player: {:.5f} # {:.5f} %'.format( cheater.mean() / 10000, (cheater.std() / 10000) / 100 ))

#plt.hist(honest, bins=50)
plt.hist(cheater, bins=20)
plt.show()