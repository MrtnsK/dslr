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

def get_dataset():
	try:
		dataset = pd.read_csv(sys.argv[1])
		dataset = dataset.fillna(dataset.mean())
		y = dataset['Hogwarts House']
		dataset = dataset[dataset.columns[6:19]]
		dataset = dataset.drop('Astronomy', axis=1)
		dataset = dataset.drop('Defense Against the Dark Arts', axis=1)
		dataset = dataset.drop('Arithmancy', axis=1)
		dataset = dataset.drop('Care of Magical Creatures', axis=1)
		dataset = dataset.drop('Potions', axis=1)
		X = np.array(dataset)
		X = StandardScaler(X)
		X = np.c_[np.ones(X.shape[0]), X]
		return X, y
	except:
		print('Error with the dataset!')
		exit(1)

def get_thetas():
	try:
		thetas = pd.read_csv(sys.argv[2])
		theta_g = thetas['Gryffindor']
		theta_s = thetas['Slytherin']
		theta_r = thetas['Ravenclaw']
		theta_h = thetas['Hufflepuff']
		return theta_g, theta_s, theta_r, theta_h
	except:
		print('Error with the thetas.csv!')
		exit(1)	

if __name__ == "__main__":
	if (len(sys.argv) != 3):
		sys.exit('Please give a valid Dataset and the thetas.csv')
	X, y = get_dataset()
	theta_g, theta_s, theta_r, theta_h = get_thetas()
	pred_g = predict(X, theta_g)
	pred_s = predict(X, theta_s)
	pred_r = predict(X, theta_r)
	pred_h = predict(X, theta_h)
	prediction = []
	for i in range(len(pred_g)):
		grade = 0
		house = 0
		if pred_g[i] > pred_s[i]:
			grade = pred_g[i]
			house = 'Gryffindor'
		else:
			grade = pred_s[i]
			house = 'Slytherin'
		if pred_r[i] > grade:
			grade = pred_r[i]
			house = 'Ravenclaw'
		if pred_h[i] > grade:
			grade = pred_h[i]
			house = 'Hufflepuff'
		prediction.append(house)
	prediction = np.array(prediction)
	prediction = pd.DataFrame(prediction, columns=['Hogwarts House'])
	prediction = prediction.rename_axis('Index', axis=0)
	prediction.to_csv('houses.csv')
