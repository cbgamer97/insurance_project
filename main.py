import matplotlib

matplotlib.use('TkAgg')  # Or 'QtAgg' if you have Qt installed
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('insurance.csv')

# Calculate averages and counts
avg_charges = df.groupby('smoker')['charges'].mean()
avg_bmi = df.groupby('smoker')['bmi'].mean()
smoking_counts = df[df['smoker'] == 'yes'].groupby('sex').size()

print("Average charges by smoking status:\n", avg_charges)
print("\nAverage BMI by smoking status:\n", avg_bmi)
print("\nNumber of smokers by sex:\n", smoking_counts)

# Create subplots for boxplots and barplot
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Boxplot for charges by smoker
sns.boxplot(ax=axes[0], x='smoker', y='charges', data=df)
axes[0].set_title('Insurance Charges by Smoking Status')
axes[0].set_xlabel('Smoker')
axes[0].set_ylabel('Charges')

# Boxplot for BMI by smoker
sns.boxplot(ax=axes[1], x='smoker', y='bmi', data=df)
axes[1].set_title('BMI by Smoking Status')
axes[1].set_xlabel('Smoker')
axes[1].set_ylabel('BMI')

plt.tight_layout()
plt.show()
