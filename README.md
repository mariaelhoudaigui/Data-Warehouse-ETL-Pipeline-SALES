#  Business Intelligence System with SSIS & Power BI

##  Project Description

This project focuses on creating a complete business intelligence system to analyze the commercial performance of an electronics sales company
The main objective is to support data-driven decision-making through:

- A well-structured **Data Warehouse** 
- Robust **ETL processes** using SSIS
- Automated daily data refresh with **SQL Server Jobs**
- Interactive **Power BI dashboards**

---

##  Educational Objectives

- Design a **Data Warehouse** using a snowflake schema
- Develop a complete **ETL process** with **SQL Server Integration Services (SSIS)**:
  - Extract data from multiple sources
  - Clean, transform, enrich, and aggregate the data
  - Load the data into the Data Warehouse
- Schedule **daily ETL jobs** using **SQL Server Agent**
- Build **interactive dashboards** in **Power BI** including KPIs and visual charts.

---

## Technologies Used

- **Microsoft SQL Server**
- **SQL Server Integration Services (SSIS)**
- **Power BI**
- **Python** 
---

##  Data Warehouse Schema

A **snowflake schema** was designed with the following structure:

### 🔹 Fact Table

- `FactSales`: contains measures such as:
  - Quantity Sold
  - Total Revenue
  - Total Cost
  - Profit Margin

### 🔹 Dimension Tables

- `Product Dimension`
  - Brand
  - Category
  - Sub-category
  - Rating

- `Store Dimension`
  - Country
  - State/Region
  - Store

- `Customer Dimension`
  - Continent
  - Country
  - State
  - City

- `Time Dimension`
  - Year
  - Month
  - Day

This model supports **multi-level analysis** and **dynamic filtering** in Power BI for better insight generation.

## KPIs & Dashboard

The Power BI dashboard includes the following **Key Performance Indicators (KPIs)**:

- **Revenue** and **Profit Margin** – displayed as cards
- **Sales by Store** – donut chart
- **Top 10 Products by Revenue** – bar chart
- **Customer Count** and **Transaction Count** – cards
- **Quantity Sold by Country** – map visualization
- **Annual Revenue Trends** – line chart

All KPIs are dynamic and respond to filters such as **year**, **month**, **country**, and **brand**.

