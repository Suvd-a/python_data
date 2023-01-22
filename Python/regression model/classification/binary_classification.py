import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

diabetes = pd.read_csv('/Users/suvdaa/diabetes.csv')

# Separate features and labels
features = ['Pregnancies', 'PlasmaGlucose', 'DiastolicBloodPressure', 'TricepsThickness', 'SerumInsulin', 'BMI', 'DiabetesPedigree', 'Age']
label = 'Diabetic'
X, y = diabetes[features].values, diabetes[label].values

for n in range(0,4):
	print("Patient", str(n+1), "\n  Features:", list(X[n]), "\n Label:", y[n])

for col in features:
	diabetes.boxplot(column=col, by='Diabetic', figsize=(6,6))
	plt.title(col)

# Split data 70%-30% into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

print('Training cases: %d\nTest cases: %d' % (X_train.shape[0], X_test.shape[0]))