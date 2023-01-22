import pandas as pd
#Load data from a text file
df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
#Remove any rows with missing data
#passes = pd.Series(df_students['Grade'] >= 60)
#Save who passed to the Pandas dataframe
#df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
from matplotlib import pyplot as plt
# Get the variable to examine
var_data = df_students['Grade']
#Create a Figure
fig = plt.figure(figsize=(10,4))
#Plot a histogram
plt.hist(var_data)

#Add titles and labels
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
#Show the figure
plt.show()
