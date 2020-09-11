import pandas as pd
import csv
import sys
from math import sqrt

def describe(dataset):
	data = dataset[dataset.columns[6:19]]
	count = []
	mean = []
	std = []
	vmin = []
	fQ = []
	sQ = []
	tQ = []
	vmax = []
	for i in range(data.shape[1]):
		c = data.iloc[:,i].tolist()
		c = [x for x in c if str(x) != 'nan']
		c.sort
		count.append(len(c))
		mean.append(sum(c) / len(c))
		vmin.append(min(c))
		vmax.append(max(c))
		result = 0
		for i in range(len(c)):
			result += (c[i] - sum(c) / len(c))**2 
		result = result / (len(c) - 1)
		std = sqrt(result)
		print (std)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Please give a valid Dataset')
	dataset = pd.read_csv(sys.argv[1])
	describe(dataset)
