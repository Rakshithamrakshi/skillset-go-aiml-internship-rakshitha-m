from predict_sms import predict_sms

normal = [
    "Hey, are we still meeting at 6 for dinner?",
    "WINNER! You have been selected for a prize. Text CLAIM to 80000 now to collect your reward.",
    "Reminder: your appointment is tomorrow at 10am.",
    "£££ FREE £££",
    "ok",
    "Café at 5? 😊",
    "word " * 500,
]

print("--- normal inputs ---")
for t in normal:
    r = predict_sms(t)
    assert r["label"] in ("spam", "ham") and 0.0 <= r["spam_probability"] <= 1.0
    print(f"{r['label']:5} {r['spam_probability']:.4f}  {ascii(t[:60])}")

print("--- invalid inputs (should raise) ---")
for bad, expected in [("", ValueError), ("   ", ValueError), (None, TypeError), (123, TypeError)]:
    try:
        predict_sms(bad)
    except expected as err:
        print("OK:", ascii(bad), "->", type(err).__name__, "-", err)
    else:
        raise SystemExit(f"NOT RAISED for {ascii(bad)}")

print("All checks passed.")