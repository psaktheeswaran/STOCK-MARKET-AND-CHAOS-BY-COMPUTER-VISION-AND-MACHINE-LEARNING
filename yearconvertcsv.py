import pandas as pd

# Read the CSV file
df = pd.read_csv("CIPLA.csv")

# Extract the year from the "Date" column
df['Date'] = pd.to_datetime(df['Date']).dt.year

# Save the modified DataFrame to a new CSV file
df.to_csv("CIPLA_year_only.csv", index=False)

