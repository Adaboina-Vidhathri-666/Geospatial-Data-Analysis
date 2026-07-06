import pandas as pd

# Load dataset
df = pd.read_csv("sales_locations.csv")

print("Original Dataset\n")
print(df)

# Total Sales
print("\nTotal Sales")
print(df["Sales"].sum())

# Average Sales
print("\nAverage Sales")
print(df["Sales"].mean())

# Highest Sales City
print("\nHighest Sales City")
print(df.loc[df["Sales"].idxmax()])

# High Demand but Low Sales
opportunity = df[
    (df["Demand"] == "High") &
    (df["Sales"] < 60000)
]

print("\nBusiness Expansion Opportunities")
print(opportunity)

# Save report
opportunity.to_csv("business_expansion.csv", index=False)

print("\nAnalysis Completed Successfully!")