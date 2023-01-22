import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#load the training dataset
penguins = pd.read_csv('/Users/suvdaa/penguins.csv')

# Display a random sample of 10 observations
sample = penguins.sample(10)
penguin_classes = ['Adelie', 'Gentoo', 'Chinstrap']
print(sample.columns[0:5].values, 'SpeciesName')
for index, row in penguins.sample(10).iterrows():
	print('[', row[0], row[1], row[2], row[3], int(row[4]), ']', penguin_classes[int(row[4])])

# Count the number of null values for each column
print(penguins.isnull().sum())

print(penguins[penguins.isnull().any(axis=1)])

# Drop rows containing NaN values
penguins = penguins.dropna()
# Confirm there are now no nulls
print(penguins.isnull().sum())

penguin_features = ['CulmenLength', 'CulmenDepth', 'FlipperLength', 'BodyMass']
penguin_label = 'Species'
for col in penguin_features:
	penguins.boxplot(column=col, by=penguin_label, figsize=(6, 6))
	plt.title(col)

# Separate features and labels
penguins_X, penguins_y = penguins[penguin_features].values, penguins[penguin_label].values

# Split data 70%-30% into training set and test set

x_penguin_train, x_penguin_test, y_penguin_train, y_penguin_test = train_test_split(penguins_X, penguins_y,
                                                                                    test_size=0.30,
                                                                                    random_state=0,
                                                                                    stratify=penguins_y)

print ('Training Set: %d, Test Set: %d \n' % (x_penguin_train.shape[0], x_penguin_test.shape[0]))

# Set regularization rate
reg = 0.1

# train a logistic regression model on the training set
multi_model = LogisticRegression(C=1/reg, solver='lbfgs', multi_class='auto', max_iter=10000).fit(x_penguin_train, y_penguin_train)
print(multi_model)