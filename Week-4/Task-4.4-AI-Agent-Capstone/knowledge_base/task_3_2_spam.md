# Task 3.2 - SMS Spam Classifier (TensorFlow/Keras)

Skill Set Go EduTech AI/ML Internship, Week 3.

## Problem
Classify an SMS as spam or ham from its text. A useful prediction catches most spam
(recall) without blocking real messages (precision). Spam is the minority class, so
accuracy alone is misleading: predicting "ham" for everything scores 87.3% on the test set.

## Data
SMS Spam Collection (UCI), 5,574 messages (4,827 ham, 747 spam). See `data/README.md`
for the download steps, citation and terms. The raw file is not stored in this repo.
- 403 exact duplicate rows removed before splitting (no text carried both labels): 5,171 messages (4,518 ham, 653 spam).
- Stratified 80/20 split, random_state=42: 4,136 train / 1,035 test (131 spam).
- 15% of train held out for validation: 3,515 train (444 spam) / 621 validation (78 spam).
- Leakage check: 0 messages appear in both train and test.

## Models
1. Always predict ham (reference).
2. TF-IDF (word 1-2 grams) + logistic regression, trained on 4,136 messages, and again on the same 3,515 as Keras for a like-for-like comparison.
3. Keras: TextVectorization (5,000 words, 50 tokens) -> Embedding(16) -> average pooling ->
   Dense(16, ReLU) -> Dropout(0.3) -> sigmoid. 80,289 parameters. Adam (lr 0.001), binary
   cross-entropy, batch size 32, early stopping on validation loss (patience 5).
   Best epoch 12 of 17; about 10.5-11.0 s on CPU (two runs with the same code).
   Decision cutoff 0.5, fixed before the test set was used.

## Test results (1,035 messages, 131 spam)
| Model | Accuracy | Spam precision | Spam recall | Spam F1 | Missed spam | False alarms |
|---|---|---|---|---|---|---|
| Always predict ham | 0.8734 | 0.0000 | 0.0000 | 0.0000 | 131 | 0 |
| TF-IDF + LR (4,136 train) | 0.9623 | 0.9894 | 0.7099 | 0.8267 | 38 | 1 |
| TF-IDF + LR (3,515 train) | 0.9614 | 0.9892 | 0.7023 | 0.8214 | 39 | 1 |
| Keras (3,515 train) | 0.9681 | 0.8828 | 0.8626 | 0.8726 | 18 | 15 |

Keras catches more spam (113 vs 92 at the same training size) but raises far more false
alarms (15 vs 1): it trades precision for recall, so it is not simply better. Validation
looked better than test (2 false alarms among 543 ham vs 15 among 904), because the
validation set is small and also chose the stopping epoch.

## Files
| Path | Purpose |
|---|---|
| `notebooks/sms_spam_classifier.ipynb` | Full workflow: EDA, split, baselines, Keras model, evaluation |
| `predict_sms.py` | Loads the saved model and predicts one message |
| `test_predict_sms.py` | Normal and invalid-input checks for the prediction function |
| `model/` | `sms_spam_keras.weights.h5`, `vocabulary.json`, `model_config.json` |
| `results/` | Charts and JSON metrics |

## How to run
1. Install the packages from `../Task-3.1-TensorFlow-Keras/requirements.txt` (the same versions were used; torch is not needed here).
2. Download the data as described in `data/README.md`.
3. Predict: `python Week-3/Task-3.2-Text-Classification/predict_sms.py "your message"`
4. Checks: `python Week-3/Task-3.2-Text-Classification/test_predict_sms.py`
5. Re-running the notebook retrains the model and overwrites the files in `model/`; results may differ slightly.

TensorFlow prints oneDNN and GPU warnings on startup. They are normal on CPU/Windows.

## Limitations
- Only 131 spam messages in the test set: recall is uncertain by roughly +/- 6 percentage points (rough estimate), so small differences between models are weak evidence.
- Only exact duplicates were removed; near-duplicates were not measured.
- Spam and ham come from different sources (per the dataset's readme), so the model may partly learn source or style. Untested.
- The default text cleaning lowercases and strips punctuation; signals such as the pound sign and exclamation marks may be lost (not tested).
- Some raw messages contain damaged characters; not counted or cleaned.
- Confidently wrong on some input: 6 of the 15 false alarms had spam probability above 0.9, and a message of one word repeated 500 times was labeled spam at 0.9999.
- The model could not be saved as one `.keras` file because of a Windows encoding error (probably a rare character in the vocabulary), so weights and vocabulary are saved separately; they rebuild the identical model (max probability difference 0.0).
- Single run, single split; not a production spam filter.
- `model/vocabulary.json` holds the 5,000 word tokens learned from the training messages, including a few dozen phone-number-like tokens (34 matched a UK-number pattern) that appear in the public dataset; they were left unchanged so the saved model stays identical to the tested one. Masking numbers before training is a planned improvement.

## Future improvements
Tune the cutoff or class weights on validation data only; character n-grams; cross-validation; remove near-duplicates; clean encoding issues; try a larger and more recent dataset.