import pandas as pd
from matplotlib import pyplot as plt

df_students = pd.read_csv('/Users/suvdaa/Downloads/grades.csv', delimiter=',', header='infer')
df_students = df_students.dropna(axis=0, how='any')
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
print(df_students)
for col_name in ['Grade', 'StudyHours']:
	col = df_students[col_name]
	rng = col.max() - col.min()
	var = col.var()
	std = col.std()
	print('\n{}:\n - Range: {:.2f}\n - Variance: {:.2f}\n - Std.Dev: {:.2f}'.format(col_name, rng, var, std))
