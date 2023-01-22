import pandas as pd
import matplotlib.pyplot as plt

bike_data = pd.read_csv('/Users/suvdaa/daily-bike-share.csv')

bike_data['day'] = pd.DatetimeIndex(bike_data['dteday']).day
categorical_features = ['season', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'day']

# plot a boxplot for the label by each categorical feature
for col in categorical_features:
	fig = plt.figure(figsize=(9, 6))
	ax = fig.gca()
	bike_data.boxplot(column = 'rentals', by = col, ax = ax)
	ax.set_title('Label by ' + col)
	ax.set_ylabel("Bike Rentals")
plt.show()