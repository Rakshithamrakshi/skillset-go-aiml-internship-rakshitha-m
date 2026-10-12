# Task 2.3 - Hyperparameter Experimentation

## Objective
Run controlled experiments varying optimizers, learning rates, batch sizes, and
epochs on a PyTorch neural network; compare outcomes and select a final configuration.

## Tools Used
- Python
- PyTorch
- NumPy
- Pandas
- Matplotlib
- scikit-learn

## Dataset
California Housing dataset (same setup as Task 2.1) — reused to isolate the effect
of hyperparameters from the effect of the data itself.

## Work Completed
1. Built a fixed data pipeline (same split, scaling, and random seed for every run)
2. Wrote a reusable training function to run experiments with different hyperparameters
3. Group A: tested learning rates 0.01, 0.001, 0.0001 (best: 0.001)
4. Group B: tested optimizers Adam, SGD, RMSprop (best: Adam)
5. Group C: tested batch sizes 16, 32, 64, 128 (best: 32)
6. Group D: tested epoch counts 10, 30, 60, checking for overfitting (best: 30, with
   60 as a marginal but more expensive alternative)
7. Built a master comparison table of all 13 experiments, sorted by test loss
8. Plotted loss curves for each group to visually confirm the numerical results
9. Selected and justified a final configuration

## Results
Final configuration: **Adam, learning rate 0.001, batch size 32, 30 epochs**
- Final train loss: 0.2780
- Final test loss: 0.2915
- A longer run (60 epochs) achieved a marginally lower test loss (0.2807) but took
  roughly 50% longer to train, so 30 epochs was chosen as the better time/accuracy
  trade-off.
- No overfitting observed even at 60 epochs — train and test loss stayed close
  together throughout training.

## Deliverables
- Experiment notebook: `notebooks/hyperparameter_experiments.ipynb`
- Master comparison table (13 experiments) inside the notebook
- Screenshots: `screenshots/Rakshitha_Week2_Task2.3_GroupA_LearningRate.png`,
  `screenshots/Rakshitha_Week2_Task2.3_GroupB_Optimizer.png`,
  `screenshots/Rakshitha_Week2_Task2.3_GroupC_BatchSize.png`,
  `screenshots/Rakshitha_Week2_Task2.3_GroupD_Epochs.png`

## Key Learnings
- How to design controlled experiments that change one hyperparameter at a time
- Too small a learning rate causes underfitting; too large can cause instability
- Optimizer choice interacts with learning rate — SGD underperformed Adam/RMSprop
  specifically at this learning rate, not necessarily in general
- Smaller batch sizes gave better accuracy but took longer to train, per epoch budget
- More epochs kept helping, but with diminishing returns and no overfitting observed
  within the range tested
- The "best" configuration depends on what you're optimizing for (pure accuracy vs
  accuracy per unit of training time), not just the single lowest loss number

## Submission Status
Status: Completed
Submitted On: 27 September 2026