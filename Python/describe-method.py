import pandas as pd
from matplotlib import pyplot as plt

df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
df_students = df_students.dropna(axis=0, how='any')
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
# Remove outliers with extremely low value
# df_sample = df_students[df_students['StudyHours']>1]
print(df_students.describe())