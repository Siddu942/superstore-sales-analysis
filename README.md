### Superstore Sales Analysis (Python + Power BI)
# Overview
This project focuses on analyzing the Superstore dataset, which contains a little over 10,000 sales records. I used Python (mainly Pandas) to clean the data, create additional useful features, and generate summary tables. The cleaned dataset and summaries were then used to build an interactive Power BI dashboard to study sales, profit patterns, and performance across regions, categories, and customer segments.
# Tools Used
Python (Pandas, NumPy)
Power BI Desktop
Matplotlib / Seaborn for initial exploration
CSV files for storing cleaned and summary datasets
Process
# 1. Data Cleaning & Feature Creation (Python)
I cleaned the raw data by fixing encoding issues, converting date columns, removing duplicates, and filling missing values when needed.
I also created several additional fields to make the analysis easier, such as delivery days, profit margin, sales per unit, and separate columns for year, month, weekday, and a Year-Month key.
# 2. Creating Summary Datasets
To make the Power BI dashboard faster and more organized, I generated separate summary tables for:
Regions
Categories and Sub-Categories
Monthly performance
Customer segments
These summaries include total sales, profit, quantities, and margins.
# 3. Exploratory Data Analysis
Before building the dashboard, I explored monthly trends, category-level performance, discount impact on profit, and regional differences. This helped identify which visuals were useful for the dashboard.
# 4. Power BI Dashboard
The dashboard includes:
KPI cards for overall sales, profit, order count, and profit margin
Monthly trends for sales and profit
Regional performance comparison
Category and sub-category breakdown
Segment contribution
Slicers to filter by year, region, category, and segment
# Key Insights
The West region performs the best overall.
Technology brings in the highest revenue.
Higher discounts generally reduce profit.
Sales peak during November and December.
Corporate and Consumer segments contribute most of the orders.
Repository Structure
Superstore-Sales-Analysis/
│
├── Superstore_Sales_Analysis.pbix
├── Superstore_Cleaned.csv
├── Region_Summary.csv
├── Category_Summary.csv
├── Monthly_Summary.csv
├── Segment_Summary.csv
└── README.md
# How to View the Power BI dashboard
Download the repository
Open the PBIX file in Power BI Desktop
Use the slicers to interact with different parts of the report
