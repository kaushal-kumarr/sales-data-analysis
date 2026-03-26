# Sales Data Analysis Project
# Author: Kaushal
# Description: This script loads, cleans, analyzes sales data and generates a report

import pandas as pd

# -------------------------------
# STEP 1: LOAD DATA
# -------------------------------
try:
    df = pd.read_csv('sales_data.csv')
    print(" Data loaded successfully!\n")
except FileNotFoundError:
    print(" Error: sales_data.csv file not found!")
    exit()

# -------------------------------
# STEP 2: EXPLORE DATA
# -------------------------------
print("First 5 Rows:")
print(df.head(), "\n")

print("Shape of Data (Rows, Columns):")
print(df.shape, "\n")

print("Column Names:")
print(df.columns, "\n")

print("ℹData Info:")
print(df.info(), "\n")

# -------------------------------
# STEP 3: DATA CLEANING
# -------------------------------
print("Checking Missing Values:")
print(df.isnull().sum(), "\n")

# Fill missing values with 0 (you can change logic if needed)
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("Data cleaning completed!\n")


# -------------------------------
# STEP 4: DATA ANALYSIS
# -------------------------------

# Ensure column exists
if 'Total_Sales' not in df.columns:
    print("Column 'Total_Sales' not found in dataset!")
    exit()

# Convert to numeric (if needed)
df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce')

# Calculate metrics
total_sales = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
max_sales = df['Total_Sales'].max()
min_sales = df['Total_Sales'].min()

# Best selling product (if Product column exists)
if 'Product' in df.columns:
    best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
else:
    best_product = "N/A"

# -------------------------------
# STEP 5: DISPLAY RESULTS
# -------------------------------
print(" --- SALES SUMMARY REPORT --- ")
print(f"Total Revenue: ₹{total_sales:,.2f}")
print(f"Average Sales: ₹{average_sales:,.2f}")
print(f"Highest Sale: ₹{max_sales:,.2f}")
print(f"Lowest Sale: ₹{min_sales:,.2f}")
print(f"Best Selling Product: {best_product}")

# -------------------------------
# STEP 6: SAVE CLEANED DATA
# -------------------------------
df.to_csv('cleaned_sales_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_sales_data.csv'")

# -------------------------------
# STEP 7: GENERATE REPORT FILE
# -------------------------------
with open("analysis_report.md", "w", encoding="utf-8") as f:
    f.write("# Sales Data Analysis Report\n\n")
    f.write(f"## Total Revenue\n₹ {total_sales:,.2f}\n\n")
    f.write(f"## Average Sales\n₹ {average_sales:,.2f}\n\n")
    f.write(f"## Highest Sale\n₹ {max_sales:,.2f}\n\n")
    f.write(f"## Lowest Sale\n₹ {min_sales:,.2f}\n\n")
    f.write(f"## Best Selling Product\n{best_product}\n\n")
    f.write("## Insights\n")
    f.write("- This report shows overall sales performance.\n")
    f.write("- Best product contributes highest revenue.\n")
    f.write("- Data cleaned and processed using pandas.\n")

print("Report generated as 'analysis_report.md'")

# -------------------------------
# END
# -------------------------------
print("\nProject Completed Successfully!")
