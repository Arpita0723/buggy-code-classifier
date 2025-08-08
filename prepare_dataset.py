# prepare_dataset.py

import pandas as pd

# ✅ Load the dataset from dataset.csv
df = pd.read_csv("dataset.csv")

# ✅ Show how many samples we have
print("✅ Dataset loaded with", len(df), "samples")

# ✅ Check for missing values
if df.isnull().sum().sum() == 0:
    print("✅ No missing values found.")
else:
    print("⚠️ Missing values detected!")

# ✅ Save the dataset again (optional step, just ensures it's accessible)
df.to_csv("dataset.csv", index=False)
print("✅ Dataset saved as dataset.csv")
