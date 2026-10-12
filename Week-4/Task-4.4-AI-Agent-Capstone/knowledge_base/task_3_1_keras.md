# Task 3.1 - Neural Network in TensorFlow/Keras

Skill Set Go EduTech AI/ML Internship, Week 3.

## Objective
Build and train a feed-forward neural network in TensorFlow/Keras and compare it fairly
with the Week 2 PyTorch model (Task 2.1) on the same data.

## Dataset and task
California Housing (built into scikit-learn): 20,640 rows, 8 numeric features.
Regression: predict median house value.

## Setup (identical in both frameworks)
- 80/20 train/test split, random_state=42 (16,512 train / 4,128 test)
- StandardScaler on features only, fit on training data
- Architecture 8 -> 32 -> 16 -> 1 with ReLU (833 parameters)
- MSE loss, Adam (lr=0.001), batch size 32, 50 epochs
- CPU only, Python 3.11.9, TensorFlow 2.21.0, Keras 3.15.1, PyTorch 2.14.0

## Results
| Metric | PyTorch (re-run) | TensorFlow/Keras |
|---|---|---|
| Test MSE | 0.2877 | 0.2916 |
| Test MAE | 0.3597 | 0.3680 |
| Test RMSE | 0.5364 | 0.5400 |
| Test R-squared | 0.7805 | 0.7774 |
| Training time (s) | 39.0 | 70.6 |

Week 2 original PyTorch run (unseeded): test MSE 0.2921.

The PyTorch-vs-Keras gap (0.0039) is no larger than the gap between two PyTorch runs
(0.0044), so it cannot be attributed to the framework. Each setup was run once.
See `results/comparison_notes.md` for the full discussion, possible causes and limitations.

## Files
| Path | Purpose |
|---|---|
| `notebooks/tensorflow_keras_nn.ipynb` | Keras model: data, training, evaluation, comparison |
| `notebooks/pytorch_rerun_for_comparison.ipynb` | Seeded, timed PyTorch re-run with the same metrics |
| `results/keras_results.json`, `pytorch_results.json` | Raw saved metrics |
| `results/comparison_table.csv` | Comparison table built from the two JSON files |
| `results/comparison_notes.md` | Written comparison notes |
| `results/keras_loss_curve.png` | Keras train vs test loss curve |
| `requirements.txt` | Package versions used |

## How to run
1. Activate the virtual environment and install: `pip install -r requirements.txt`
2. Open `notebooks/tensorflow_keras_nn.ipynb` and run the cells from top to bottom.
3. Run `notebooks/pytorch_rerun_for_comparison.ipynb` the same way to regenerate the PyTorch results.
4. Training takes about one minute per notebook on CPU. Re-running can change the numbers slightly.

## Limitations
- One run per framework, no repeated seeds.
- Simple tabular task, so conclusions may not transfer to other models.
- Weight initialization and batch ordering differ between the frameworks.