from google_crc32c import value
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv(r'C:\Users\Kwakhanya.Naka\python\credit_card_fraud_dataset.csv')
except Exception as e:
    print("Error loading dataset:", e)

### Data Cleaning ###
# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Fill missing values using forward fill method
df.ffill(inplace=True)  # Forward fill example

# Display the DataFrame after filling missing values
print("\nData after filling missing values:")
print(df.head(4))

### Data Manipulation ###
# Example: Filter for fraudulent transactions
fraudulent_df = df[df['IsFraud'] == 1]
print("\nFraudulent transactions:")
print(fraudulent_df.head(10))

### Statistical Analysis ###
# Display the shape of the dataset (number of rows and columns)
print("Shape of the dataset:", df.shape)

# Display data types of each column
print("\nData types:")
print(df.dtypes)

# Display summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Display summary statistics for all columns, including categorical
print("\nSummary statistics for all columns:")
print(df.describe(include='all'))

### Visualization ###
# Visualization: Distribution of Transaction Amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['Amount'], bins=30, kde=True, color="purple")
plt.title('Distribution of Transaction Amounts', color="green")
plt.xlabel('Transaction Amount', color="green")
plt.ylabel('Frequency', color="green")
plt.show()

# Visualization: Count of Fraudulent vs Non-Fraudulent Transactions
plt.figure(figsize=(8, 5))
ax = sns.countplot(x='IsFraud', data=df, palette=["#FF9999", "#66B3FF"])  # More distinct colors
plt.title('Count of Fraudulent vs Non-Fraudulent Transactions', color="blue")
plt.xlabel('Is Fraud', color="blue")
plt.ylabel('Count', color="blue")

# Add value annotations on top of the bars
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='baseline', 
                color='black', fontsize=12)

plt.xticks(ticks=[0, 1], labels=['Non-Fraudulent', 'Fraudulent'])  # Better labels
plt.show()

# Save cleaned data if needed
df.to_csv(r'C:\Users\Kwakhanya.Naka\python\cleaned_credit_card_fraud_dataset.csv', index=False)
