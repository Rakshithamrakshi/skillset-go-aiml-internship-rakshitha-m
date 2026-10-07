"""Predict whether an SMS is spam or ham with the saved Keras model.

Usage (repo root, venv active):
    python Week-3/Task-3.2-Text-Classification/predict_sms.py "your message here"
"""
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

import tensorflow as tf
from tensorflow import keras

MODEL_DIR = Path(__file__).resolve().parent / "model"
_MODEL = None


def _load_model():
    with open(MODEL_DIR / "model_config.json", encoding="utf-8") as f:
        cfg = json.load(f)
    with open(MODEL_DIR / "vocabulary.json", encoding="utf-8") as f:
        vocab = json.load(f)

    vectorizer = keras.layers.TextVectorization(
        max_tokens=cfg["max_tokens"], output_mode="int",
        output_sequence_length=cfg["seq_len"],
    )
    vectorizer.set_vocabulary(vocab)

    model = keras.Sequential([
        keras.layers.Input(shape=(1,), dtype="string"),
        vectorizer,
        keras.layers.Embedding(input_dim=cfg["max_tokens"],
                               output_dim=cfg["embedding_dim"], mask_zero=True),
        keras.layers.GlobalAveragePooling1D(),
        keras.layers.Dense(16, activation="relu"),
        keras.layers.Dropout(0.3),
        keras.layers.Dense(1, activation="sigmoid"),
    ])
    model.load_weights(str(MODEL_DIR / "sms_spam_keras.weights.h5"))
    return model, cfg["threshold"]


def predict_sms(text):
    """Return {'label': 'spam'|'ham', 'spam_probability': float} for one message."""
    global _MODEL
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text.strip():
        raise ValueError("text is empty")
    if _MODEL is None:
        _MODEL = _load_model()
    model, threshold = _MODEL
    batch = tf.constant([text], dtype=tf.string)[:, tf.newaxis]
    prob = float(model.predict(batch, verbose=0).ravel()[0])
    return {"label": "spam" if prob >= threshold else "ham",
            "spam_probability": round(prob, 4)}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python predict_sms.py "message text"')
        sys.exit(1)
    try:
        print(predict_sms(" ".join(sys.argv[1:])))
    except (ValueError, TypeError) as err:
        print("Error:", err)
        sys.exit(1)