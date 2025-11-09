# -----------------------------------------------------------
# Project 2: Time Series & Category Charts
# Internship: Syntecxhub - Data Science
# Author: Sumit Gupta
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

print("===== Project 2: Time Series & Category Charts =====")

# -----------------------------------------------------------
# 1️⃣ Create / Load Sample Sales Dataset
# -----------------------------------------------------------
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=365, freq="D")
categories = ["Electronics", "Clothing", "Home Decor", "Books", "Toys"]
data = {
    "Date": np.random.choice(dates, 600),
    "Category": np.random.choice(categories, 600),
    "Sales": np.random.randint(100, 1000, size=600)
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

os.makedirs("charts", exist_ok=True)

# -----------------------------------------------------------
# 2️⃣ Time-Series Analysis: Plot Sales Over Time
# -----------------------------------------------------------
daily_sales = df.groupby("Date")["Sales"].sum()

plt.figure(figsize=(10,5))
plt.plot(daily_sales.index, daily_sales.values, color="royalblue", linewidth=1.5)
plt.title("Daily Sales Trend", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("charts/daily_sales_trend.png", dpi=300)
plt.close()

# -----------------------------------------------------------
# 3️⃣ Monthly & Quarterly Aggregation
# -----------------------------------------------------------
df["Month"] = df["Date"].dt.to_period("M")
df["Quarter"] = df["Date"].dt.to_period("Q")

monthly_sales = df.groupby("Month")["Sales"].sum()
quarterly_sales = df.groupby("Quarter")["Sales"].sum()

# Monthly line chart
plt.figure(figsize=(8,4))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o", color="green")
plt.title("Monthly Sales Overview")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("charts/monthly_sales.png", dpi=300)
plt.close()

# Quarterly bar chart
plt.figure(figsize=(6,4))
plt.bar(quarterly_sales.index.astype(str), quarterly_sales.values, color="orange")
plt.title("Quarterly Sales Comparison")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("charts/quarterly_sales.png", dpi=300)
plt.close()

# -----------------------------------------------------------
# 4️⃣ Category Comparison: Bar & Pie Charts
# -----------------------------------------------------------
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

# Bar chart
plt.figure(figsize=(7,4))
plt.bar(category_sales.index, category_sales.values, color="cornflowerblue")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("charts/category_sales_bar.png", dpi=300)
plt.close()

# Pie chart
plt.figure(figsize=(6,6))
plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=plt.cm.Set3.colors
)
plt.title("Category Sales Share")
plt.tight_layout()
plt.savefig("charts/category_sales_pie.png", dpi=300)
plt.close()

# -----------------------------------------------------------
# 5️⃣ Export Summary
# -----------------------------------------------------------
summary = {
    "Total_Sales": int(df["Sales"].sum()),
    "Best_Selling_Category": category_sales.idxmax(),
    "Highest_Sales_Month": monthly_sales.idxmax().strftime("%b %Y"),
    "Highest_Sales_Quarter": str(quarterly_sales.idxmax())
}

summary_text = f"""
===== Sales Summary Report =====
Total Sales: INR{summary['Total_Sales']:,}
Best Selling Category: {summary['Best_Selling_Category']}
Top Month: {summary['Highest_Sales_Month']}
Top Quarter: {summary['Highest_Sales_Quarter']}

Chart Discussion:
- Line charts were used for time-series trends (to show continuity over time).
- Bar charts provide an easy comparison across discrete categories/quarters.
- Pie charts visualize category share effectively for small category counts.
- Axis labels, titles, and legends enhance readability and professional clarity.
=================================
"""

with open("charts/summary_report.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print(summary_text)
print("All charts and summary exported to the 'charts/' folder successfully!")

