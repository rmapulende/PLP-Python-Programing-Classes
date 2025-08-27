import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ================================
# Task 1: Load and Explore Dataset
# ================================
try:
    # Load Iris dataset directly from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Creates a pandas DataFrame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # Add species names

    print("✅ Dataset loaded successfully!\n")

    # Display first 5 rows
    print("First 5 rows:")
    print(df.head())

    # Check structure
    print("\nDataset Info:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean dataset (no missing values in Iris, but let's show example)
    df_cleaned = df.dropna()

except FileNotFoundError:
    print("❌ Error: Dataset file not found!")
    exit()
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    exit()

# ================================
# Task 2: Basic Data Analysis
# ================================
print("\n📊 Basic Statistics:")
print(df_cleaned.describe())

# Grouping by species
grouped = df_cleaned.groupby("species")["sepal length (cm)"].mean()
print("\nAverage Sepal Length by Species:")
print(grouped)

# Pattern/Insight Example
print("\n🔎 Insights:")
print("- Iris-virginica has the largest average sepal length.")
print("- Iris-setosa tends to have smaller petals overall compared to other species.")

# ================================
# Task 3: Data Visualization
# ================================
sns.set(style="whitegrid")

# 1. Line Chart (simulate trend by plotting index vs sepal length)
plt.figure(figsize=(8,5))
plt.plot(df_cleaned.index, df_cleaned["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df_cleaned, ci=None, palette="Set2")
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: Sepal Width Distribution
plt.figure(figsize=(8,5))
sns.histplot(df_cleaned["sepal width (cm)"], bins=20, kde=True, color="skyblue")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df_cleaned, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
