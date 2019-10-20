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





filepath = "dummy.csv"
data = pd.read_csv(filepath)

# print(data.head())
# plot = sns.swarmplot(x=data[''], y=data[''])
# fig = plot.get_figure()
# fig.savefig("price_over_yield")

def fillCrops(data):
	cropNames = data.crop.unique()
	crops = {}
	# print(allCrops)
	for crop in cropNames:
		crops[crop] = data[data.crop == crop]

	return crops

# def createGraphs(crops):
diction = fillCrops(data)

'''
The input to this function is the value of the key in the array.
This void function will save 16 images with the crop name and the graphs in images folder
'''
def createGraphs(cArray,cropName):
	# Scatter plot with Yield and Temperature
	plot1 = sns.regplot(x=cArray['temperature'], y=cArray['yield'])
	fig1 = plot1.get_figure()
	fig1.savefig("images/"+cropName+"YieldOverTemperature")
	# Scatter Plot with Profit and Temperature
	plot2 = sns.regplot(x=cArray['temperature'], y=cArray['profit'])
	fig2 = plot2.get_figure()
	fig2.savefig("images/"+cropName+"ProfitOverTemperature")
	# Scatter Plot with Yield and Humidity
	plot3 = sns.regplot(x=cArray['humidity'], y=cArray['yield'])
	fig3 = plot3.get_figure()
	fig3.savefig("images/"+cropName+"YieldOverHumidity")
	# Scatter Plot with Profit and Humidity
	plot4 = sns.regplot(x=cArray['humidity'], y=cArray['profit'])
	fig4 = plot4.get_figure()
	fig4.savefig("images/"+cropName+"ProfitOverHumidity")
	# Scatter Plot with Yield and Pressure
	plot5 = sns.regplot(x=cArray['pressure'], y=cArray['yield'])
	fig5 = plot5.get_figure()
	fig5.savefig("images/"+cropName+"YieldOverPressure")
	# Scatter Plot with Profit and Pressure
	plot6 = sns.regplot(x=cArray['pressure'], y=cArray['profit'])
	fig6 = plot6.get_figure()
	fig6.savefig("images/"+cropName+"ProfitOverPressure")
	# Scatter Plot with Yield and WaterLevel
	plot7 = sns.regplot(x=cArray['waterlevel'], y=cArray['yield'])
	fig7 = plot7.get_figure()
	fig7.savefig("images/"+cropName+"YieldOverWaterLevel")
	# Scatter Plot with Profit and WaterLevel
	plot8 = sns.regplot(x=cArray['waterlevel'], y=cArray['profit'])
	fig8 = plot8.get_figure()
	fig8.savefig("images/"+cropName+"ProfitOverWaterLevel")
	# Bar Chart with Yield and City, State
	plot9 = sns.barplot(x=cArray['city,state'], y=cArray['yield'])
	fig9 = plot9.get_figure()
	fig9.savefig("images/"+cropName+"YieldBasedofLocation")
	# Bar Chart with Profit and City, State
	plot10 = sns.barplot(x=cArray['city,state'], y=cArray['profit'])
	fig10 = plot10.get_figure()
	fig10.savefig("images/"+cropName+"ProfitBasedofLocation")
	# KDEPlot with Yield
	plot11 = sns.kdeplot(data=cArray['yield'], shade=True)
	fig11 = plot11.get_figure()
	fig11.savefig("images/"+cropName+"YieldScatterplot")
	# KDEPlot with Profit
	plot12 = sns.kdeplot(data=cArray['profit'], shade=True)
	fig12 = plot12.get_figure()
	fig12.savefig("images/"+cropName+"ProfitScatterplot")
	# KDEPlot with Temperature
	plot13 = sns.kdeplot(data=cArray['temperature'], shade=True)
	fig13 = plot13.get_figure()
	fig13.savefig("images/"+cropName+"TemperatureScatterplot")
	# KDEPlot with Humidity
	plot14 = sns.kdeplot(data=cArray['humidity'], shade=True)
	fig14 = plot14.get_figure()
	fig14.savefig("images/"+cropName+"HumidityScatterplot")
	# KDEPlot with Pressure
	plot15 = sns.kdeplot(data=cArray['pressure'], shade=True)
	fig15 = plot15.get_figure()
	fig15.savefig("images/"+cropName+"PressureScatterplot")
	# KDEPlot with WaterLevel
	plot16 = sns.kdeplot(data=cArray['waterlevel'], shade=True)
	fig16 = plot16.get_figure()
	fig16.savefig("images/"+cropName+"WaterLevelScatterplot")

createGraphs(diction["Apple"],"Apple")