import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler

df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
df_students = df_students.dropna(axis=0, how='any')
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
# Remove outliers with extremely low value
df_sample = df_students[df_students['StudyHours']>1]

#Get a scaler object
scaler = MinMaxScaler()

#Create a new dataframe for the scaled values
df_normalized = df_sample[['Name', 'Grade','StudyHours']].copy()
#Normalize the numeric columns
df_normalized[['Grade', 'StudyHours']] = scaler.fit_transform(df_normalized[['Grade', 'StudyHours']])

#Plot the normalized values
df_normalized.plot(x='Name', y=['Grade', 'StudyHours'], kind='bar', figsize=(8,5))
#print(df_normalized.Grade.corr(df_normalized.StudyHours))
#Create a scatter plot
df_sample.plot.scatter(title='Study Time vs Grade', x='StudyHours', y='Grade')
plt.show()