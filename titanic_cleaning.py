import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
path = r'C:\Users\lisah\Downloads\TitanicDataset.csv'
data = pd.read_csv(path)

# 2. Display the first few rows
print("First 5 rows of the dataset:")
print(data.head())

# 3. Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# 4. Handle missing values
# Fill missing 'Age' with mean
data['Age'] = data['Age'].fillna(data['Age'].mean())

# Drop 'Cabin' due to excessive missing data
data.drop(columns='Cabin', inplace=True)

# Fill missing 'Embarked' with mode
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# 5. Encode categorical variable
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 6. Remove duplicate rows
data.drop_duplicates(inplace=True)

# 7. Remove outliers using Interquartile Range (IQR)
def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)].copy()

# Apply IQR method to remove outliers from 'Age' and 'Fare'
data = remove_outliers_iqr(data, 'Age')
data = remove_outliers_iqr(data, 'Fare')

# 8. Normalize the 'Age' column using Min-Max normalization
data['Age'] = (data['Age'] - data['Age'].min()) / (data['Age'].max() - data['Age'].min())

# 9. Visualizations
# Boxplot of 'Age' after preprocessing
plt.figure(figsize=(6, 4))
sns.boxplot(y=data['Age'])
plt.title('Boxplot of Age (After Outlier Removal & Normalization)')
plt.show()

# Boxplot of 'Age' grouped by 'Survived'
plt.figure(figsize=(6, 4))
sns.boxplot(x='Survived', y='Age', data=data)
plt.title('Survival by Age')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Normalized Age')
plt.show()
