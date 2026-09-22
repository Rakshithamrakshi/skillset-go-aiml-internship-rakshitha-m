# Task 1.4 - Two ML Models with Scikit-learn

## Objective
Train and evaluate one regression model and one classification model 
using the full supervised learning workflow: split, preprocess, train 
a baseline, evaluate, and inspect errors.

## Datasets
- **Regression**: California Housing dataset (built into scikit-learn) - 
  predicting median house value
- **Classification**: Cleaned Titanic dataset (reused from Task 1.2) - 
  predicting passenger survival

## Tools Used
- Python 3.11.9
- Pandas, NumPy
- Scikit-learn (Pipeline, ColumnTransformer, LinearRegression, LogisticRegression)
- Jupyter Notebook

## Work Completed

### Regression (House Price Prediction)
- Split data 80/20 before any preprocessing
- Built a Pipeline with StandardScaler + LinearRegression baseline
- Evaluated with MAE (0.53), RMSE (0.75), R² (0.576)
- Inspected worst predictions - identified the dataset's known $500K price 
  cap as a source of model confusion

### Classification (Titanic Survival Prediction)
- Selected relevant features, separated numeric vs categorical columns
- Used stratified train/test split to preserve class balance
- Built a Pipeline with ColumnTransformer (scaling + one-hot encoding) + 
  Logistic Regression baseline
- Evaluated with Accuracy (0.805), Precision (0.793), Recall (0.667), F1 (0.724)
- Analyzed confusion matrix and misclassified examples - found the model 
  struggles with exceptions to the general "male + 3rd class" survival pattern

## Deliverables
- `ml_models.ipynb` - both models, evaluation, and error analysis in one notebook

## Key Learnings
- Why splitting before preprocessing prevents data leakage
- How Pipeline and ColumnTransformer keep preprocessing consistent and reusable
- Why a single metric (like accuracy) can be misleading, especially with 
  imbalanced classes
- How inspecting specific errors (not just aggregate metrics) reveals real 
  model limitations and dataset quirks

## Submission Status
Status: Completed
Submitted On: 22 September 2026