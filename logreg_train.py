import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def StandardScaler(X):
    mean = np.mean(X, axis=0)
    scale = np.std(X - mean, axis=0)
    return (X - mean) / scale

def	cost(X, y, theta, passes):
	

def OfA(X, y):
	theta = 0
	m = float(len(X))
	for passes in range(2000):
		theta = theta - 1 * (1 / m) * (X.T @ ((X @ theta) - y))
		cost(X, y, theta, passes)

def	LogisticRegression(X, y):
	y_g = y.replace({"Gryffindor" : 1 , "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuf" : 0})
	y_s = y.replace({"Gryffindor" : 0 , "Slytherin" : 1, "Ravenclaw" : 0, "Hufflepuf" : 0})
	y_r = y.replace({"Gryffindor" : 0 , "Slytherin" : 0, "Ravenclaw" : 1, "Hufflepuf" : 0})
	y_h = y.replace({"Gryffindor" : 0 , "Slytherin" : 0, "Ravenclaw" : 0, "Hufflepuf" : 1})
	theta_g = OfA(X, y_g)
	theta_s = OfA(X, y_s)
	theta_r = OfA(X, y_r)
	theta_h = OfA(X, y_h)
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
	print(X)
	X = StandardScaler(X)
	X = np.c_[np.ones(X.shape[0]), X]
	print(X)
