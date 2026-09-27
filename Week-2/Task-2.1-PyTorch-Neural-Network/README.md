# Task 2.1 - Neural Network in PyTorch

## Objective
Implement a feed-forward neural network in PyTorch, covering tensors, datasets,
dataloaders, loss functions, and the training loop.

## Tools Used
- Python
- PyTorch
- NumPy
- Pandas
- Matplotlib
- scikit-learn (train/test split, scaling)
- Jupyter Notebook

## Dataset
California Housing dataset (built into scikit-learn) — predicting median house value
from 8 numeric features (income, rooms, location, etc.).

## Work Completed
1. Loaded and inspected the California Housing dataset
2. Split data into train/test sets and scaled features using StandardScaler
3. Converted data into PyTorch tensors and built a custom Dataset + DataLoader
4. Defined a feed-forward neural network (8 → 32 → 16 → 1) using nn.Module
5. Trained the model for 50 epochs using MSE loss and the Adam optimizer
6. Evaluated on the test set and compared train vs test loss
7. Visualized the training loss curve
8. Compared sample predictions against actual values

## Results
- Final training loss (MSE): ~0.27
- Test loss (MSE): ~0.29
- Train and test loss are close, indicating the model generalizes reasonably well
  and is not overfitting

## Deliverables
- PyTorch training notebook: `notebooks/pytorch_nn.ipynb`
- Loss curve screenshot: `screenshots/Rakshitha_Week2_Task2.1_LossCurve.png`

## Key Learnings
- How to build a PyTorch Dataset and DataLoader for batching data
- How to define a neural network using nn.Module and nn.Sequential
- The role of activation functions (ReLU) in enabling non-linear learning
- The full training loop: zero_grad, forward pass, loss calculation, backward pass, optimizer step
- Why scaling features and using train/test splits matters for fair evaluation
- How to interpret a loss curve and compare train vs test loss to check for overfitting

## Submission Status
Status: Completed
Submitted On: 27 September 2026