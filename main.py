import matplotlib

matplotlib.use('TkAgg')  # Or 'QtAgg' if you have Qt installed
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('insurance.csv')

# Step 2: Compare average insurance charges between smokers and non-smokers
avg_charges = df.groupby('smoker')['charges'].mean()
print("Average charges:\n", avg_charges)

print("\nCounts by smoker status:\n", df['smoker'].value_counts())

# Step 3: Visualize with a boxplot
sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Insurance Charges by Smoking Status')
plt.xlabel('Smoker')
plt.ylabel('Charges')
plt.show()
