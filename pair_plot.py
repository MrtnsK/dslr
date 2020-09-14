import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
sns.set(style="ticks", color_codes=True)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit('Please give a valid Dataset')
	dataset = pd.read_csv(sys.argv[1])
	dataset.dropna(inplace=True)
	dataset = dataset.drop('Astronomy', axis='columns')
	dataset = dataset.drop('Defense Against the Dark Arts', axis='columns')
	sns.pairplot(dataset, hue = 'Hogwarts House', height=1)
	plt.show()
