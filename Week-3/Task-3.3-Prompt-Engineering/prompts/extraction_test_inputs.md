# Extraction Test Inputs (fixed for all prompt versions)

Category: Extraction (order details from emails to JSON)
All emails and names are invented for this exercise. No real personal data.

## Fields to extract

- order_id (text, or null if missing)
- customer_name (text, the person placing the order)
- item (text)
- quantity (whole number)
- delivery_city (text)

## Emails

**E1.**
Hi team, I would like to place an order. Please send 2 blue notebooks to Pune. My name is Meera Iyer. Order reference: ORD-1001. Thanks!

**E2.**
Hello, this is Karan Mehta. Order ORD-1002. I want four steel water bottles delivered to Jaipur. Actually, please make it three instead of four.

**E3.**
Hi, I am ordering 5 desk lamps for delivery to Mysuru. Name: Divya Rao. I do not have an order number yet.

**E4.**
Order ORD-1004 from Imran Sheikh: 10 USB cables to Chennai. My friend Rohan Das will receive the parcel.

**E5.**
Hello, I am Sneha Pillai (ORD-1005). Please deliver a green backpack to Kochi. The price quoted last month was Rs 1,200, but I understand it may have changed.

## Expected answers (written BEFORE running any prompt)

| ID | order_id | customer_name | item | quantity | delivery_city | Trap |
|----|----------|---------------|------|----------|---------------|------|
| E1 | ORD-1001 | Meera Iyer | blue notebooks | 2 | Pune | none (easy baseline) |
| E2 | ORD-1002 | Karan Mehta | steel water bottles | 3 | Jaipur | quantity was changed in the email (3, not 4) |
| E3 | null | Divya Rao | desk lamps | 5 | Mysuru | order number is missing, so it must be null, not invented |
| E4 | ORD-1004 | Imran Sheikh | USB cables | 10 | Chennai | Rohan Das is the receiver, not the customer |
| E5 | ORD-1005 | Sneha Pillai | green backpack | 1 | Kochi | "a" means 1, and the price must be ignored |

Item matching: singular or plural is accepted (for example "blue notebook" = "blue notebooks").

## Scoring criteria (written before running)

- Each of the 5 fields correct: 1 point each, so 5 points per email.
- Format rule: the reply contains one JSON object using exactly these 5 key names (order_id, customer_name, item, quantity, delivery_city), with no explanation text outside the JSON. A code block fence around the JSON is allowed. 1 point per email.
- Maximum per email: 6 points. Maximum per full run of 5 emails: 30 points.

## Run log

- Model name: ChatGPT
- Date: 07 Oct 2026