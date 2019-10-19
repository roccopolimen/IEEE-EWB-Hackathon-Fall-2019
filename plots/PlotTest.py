import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Import nyc filepath for pumpkin prices
# new_york_filepath = "a-year-of-pumpkin-prices/new-york_9-24-2016_9-30-2017.csv"
# new_york = pd.read_csv(new_york_filepath)

# See the first couple of values in the nyc csv file
# new_york.head()
# print(new_york.head())

# swarm_plot = sns.swarmplot(x=new_york['Variety'],y=new_york['High Price'])
# fig = swarm_plot.get_figure()
# fig.savefig("pricentype.png")





filepath = "../webapp/dataset.csv"
data = pd.read_csv(filepath)

# print(data.head())
# plot = sns.swarmplot(x=data[''], y=data[''])
# fig = plot.get_figure()
# fig.savefig("price_over_yield")

def fillCrops(data):
	cropNames = data.Crop.unique()
	crops = {}
	# print(allCrops)
	for crop in cropNames:
		crops[crop] = data[data.Crop == crop]

	return crops

print(fillCrops(pd.read_csv("dummy.csv")))
