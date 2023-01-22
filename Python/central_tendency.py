import pandas as pd
#Load data from a text file
df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
#Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

passes = pd.Series(df_students['Grade'] >= 60)
#Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
from matplotlib import pyplot as plt
# Get the variable to examine
var = df_students['Grade']

#Get statistics
min_val = var.min()
max_val = var.max()
mean_val = var.mean()
med_val = var.median()
mod_val = var.mode()[0]

print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
		mean_val, med_val, mod_val, max_val))
#Create a figure
fig = plt.figure(figsize=(10,4))

#Plot o histogram
plt.hist(var)

# Add lines for the statistics
plt.axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2)
plt.axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2)
plt.axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2)
plt.axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2)
plt.axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2)

#Add titles and labels
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()