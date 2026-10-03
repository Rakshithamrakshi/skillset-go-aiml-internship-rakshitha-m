# Task 3.1: PyTorch vs TensorFlow/Keras Comparison Notes

## Setup (identical for both)
- Dataset: California Housing (20,640 rows, 8 features), regression
- Split: 80/20, random_state=42 (16,512 train / 4,128 test)
- Scaling: StandardScaler on features only, fit on training data
- Architecture: 8 -> 32 -> 16 -> 1, ReLU (833 parameters)
- Loss/optimizer: MSE / Adam, lr=0.001; batch size 32; 50 epochs
- Hardware: CPU only (TensorFlow has no native-Windows GPU support)
- Software: TensorFlow 2.21.0, Keras 3.15.1, PyTorch 2.14.0, Python 3.11.9

## Results (from results/pytorch_results.json and keras_results.json)
| Metric | PyTorch (re-run) | TensorFlow/Keras |
|---|---|---|
| Test MSE | 0.2877 | 0.2916 |
| Test MAE | 0.3597 | 0.3680 |
| Test RMSE | 0.5364 | 0.5400 |
| Test R-squared | 0.7805 | 0.7774 |
| Train MSE (final weights) | 0.2697 | 0.2683 |
| Training time (s) | 39.0 | 70.6 |

Week 2 reference (original notebook, no seed, no timer): final-epoch running train
loss 0.2745, test MSE 0.2921. Training time, MAE and R-squared were not recorded in Week 2.

## Findings
1. Both frameworks reach very similar accuracy. Test MSE differs by 0.0039 (about 1.4%).
2. The two PyTorch runs (Week 2: 0.2921, re-run: 0.2877) differ by 0.0044, which is
   as large as the PyTorch-vs-Keras gap. The gap is therefore within run-to-run variation
   observed here, and cannot be attributed to the framework.
3. Neither model shows strong overfitting: train and test MSE are close for both
   (PyTorch 0.2697 vs 0.2877, Keras 0.2683 vs 0.2916). Keras shows a slightly larger gap.
4. Training took 39.0 s in PyTorch and 70.6 s in Keras in this setup. Each was run once,
   so this is a measured result for this machine and not a general claim about speed.

## Possible sources of difference (not individually tested)
- Weight initialization: Keras defaults to Glorot uniform with zero biases; PyTorch uses
  its own default scheme.
- Batch order: shuffling differs between the frameworks even with the same seed value.
- Randomness: one run per framework.
- Numerics: TensorFlow reported oneDNN custom operations, which can change floating-point results slightly.
- Timing: Keras fit() and the PyTorch loop have different per-step overheads. Both
  evaluated on the test set after each epoch.

## Keras workflow vs PyTorch (what I learned)
- Keras: Sequential model, compile(loss, optimizer, metrics), fit() runs the whole loop.
- PyTorch: nn.Module, manual loop (zero_grad, forward, loss, backward, step).
- Keras needs less code, PyTorch makes every training step visible.

## Limitations
- One run per framework, no repeated seeds, so no confidence interval.
- Week 2 model was not seeded, so the original run cannot be reproduced exactly.
- Test data was used for per-epoch monitoring only, not for tuning.
- Simple tabular task; conclusions may not transfer to other model types.

## Next steps
- Repeat each framework with several seeds and compare mean and spread.
- Use identical weight initialization in both frameworks to isolate its effect.
