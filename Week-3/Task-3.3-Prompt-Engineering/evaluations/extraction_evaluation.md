# Extraction Evaluation (order details from emails to JSON)

Model: ChatGPT (exact model version not recorded)
Date: 07 Oct 2026
Test inputs: prompts/extraction_test_inputs.md (E1 to E5, unchanged across versions)
Scoring: 6 points per email (5 fields correct + JSON format with exact keys). Max 30.

## Evaluation sheet

| Category | Version | Prompt | Expected Output | Actual Output | Problems | Improvement |
|----------|---------|--------|-----------------|---------------|----------|-------------|
| Extraction | V1 | `Extract the order details from this email: [EMAIL]` | JSON-style fields: order_id, customer_name, item, quantity, delivery_city; E3 order_id null; E5 quantity 1 | All field values correct. Replies were bullet lists with inconsistent labels. Score 25/30 | No JSON in any reply; labels varied; extra fields in E4 (Receiver) and E5 (prices); E3 said "Not provided" instead of null; E1 had an intro sentence | Asked for JSON with exact keys and nothing else |
| Extraction | V2 | `Extract the order details from this email and return only a JSON object with exactly these keys: order_id, customer_name, item, quantity, delivery_city. Do not write anything outside the JSON.` + email | Same as V1 | 4 of 5 emails fully correct. All 5 were clean JSON with the exact keys. E3 gave null. Score 29/30 | E5: "a green backpack" gave quantity null instead of 1 | Added a rule for "a" or "an" |
| Extraction | V3 | V2 prompt + `If a quantity is written as "a" or "an", use 1.` | Same as V1 | All 5 correct and clean JSON. Score 30/30 | None found in this single run | Keep as final prompt |

## Final extraction prompt

```
Extract the order details from this email and return only a JSON object with exactly these keys: order_id, customer_name, item, quantity, delivery_city. Do not write anything outside the JSON. If a quantity is written as "a" or "an", use 1.

Email:
[EMAIL]
```

## What I learned

- Asking for a fixed JSON format removed the label differences and the extra fields.
- The format instruction also stopped the model from adding unrequested fields (Receiver, prices) without any separate rule.
- The "a" or "an" case was a real failure that only showed up after the format was fixed. One extra rule fixed it.
- The model returned null for the missing order number without being told, but this was not tested on other emails.

## Limitations

- Only one model (ChatGPT) and one run per email.
- Only 5 invented emails, all short and in clear English.
- The "a" or "an" rule was written after seeing the E5 failure, so E5 is no longer an unseen test.
- No repeat runs were done, so consistency across runs is not verified.