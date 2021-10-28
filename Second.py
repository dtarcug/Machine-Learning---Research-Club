import random
from matplotlib import pyplot as plt

def loss(data, m, b):
    return sum((m*x+b - data[x])**2 for x in range(100))/len(data)


# mm = max(min(int(input("Choose a slope from -100 to 100: ")), 100), -100)
# bb = max(min(int(input("Choose a y-int from -100 to 100: ")), 100), -100)
# NOISE = abs(int(input("Choose the amount of noise: ")))
mm = random.randint(-100, 100)
bb = random.randint(-10000, 10000)
NOISE = 500

data = [random.gauss(mm*x+bb, NOISE) for x in range(100)]

rate_a, rate_b = 10, 10
a, b = 0, 0
losses = []
streak_a, streak_b = True, True
iterations = 0
while rate_a > 0.1 or rate_b > 0.1:
    min_loss = loss(data, a, b)
    losses.append(min_loss)
    best_a, best_b = a, b
    change_a, change_b = 0, 0
    for da, db in [(rate_a, 0), (-rate_a, 0), (0, rate_b), (0, -rate_b),
                   (rate_a, rate_b), (-rate_a, rate_b), (rate_a, -rate_b), (-rate_a, -rate_b)]:
        l = loss(data, a+da, b+db)
        if l < min_loss:
            best_a = a+da
            best_b = b+db
            change_a = da
            change_b = db
            min_loss = l
    if change_a == 0:
        rate_a /= 2
    elif streak_a == (change_a > 0):
        rate_a *= 2
    else:
        streak_a = (change_a > 0)
        rate_a /= 2

    if change_b == 0:
        rate_b /= 2
    elif streak_b == (change_b > 0):
        rate_b *= 2
    else:
        streak_b = (change_b > 0)
        rate_b /= 2

    a, b = best_a, best_b
    iterations += 1
    plt.title(f"Graph Iteration {iterations}")
    plt.scatter(range(100), data)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(range(100), [a * x + b for x in range(100)], color='r', label="Model")
    plt.plot(range(100), [mm * x + bb for x in range(100)], color='g', label="True Function")
    plt.legend()
    plt.show()

final_loss = loss(data, a, b)
losses.append(final_loss)
print("Original Slope:", mm)
print("Original Intercept:", bb)
print("Learnt Slope:", a)
print("Learnt Intercept:", b)
print("Loss:", final_loss)
print("Iterations:", iterations)
plt.title("Graph")
plt.scatter(range(100), data)
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(range(100), [a*x+b for x in range(100)], color='r', label="Model")
plt.plot(range(100), [mm*x+bb for x in range(100)], color='g', label="True Function")
plt.legend()
plt.show()

plt.title("Loss")
plt.plot(range(len(losses)), losses)
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.show()