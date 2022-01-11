import sklearn as sk
import itertools as it
import math, numpy  as np
from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split
from scipy import stats
np.random.seed(0)



''' This is a way to find the k nearest neighbor, broken down to be hopefully easier to understand.
Please ignore my bad code. 
'''


data = load_iris()
x, y = data.data, data.target
#inputs (like coordinates), target (like shape)

train_x, test_x, train_y, test_y = train_test_split(x, y)

# 2D array train_x: coordinates,
# 2D array test_x: ?,
# array train_y: type,
# array test_y: answer key


# 1. Use test_x and train_x to find the KNN
# 2. Look at the classes of these points (train y)
# 3. Look at the mode of the classes, and set that as the guess of the class
# 4. Use test_y to check your answer
k = 3


def distance(coord1, coord2):
    # ^ this function finds a distance between two coordinates.
    #it's just the distance formula.

    total = 0 #distance between pt 1 & pt 2

    for i, j in zip(coord1, coord2):
        total += (i - j) ** 2 #(i-j)^2

    total = math.sqrt(total)

    return total

#MAKE A LIST OF THE DISTANCES:
#Make a list of the distances between test_x[0] (the first coordinate in test_x) and all the coordinates in train_x:
distances = []
for i in train_x :
    distances.append(distance(i, test_x[0]))

#K NEAREST NEIGHBORS:
#find the coordinates of the nearest neighbors
sortedDistances = sorted(distances) #<-- stores the distances, sorted from min to max
print(sortedDistances[:k]) #<-- all of the smallest distances, up until k (this is called comprehension)
#^ k smallest distances

#closest = train_x[distances.index(sortedDistances[0])]#<--coordinates that are closest


# K NEAREST NEIGHBOR CLASSES:
# find the classes of the nearest neighbors
nearestClasses = []
for i in range(k):
    nearestClasses.append(train_y[distances.index(sortedDistances[i])])
    #^train_y[the index of the coordinates that are the smallest distance away]
    #(index means its number in the list

#FIND THE MODE CLASS:
m=stats.mode(nearestClasses)
print(m.mode)
