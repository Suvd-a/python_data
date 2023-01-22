import pandas as pd

#Load data from a text file
df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
#Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

passes = pd.Series(df_students['Grade'] >= 60)
#Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

def show_density(var_data):
	from matplotlib import pyplot as plt

	fig = plt.figure(figsize=(10,4))

	#Plot density
	var_data.plot.density()

	#Add titles and labels
	plt.title('Data Density')

	#Show the mean, median and mode
	plt.axvline(x=var_data.mean(), color = 'cyan', linestyle='dashed', linewidth = 2)
	plt.axvline(x=var_data.median(), color = 'red', linestyle='dashed', linewidth = 2)
	plt.axvline(x=var_data.mode()[0], color = 'yellow', linestyle='dashed', linewidth = 2)

	#Show the figure
	plt.show()

#Get the density of Grade
col = df_students['Grade']
show_density(col)