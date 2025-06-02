import matplotlib

matplotlib.use('TkAgg')  # Or 'QtAgg' if you have Qt installed
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('insurance.csv')

