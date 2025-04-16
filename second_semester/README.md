# 🧪 Data Science Explorations: Missing Data Patterns & COVID-19 Trends

This project covers **two key explorations** in data analysis:

1. **🏠 Missing Data Analysis** using the **Bangalore House Price** dataset  
2. **🦠 COVID-19 Time Series Visualization** for U.S. states  

Both parts demonstrate real-world applications of exploratory data analysis (EDA), missing data handling, and data visualization using Python.

---

## 1️⃣ Missing Data Analysis (MCAR, MAR, MNAR) - 🏠 Bangalore House Price Dataset

### 📊 Dataset Overview

The Bangalore house price dataset contains listings with features like:
- Location  
- Size (e.g., 2 BHK, 3 Bedroom)  
- Area type (e.g., Super built-up Area, Carpet Area)  
- Price  
- Balcony count  
- Availability date  

### 🎯 Objective

Identify and classify types of missing data:
- **MCAR** (Missing Completely At Random)  
- **MAR** (Missing At Random)  
- **MNAR** (Missing Not At Random)  

### 🧠 Methodology

- Performed EDA to find missing values.  
- Grouped data by attributes like BHK, area type, and price to observe missing patterns.  
- Used visualizations to support logical inferences.  
- Assigned missingness types based on observed dependencies.  

#### Example:
- **Balcony column** may show **MAR** (missing depending on size) or **MNAR** (missing in higher or lower priced homes).  
- **Area Type** missingness is often **MAR**.

### 📈 Tools & Libraries

- `pandas`, `matplotlib`, `seaborn`, `numpy`  
- Jupyter Notebook  

### ✅ Key Insights

- Not all missing data should be treated the same—understanding *why* data is missing helps improve modeling later.  
- Suggested imputation strategies based on missingness types.

---

## 2️⃣ COVID-19 Weekly/Monthly Case Trends - 🦠 U.S. State Time Series

### 📊 Dataset Overview

The COVID-19 dataset includes daily confirmed case counts by state in the United States.

### 🎯 Objective

- Convert daily data to **weekly or monthly trends** for clearer insights.  
- Visualize trends for one selected state (e.g., California, New York).  

### 📅 Methodology

- Converted the `date` column to datetime format using:  
  ```python
  df['date'] = pd.to_datetime(df['date'])
  
- Grouped data by month or week using:
  ```python
  df.resample('M', on='date')['cases'].sum()

- Visualized trends using `sns.lineplot()` for a smooth view of changes over time.

### 📊 Best Visualization Practice
- Line plots are ideal for time series data like COVID trends.
- Bar plots can be used for fewer time points (e.g., monthly totals), but may get cluttered for dense daily data.

### ✅ Insights
- Showed surges and declines in case numbers.
- Helps compare COVID trends over time for individual states.

### 📂 Project Structure
```kotlin
├── data/
│   ├── bangalore_house_price.csv
│   └── us_covid_cases.csv
├── notebooks/
│   ├── missing_data_analysis.ipynb
│   └── covid_cases_visualization.ipynb
├── visuals/
│   └── covid_trend_plot.png
├── README.md
└── requirements.txt

