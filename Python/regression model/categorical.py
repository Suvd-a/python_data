import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bike_data = pd.read_csv('/Users/suvdaa/daily-bike-share.csv')

bike_data['day'] = pd.DatetimeIndex(bike_data['dteday']).day
# plot a bar plot for each categorical feature count
categorical_features = ['season', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'day']
for col in categorical_features:
	counts = bike_data[col].value_counts().sort_index()
	fig = plt.figure(figsize=(9, 6))
	ax = fig.gca()
	counts.plot.bar(ax = ax, color='steelblue')
	ax.set_title(col + ' counts')
	ax.set_xlabel(col)
	ax.set_ylabel("Frequency")
plt.show()
