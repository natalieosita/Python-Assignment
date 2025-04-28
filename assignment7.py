# 1. Load and explore the dataset
import pandas as pd

# Load dataset (modify the file path accordingly)
df = pd.read_csv("your_dataset.csv")

# Display first few rows
print(df.head())

# Check data types and missing values
print(df.info())
print(df.isnull().sum())

# Clean missing values (drop or fill)
df = df.dropna()  # Alternative: df.fillna(method='ffill')


# 2. Basic data analysis
# Compute basic statistics
print(df.describe())

# Group by a categorical column (modify column name)
grouped_data = df.groupby("Category_Column")["Numerical_Column"].mean()
print(grouped_data)

# Identify patterns
print(df.corr())  # Displays correlation between numerical columns


# 3. Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Line Chart (Trends Over Time)
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="Date_Column", y="Value_Column")
plt.title("Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.show()

# Bar Chart (Comparison)
plt.figure(figsize=(8,5))
sns.barplot(x="Category_Column", y="Numerical_Column", data=df)
plt.title("Comparison of Categories")
plt.show()

# Histogram (Distribution)
plt.figure(figsize=(8,5))
sns.histplot(df["Numerical_Column"], bins=20)
plt.title("Distribution of Numerical Column")
plt.show()

# Scatter Plot (Relationship between two numerical columns)
plt.figure(figsize=(8,5))
sns.scatterplot(x="Numerical_Column1", y="Numerical_Column2", data=df)
plt.title("Scatter Plot")
plt.show()


# 4. Error handling
try:
    df = pd.read_csv("your_dataset.csv")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")