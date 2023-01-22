import pandas as pd
from matplotlib import pyplot as plt

df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
df_students = df_students.dropna(axis=0, how='any')
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
# Remove outliers with extremely low value
df_sample = df_students[df_students['StudyHours']>1]

# Define a function based on our regression coefficients
def f(x):
	m = 6.3134
	b = -17.9164
	return m*x + b

study_time = 14

#Get f(x) for study time
prediction = f(study_time)

#Grade can't be less than 0 or more than 100
expected_grade = max(0,min(100,prediction))

#Print the estimated grade
print ('Studying for {} hours per week may result in a grade of {:.0f}'.format(study_time, expected_grade))