import pandas as pd
import matplotlib.pyplot as plt

bike_data = pd.read_csv('/Users/suvdaa/daily-bike-share.csv')

bike_data['day'] = pd.DatetimeIndex(bike_data['dteday']).day
numeric_features =['temp', 'atemp', 'hum', 'windspeed']
for col in numeric_features:
	fig = plt.figure(figsize=(9, 6))
	ax = fig.gca()
	feature = bike_data[col]
	label = bike_data['rentals']
	correlation = feature.corr(label)
	plt.scatter(x=feature, y=label)
	plt.xlabel(col)
	plt.ylabel('Bike rentals')
	ax.set_title('rentals vs ' + col + '- correlation: ' + str(correlation))
plt.show()
