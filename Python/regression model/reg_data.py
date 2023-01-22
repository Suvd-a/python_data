import pandas as pd
import matplotlib.pyplot as plt

bike_data = pd.read_csv('/Users/suvdaa/daily-bike-share.csv')

bike_data['day'] = pd.DatetimeIndex(bike_data['dteday']).day
numeric_features =['temp', 'atemp', 'hum', 'windspeed']
#print(bike_data[numeric_features + ['rentals']].describe())
#print(bike_data.head())

# Get the label column
label = bike_data['rentals']

# Create a figure for 2 sublopts ( 2 rows, 1 column)
fig, ax = plt.subplots(2, 1, figsize = (9,12))

#Plot the histogram
ax[0].hist(label, bins=100)
ax[0].set_ylabel('Frequency')

#Add lines for the mean, median and mode)
ax[0].axvline(label.mean(), color='magenta', linestyle='dashed', linewidth=2)
ax[0].axvline(label.median(), color='cyan', linestyle='dashed', linewidth=2)

#Plot the boxplot
ax[1].boxplot(label, vert=False)
ax[1].set_xlabel('Rentals')

# Add a title to the Figure
fig.suptitle('Rental Distribution')

# Plot a histogram for each numeric feature
for col in numeric_features:
	fig = plt.figure(figsize=(9, 6))
	ax = fig.gca()
	feature = bike_data[col]
	feature.hist(bins=100, ax = ax)
	ax.axvline(feature.mean(), color='magenta', linestyle='dashed', linewidth=2)
	ax.axvline(feature.median(), color='cyan', linestyle='dashed', linewidth=2)
	ax.set_title(col)
plt.show()