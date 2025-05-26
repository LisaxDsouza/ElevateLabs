# ElevateLabs
A repo for uploading tasks given by elevate lab internship

# Task 1: Titanic Dataset Cleaning and Visualization

This project is a mini-task focused on data cleaning and visualizing the [Titanic dataset](https://www.kaggle.com/c/titanic/data) from Kaggle. It includes handling missing values, encoding, normalization, outlier detection and visualization.

##Task Objectives

- Handle missing values in columns such as Age, Cabin, and Embarked
- Encode categorical data (Sex)
- Normalize the Age column
- Detect and remove outliers using Interquartile Range (IQR)
- Visualize distributions and outliers using boxplots

## Steps Performed

1. **Load the dataset using pandas**
2. **Handle missing values:**
   - Filled Age with mean
   - Dropped Cabin due to high percentage of missing data
   - Filled Embarked with mode
3. **Encode categorical variable:**
   - Sex: male → 0, female → 1
4. **Remove duplicate rows**
5. **Normalize the Age column** (either z-score or min-max)
6. **Outlier detection and removal using IQR** for Age and Fare
7. **Visualize:**
   - Boxplot of Age
   - Boxplot of Age vs Survived

##Libraries Used

- `pandas`
- `matplotlib`
- `seaborn`

##Sample Visualizations

- Boxplot of `Age` before and after removing outliers
- Boxplot comparing `Age` across survival classes

## How to Run

```bash
# Clone the repository
git clone https://github.com/LisaxDsouza/titanic-cleaning-visualization.git
cd titanic-cleaning-visualization

# Run the script
python titanic_cleaning.py
