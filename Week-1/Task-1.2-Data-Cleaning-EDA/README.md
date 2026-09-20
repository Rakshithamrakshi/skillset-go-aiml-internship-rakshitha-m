# Task 1.2 - Data Cleaning & EDA

## Objective
Clean and analyze a real-world dataset (Titanic passenger data) using 
NumPy, Pandas, and Matplotlib. Identify data quality issues, make 
documented cleaning decisions, and extract meaningful insights through 
visualization.

## Dataset
Titanic passenger dataset (891 rows, 12 columns) - a classic real-world 
dataset with genuine missing values and mixed data types, sourced from 
a public GitHub repository.

## Tools Used
- Python 3.11.9
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook (VS Code)

## Work Completed
1. Loaded the dataset and inspected shape, columns, data types, and 
   summary statistics
2. Identified missing values: Age (177), Embarked (2), Cabin (687, ~77%)
3. Checked for duplicate rows (none found) and inconsistent category values
4. Cleaned the data:
   - Filled missing `Age` with the median (robust to outliers)
   - Filled missing `Embarked` with the mode (only 2 rows affected)
   - Dropped `Cabin` column entirely (77% missing, unreliable to fill)
5. Saved the cleaned dataset separately (`dataset/titanic_cleaned.csv`), 
   keeping the original data untouched
6. Created 3 visualizations with written observations:
   - Survival rate by gender
   - Survival rate by passenger class
   - Age distribution (including a noted limitation from median imputation)
7. Summarized key findings at the end of the notebook

## Deliverables
- `notebook.ipynb` - full cleaning and EDA process with outputs
- `dataset/titanic_cleaned.csv` - cleaned dataset

## Key Learnings
- Why median (not mean) is safer for filling missing numeric data with outliers
- How to decide between filling vs. dropping a column based on missing percentage
- That imputation strategies can introduce visible artifacts (e.g. artificial 
  spikes) that should be honestly documented, not hidden
- How working directory paths work differently in Jupyter notebooks vs 
  standalone Python scripts

## Submission Status
Status: Completed
Submitted On: 20 September 2026