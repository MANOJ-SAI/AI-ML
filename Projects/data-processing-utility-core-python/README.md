# Python Mini Project – Data Processing Utility for AI/ML

## Description
This mini project demonstrates core Python programming concepts
used in AI/ML data pipelines. The project simulates real-world data
generation, loading, cleaning, and saving using object-oriented
design and file handling.

The project focuses on preparing clean data before it is used
for machine learning models.

---

## Project Structure

- dataset_generator.py – Generates synthetic CSV data with missing values
- data_loader.py – Loads CSV data using Python standard library
- data_processor.py – Cleans data by removing incomplete records
- main.py – Orchestrates the complete workflow
- input_data.csv – Raw generated dataset
- processed_data.csv – Cleaned output dataset
- requirements.txt – Project dependencies

---

## Key Concepts Covered

- Python OOP (classes, objects, constructors)
- File handling using csv module
- Data cleaning (handling missing values)
- Modular programming
- Basic data preprocessing for AI/ML pipelines

---

## Technologies Used

- Python
- csv module
- faker (for synthetic data generation)

---

## Workflow

1. Generate synthetic dataset with missing values
2. Load CSV data into Python
3. Remove records with empty or null fields
4. Save cleaned data into a new CSV file

---

## ️ How to Run the Project

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script:
    ```bash
   python main.py
    ```



## Outcome

- Built a reusable data preprocessing utility
- Gained hands-on experience with Python OOP
- Prepared foundation for Data Science and AI/ML workflows

---

## Future Enhancements

- Replace csv logic with pandas
- Add statistical summaries
- Integrate machine learning models