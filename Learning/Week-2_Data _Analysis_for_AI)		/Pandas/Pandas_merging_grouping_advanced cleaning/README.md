# Pandas Advanced Operations – Merging, Grouping & Data Cleaning  

This directory contains my **Week-2 Pandas learning notebook**, implemented in **Google Colab** and pushed to GitHub.  

This module focuses on:

- Data Merging & Combining  
- Grouping & Aggregation (Core Data Science Skill)  
- Advanced Data Cleaning  
- Feature Engineering  
- Final Data Validation  

These concepts are heavily used in **real-world Data Science and Machine Learning projects**.

---

# 1. Merging Data (VERY IMPORTANT)

## 🔹 Core Functions
- `pd.merge()`
- `df.join()`
- `pd.concat()`

---

## 🔹 `pd.merge()` (MOST IMPORTANT)

```python
pd.merge(
    left_df,
    right_df,
    on='column',
    how='inner'
)
```

### `how` Types (MUST KNOW)
- `how='inner'`
- `how='left'`
- `how='right'`
- `how='outer'`

### Example
```python
pd.merge(df1, df2, on='id', how='left')
```

📌 **90% of real-world projects use `merge()`**

---

### 🔹 Merge on Different Column Names
```python
pd.merge(df1, df2, left_on='emp_id', right_on='id')
```

---

## 🔹 `pd.concat()` (Stacking Data)

```python
pd.concat([df1, df2])
pd.concat([df1, df2], axis=1)
```

### Used When:
- Combining same-structure datasets  
- Appending data  
- Horizontal column joining  

---

# 2. Grouping Data (`groupby`) – DATA SCIENCE CORE

## 🔹 Basic Grouping
```python
df.groupby('department')
```

---

## 🔹 Aggregations
```python
df.groupby('department').mean()
df.groupby('city')['salary'].sum()
df.groupby('team').count()
```

---

## 🔹 Multiple Aggregations
```python
df.groupby('department').agg({
    'salary': ['mean', 'max'],
    'age': 'mean'
})
```

📌 **This is interview gold.**

---

## 🔹 Groupby + Filtering
```python
df.groupby('department').filter(
    lambda x: x['salary'].mean() > 50000
)
```

---

# 3. Advanced Data Cleaning (VERY IMPORTANT)

## 🔹 Detect Missing Values
```python
df.isnull()
df.isnull().sum()
```

---

## 🔹 Advanced `fillna()`
```python
df.fillna(method='ffill')
df.fillna(method='bfill')
df.fillna(df.mean())
```

---

## 🔹 Remove Duplicates
```python
df.duplicated()
df.drop_duplicates()
df.drop_duplicates(subset=['id'])
```

---

## 🔹 Fix Data Types (CRITICAL before ML)
```python
df.astype(int)
df['date'] = pd.to_datetime(df['date'])
```

---

## 🔹 String Cleaning (VERY COMMON)
```python
df['name'].str.lower()
df['name'].str.strip()
df['name'].str.replace(" ", "")
```

---

## 🔹 Handling Outliers (Basic Filtering)
```python
df[df['salary'] < 1000000]
```

(Simple filtering is enough at this stage.)

---

# 4. Column Engineering (Feature Preparation)

```python
df['new_col'] = df['salary'] / 100000
df['is_high_salary'] = df['salary'] > 70000
```

📌 These features directly feed Machine Learning models.

---

# 5. Advanced Sorting & Indexing

```python
df.sort_values(by=['department', 'salary'])
df.reset_index(drop=True)
df.set_index('id')
```

---

# 6. Final Data Validation (IMPORTANT)

```python
df.shape
df.info()
df.describe()
```

Final validation ensures:
- No unexpected missing values  
- Correct data types  
- Clean dataset before ML modeling  

---

# Module Summary (Week-2)

In this module, I covered:

- Data Merging (Real-world datasets combination)  
- Grouping & Aggregation (Core Data Science skill)  
- Advanced Cleaning Techniques  
- Feature Engineering  
- Final Dataset Validation  

These topics are sufficient for mastering **Pandas Merging, Grouping & Advanced Cleaning**, which form a critical part of the Data Science workflow.

---

## Tools Used
- Python  
- Pandas  
- Google Colab  
- Git & GitHub  