# Extraction V1 Runs

Model: ChatGPT
Date: 07 Oct 2026
Prompt used: Extract the order details from this email: [EMAIL]

## E1
Output:
Here are the extracted order details:

* **Customer:** Meera Iyer
* **Order Reference:** ORD-1001
* **Item:** Blue notebooks
* **Quantity:** 2
* **Delivery Location:** Pune


## E2
Output:
* **Name:** Karan Mehta
* **Order Reference:** ORD-1002
* **Item:** Steel water bottles
* **Quantity:** 3
* **Delivery City:** Jaipur


## E3
Output:
* **Customer Name:** Divya Rao
* **Item:** Desk lamps
* **Quantity:** 5
* **Delivery Location:** Mysuru
* **Order Number:** Not provided / Not available yet


## E4
Output:
* **Order Number:** ORD-1004
* **Customer:** Imran Sheikh
* **Item:** USB cables
* **Quantity:** 10
* **Delivery City:** Chennai
* **Receiver:** Rohan Das


## E5
Output:
* **Customer:** Sneha Pillai
* **Order ID:** ORD-1005
* **Item:** Green backpack
* **Quantity:** 1
* **Delivery location:** Kochi
* **Quoted price:** ₹1,200 (last month)
* **Current price:** Not confirmed; may have changed

## V1 Scorecard

Model: ChatGPT
Date: 07 Oct 2026

| ID | order_id | customer_name | item | quantity | delivery_city | Format (JSON, exact keys) | Score |
|----|----------|---------------|------|----------|---------------|---------------------------|-------|
| E1 | Y | Y | Y | Y | Y | N | 5/6 |
| E2 | Y | Y | Y | Y | Y | N | 5/6 |
| E3 | Y (said "Not provided", not null) | Y | Y | Y | Y | N | 5/6 |
| E4 | Y | Y | Y | Y | Y | N | 5/6 |
| E5 | Y | Y | Y | Y | Y | N | 5/6 |

**V1 total score: 25 / 30**

Problems found:
- No reply was a JSON object; all were bullet lists with inconsistent labels (Customer / Name, Order Reference / Order ID / Order Number, Delivery Location / City).
- E1 started with an explanation sentence.
- E4 added an unrequested "Receiver" field. E5 added unrequested "Quoted price" and "Current price" fields.
- E3 wrote "Not provided / Not available yet" instead of null.