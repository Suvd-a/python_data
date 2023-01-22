import pandas as pd
#Load data from a text file
df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
#Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

passes = pd.Series(df_students['Grade'] >= 60)
#Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

var = df_students['Grade']
# Create a function 
def show_distribution(var_data):
	from matplotlib import pyplot as plt

	#Get statistics
	min_val = var.min()
	max_val = var.max()
	mean_val = var.mean()
	med_val = var.median()
	mod_val = var.mode()[0]
	print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
		mean_val, med_val, mod_val, max_val))

	#Create a figure for 2 subplots (2 rows, 1 column)
	fig, ax = plt.subplots(2, 1, figsize = (10,4))

	#Plot the histogram
	ax[0].hist(var_data)
	ax[0].set_ylabel('Frequency')

	#Add lines for the mean, median and mode
	ax[0].axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2)
	ax[0].axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2)
	ax[0].axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2)
	ax[0].axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2)
	ax[0].axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2)

	#Plot the boxplot
	ax[1].boxplot(var_data, vert=False)
	ax[1].set_xlabel('Value')

	#Add a title to the Figure
	fig.suptitle('Data Distribution')

	#Show the figure
	plt.show()

#Get the variable to examine
col = df_students['Grade']

#Call the function
show_distribution(col)