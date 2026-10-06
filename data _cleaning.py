import pandas as pd

# Load dataset
df = pd.read_csv("task1_raw_dataset.csv")

# Handle missing values
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Price"] = df["Price"].fillna(df["Price"].median())

# Fix text formatting
for col in ["Customer_Name", "Product", "Region"]:
    df[col] = df[col].astype(str).str.strip().str.title()

# Convert date to proper format
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Remove duplicate records
df = df.drop_duplicates()

# Create Total Sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Save cleaned dataset
df.to_csv("task1_cleaned_dataset.csv", index=False)

print("Data cleaning completed successfully.")
print(df)