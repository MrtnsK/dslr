import pandas as pd
import matplotlib.pyplot as plt
import sys

def scatter(dataset):
	plt.figure()
	plt.scatter(dataset['Astronomy'], dataset['Defense Against the Dark Arts'])
	plt.title("Similar Features")
	plt.xlabel("Astronomy")
	plt.ylabel("Defense Against the Dark Arts")
	plt.show()

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Please give a valid Dataset')
	dataset = pd.read_csv(sys.argv[1])
	dataset.dropna(inplace=True)
	scatter(dataset)
