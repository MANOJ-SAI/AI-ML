# Pandas Data Analysis & Data Manipulation  

This directory contains my **Pandas learning notebook**, implemented in **Google Colab** and pushed to GitHub.  
This notebook covers **Pandas fundamentals, data cleaning, filtering, transformation, and aggregation**, which are **essential for Data Science, Machine Learning, and Exploratory Data Analysis (EDA)**.

Pandas is one of the most important libraries for handling structured data in real-world ML projects.

---

## Topics Covered  

---

### 1. Creating & Loading Data (MUST KNOW)
- `pd.read_csv()`
- `pd.read_json()`
- `pd.DataFrame()`

#### Inspecting Data
- `df.head()`
- `df.tail()`
- `df.shape`
- `df.columns`
- `df.dtypes`
- `df.info()`

📌 **Purpose:** Understand the structure, size, and types of your dataset before analysis.

---

### 2. Selecting Data (CORE CONCEPT)

#### Column Selection
- `df['column']`
- `df[['col1', 'col2']]`

#### Row Selection
- `df.iloc[]` (Index-based selection)
- `df.loc[]` (Label-based selection)

#### Examples
- `df.iloc[0]` → First row  
- `df.loc[5]` → Row with index 5  
- `df.loc[:, 'salary']` → Entire salary column  

📌 **Very Important:** Used for feature selection in ML models.

---

### 3. Filtering Data (MOST IMPORTANT)

#### Conditional Filtering
- `df[df['age'] > 30]`
- `df[df['salary'] >= 50000]`

#### Multiple Conditions
- `df[(df['age'] > 25) & (df['salary'] > 60000)]`
- `df[(df['city'] == 'Bangalore') | (df['city'] == 'Hyderabad')]`

#### Using `isin()`
- `df[df['city'].isin(['Bangalore', 'Hyderabad'])]`

#### Using `between()`
- `df[df['age'].between(25, 40)]`

📌 **Used in every Data Science project.**

---

### 4. Handling Missing Data (DATA CLEANING)
- `df.isnull()`
- `df.isnull().sum()`
- `df.notnull()`
- `df.dropna()`
- `df.fillna(0)`
- `df.fillna(df.mean())`

📌 Replaces manual Python cleaning logic. Critical before training ML models.

---

### 5. Sorting & Ordering
- `df.sort_values(by='salary')`
- `df.sort_values(by='salary', ascending=False)`
- `df.sort_index()`

📌 Used in reporting and data analysis.

---

### 6. Data Transformation (Feature Engineering)

#### Apply Functions
- `df.apply()`
- `df.applymap()`
- `df.map()`

#### Example
```python
df['salary_lakh'] = df['salary'].apply(lambda x: x / 100000)
```

📌 Important for creating new ML features.

---

### 7. Aggregation & Statistics (DATA SCIENCE CORE)

#### Basic Statistics
- `df.mean()`
- `df.median()`
- `df.sum()`
- `df.min()`
- `df.max()`
- `df.count()`
- `df.describe()`

#### Grouping & Aggregation
- `df.groupby('department').mean()`
- `df.groupby('city')['salary'].sum()`

📌 Heavily used in Exploratory Data Analysis (EDA).

---

### 8. Renaming & Modifying Columns
- `df.rename(columns={'old': 'new'})`
- `df.drop(columns=['column'])`
- `df.astype(int)`

📌 Necessary before building ML models.

---

### 9. Index Handling
- `df.set_index('id')`
- `df.reset_index()`

📌 Important for joins, merging, and time-series analysis.

---

### 10. Exporting Data
- `df.to_csv()`
- `df.to_json()`
- `df.to_excel()`

📌 Used to save processed datasets for reporting or ML pipelines.

---

## Why This Repository is Important

This notebook demonstrates:

- Real-world data cleaning workflow  
- Filtering & transformation techniques  
- Feature engineering basics  
- Grouping & statistical analysis  
- Data preparation before Machine Learning  

Pandas is the backbone of **Data Science projects**, and mastering these concepts is essential for becoming a Machine Learning Engineer or Data Analyst.

---

## Tools Used
- Python  
- Pandas  
- Google Colab  
- Git & GitHub  
