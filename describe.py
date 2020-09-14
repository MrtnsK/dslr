import pandas as pd
import sys
from math import sqrt
import numpy as np

def get_m(c):
	_max = 0
	_min = 0
	for i in c:
		if (i > _max):
			_max = i
		if (i < _min):
			_min = i
	return _max, _min

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
		c.sort()
		count.append(len(c))
		mean.append(sum(c) / len(c))
		_max, _min = get_m(c)
		vmin.append(min(c))
		vmax.append(max(c))
		result = 0
		for i in range(len(c)):
			result += (c[i] - sum(c) / len(c))**2 
		result = result / (len(c) - 1)
		std.append(sqrt(result))
		fQ.append(c[int(len(c) * 0.25)])
		sQ.append(c[int(len(c) * 0.5)])
		tQ.append(c[int(len(c) * 0.75)])
	datalist = list(zip(count, mean, std, vmin, fQ, sQ, tQ, vmax))
	datalist = np.transpose(datalist)
	dataframe = pd.DataFrame(datalist, columns=data.columns.values, index=['count', 'mean', 'std', 'vmin', '25%', '50%', '75%', 'vmax'])
	print(dataframe)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Please give a valid Dataset')
	dataset = pd.read_csv(sys.argv[1])
	describe(dataset)
