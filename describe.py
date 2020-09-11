import pandas as pd
import csv
import sys

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
		c.sort
		count.append(len(c))
		mean.append(sum(c) / len(c))
		vmin = min(c)
		vmax = max(c)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Please give a valid Dataset')
	dataset = pd.read_csv(sys.argv[1])
	describe(dataset)
