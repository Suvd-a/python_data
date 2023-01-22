data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
import numpy as np
grades = np.array(data)
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]
student_data = np.array([study_hours, grades])
import pandas as pd
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
							'StudyHours':student_data[0],
							'Grade':student_data[1]})
df_students =pd.read_csv('/Users/suvdaa/Downloads/grades.csv',delimiter=',',header='infer')

df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
df_students = df_students.dropna(axis=0, how='any')
mean_study = df_students['StudyHours'].mean()
mean_grade = df_students.Grade.mean()
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
df_students = df_students.sort_values('Grade', ascending=False)
print(df_students)