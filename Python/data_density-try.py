import pandas as pd
from matplotlib import pyplot as plt

df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
df_students = df_students.dropna(axis=0, how='any')
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
print(df_students)
def show_density(var_data):
	fig = plt.figure(figsize=(10,4))

	#Plot density
	var_data.plot.density()

	#Add titles and labels
	plt.title('Data Density')

	#Show the mean, median, and mode
	plt.axvline(x=var_data.mean(), color = 'cyan', linestyle='dashed', linewidth = 2)
	plt.axvline(x=var_data.median(), color = 'red', linestyle='dashed', linewidth = 2)
	plt.axvline(x=var_data.mode()[0], color = 'yellow', linestyle='dashed', linewidth = 2)

	#Show the figure
	plt.show()

#Get the density of StudyHours
col = df_students['StudyHours']
show_density(col)