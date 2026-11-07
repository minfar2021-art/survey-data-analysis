import pandas as pd

# Load the dataset
file_path = "/storage/emulated/0/Download/survey.xlsx"
df = pd.read_excel(file_path)

# List of demographic variables
variables = ['A. Gender', 'B. Age', 'C. Education Level', 'D. Work Experience']

# Calculate frequency and percentage distributions
for var in variables:
    print(f"\n--- Frequency & Percentage Distribution: {var} ---")
    counts = df[var].value_counts()
    percents = df[var].value_counts(normalize=True) * 100
    summary_df = pd.DataFrame({'Frequency': counts, 'Percentage (%)': percents})
    print(summary_df)
