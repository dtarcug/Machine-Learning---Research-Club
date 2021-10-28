import random
from matplotlib import pyplot as plt

#y=mx+b
def loss(data, m, b):
    return sum((m*x+b - data[x])**2 for x in range(100))/len(data)

mm = max(min(int(input("Choose a slope from -100 to 100: ")), 100), -100)
bb = max(min(int(input("Choose a y-int from -100 to 100: ")), 100), -100)
NOISE = abs(int(input("Choose the amount of noise: ")))

data = [random.gauss(mm*x+bb, NOISE) for x in range(100)]


best_m = 0
best_b = 0
min_loss = float('inf')

for _ in range(10000):
    m = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    l = loss(data, m, b)
    if l < min_loss:
        min_loss = l
        best_m = m
        best_b = b
print("Slope Learnt:", best_m)
print("Y-int Learnt:", best_b)
plt.scatter(range(100), data)
plt.plot(range(100), [best_m*x+best_b for x in range(100)], color='r', label="Model")
plt.plot(range(100), [mm*x+bb for x in range(100)], color='g', label="True Function")
plt.legend()
plt.show()