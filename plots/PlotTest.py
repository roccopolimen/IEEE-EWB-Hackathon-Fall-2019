import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Import nyc filepath for pumpkin prices
new_york_filepath = "a-year-of-pumpkin-prices/new-york_9-24-2016_9-30-2017.csv"
new_york = pd.read_csv(new_york_filepath)

# See the first couple of values in the nyc csv file
new_york.head()
print(new_york.head())

swarm_plot = sns.swarmplot(x=new_york['Variety'],y=new_york['High Price'])
fig = swarm_plot.get_figure()
fig.savefig("pricentype.png")