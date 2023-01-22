import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
df_students = df_students.dropna(axis=0, how='any')
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
# Remove outliers with extremely low value
df_sample = df_students[df_students['StudyHours']>1]
df_regression = df_sample[['Grade', 'StudyHours']].copy()

#Get the regression slope and intercept
m, b, r, p, se = stats.linregress(df_regression['StudyHours'], df_regression['Grade'])
print('slope: {:.4f}\ny-intercept: {:.4f}'.format(m,b))
print('so...\n f(x) = {:.4f}x + {:.4f}'.format(m,b))

#Use the function (mx + b) to calculate f(x) for each x (StudyHours) value
df_regression['fx'] = (m * df_regression ['StudyHours']) + b

#Calculate the error between f(x) and the actual y (Grade) value
df_regression['error'] = df_regression['fx'] - df_regression['Grade']

#Create a scatter plot of Grade vs StudyHours
df_regression.plot.scatter(x='StudyHours', y='Grade')

#Plot the regression line
plt.plot(df_regression['StudyHours'], df_regression['fx'], color='cyan')

# Show the original x,y values, the f(x) value, and the error
print(df_regression[['StudyHours', 'Grade', 'fx', 'error']])
plt.show()