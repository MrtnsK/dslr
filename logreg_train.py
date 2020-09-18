import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def StandardScaler(X):
    mean = np.mean(X, axis=0)
    scale = np.std(X - mean, axis=0)
    return (X - mean) / scale

def predict(X, theta):
	z = np.dot(X, theta)
	sig = 1 / (1 + np.exp(-z))
	return sig
# xavier initialization
# https://towardsdatascience.com/weight-initialization-techniques-in-neural-networks-26c649eb3b78
def xavier(X):
	return np.random.randn(X.shape[1]) * np.sqrt(1 / X.shape[1])

def	cost(X, y, theta):
	return ((-1 / X.shape[0]) * np.sum(y * np.log(predict(X, theta)) + (1 - y) * np.log(1 - predict(X, theta))))

# learning rate decay
# https://towardsdatascience.com/learning-rate-schedules-and-adaptive-learning-rate-methods-for-deep-learning-2c8f433990d1
def OfA(X, y, House):
	costs = []
	y = np.array(y)
	theta = xavier(X)
	lr = 1
	m = float(len(X))
	for epoch in range(3000):
		theta = theta - lr * (1 / m) * (np.dot((predict(X, theta) - y), X))
		costs.append(cost(X, y, theta))
		lr = (1 / (1 + lr * epoch))
	x = np.arange(len(costs))
	plt.plot(x, costs)
	plt.title(House)
	plt.show()
	return costs

def	LogisticRegression(X, y):
	y_g = y.replace({"Gryffindor" : 1 , "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuff" : 0})
	y_s = y.replace({"Gryffindor" : 0 , "Slytherin" : 1, "Ravenclaw" : 0, "Hufflepuff" : 0})
	y_r = y.replace({"Gryffindor" : 0 , "Slytherin" : 0, "Ravenclaw" : 1, "Hufflepuff" : 0})
	y_h = y.replace({"Gryffindor" : 0 , "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuff" : 1})
	theta_g = OfA(X, y_g, "Gryffindor")
	theta_s = OfA(X, y_s, "Slytherin")
	theta_r = OfA(X, y_r, "Ravenclaw")
	theta_h = OfA(X, y_h, "Hufflepuff")
	thetas = [theta_g, theta_s, theta_r, theta_h]
	return thetas

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Please give a valid Dataset')
	dataset = pd.read_csv(sys.argv[1])
	dataset = dataset.fillna(dataset.mean())
	y = dataset['Hogwarts House']
	dataset = dataset[dataset.columns[6:19]]
	dataset = dataset.drop('Astronomy', axis=1)
	dataset = dataset.drop('Defense Against the Dark Arts', axis=1)
	X = np.array(dataset)
	X = StandardScaler(X)
	X = np.c_[np.ones(X.shape[0]), X]
	LogisticRegression(X,y)
