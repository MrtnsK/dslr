import pandas as pd
import matplotlib.pyplot as plt
import sys

def	get_house_grades(dataset, gradedata, house, grade):
	data = gradedata[dataset["Hogwarts House"] == house][grade]
	data.dropna(inplace=True)
	return data

def histogram(dataset, gradedata):
	for col in gradedata.columns:
		plt.figure()
		plt.hist(get_house_grades(dataset, gradedata, 'Gryffindor', col), bins=50, label = 'Gryffindor', color = 'r')
		plt.hist(get_house_grades(dataset, gradedata, 'Slytherin', col), bins=50, label = 'Slytherin', color = 'g')
		plt.hist(get_house_grades(dataset, gradedata, 'Hufflepuff', col), bins=50, label = 'Hufflepuff', color = 'b')
		plt.hist(get_house_grades(dataset, gradedata, 'Ravenclaw', col), bins=50, label = 'Ravenclaw', color = 'y')
		plt.title(col)
		plt.legend(loc = 'upper left')
		plt.show()

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		sys.exit('Please give a valid Dataset')
	dataset = pd.read_csv(sys.argv[1])
	gradedata = dataset[dataset.columns[6:19]]
	histogram(dataset, dataset[gradedata.columns.values])
