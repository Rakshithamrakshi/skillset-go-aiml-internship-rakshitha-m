# Extraction V2 Runs

Model: ChatGPT
Date: 07 Oct 2026
Change from V1: asked for only a JSON object with exactly the keys order_id, customer_name, item, quantity, delivery_city, and nothing outside the JSON.

## E1
Output:
{"order_id":"ORD-1001","customer_name":"Meera Iyer","item":"blue notebooks","quantity":2,"delivery_city":"Pune"}


## E2
Output:
{"order_id":"ORD-1002","customer_name":"Karan Mehta","item":"steel water bottles","quantity":3,"delivery_city":"Jaipur"}


## E3
Output:
{
"order_id": null,
"customer_name": "Divya Rao",
"item": "desk lamps",
"quantity": 5,
"delivery_city": "Mysuru"
}


## E4
Output:
{"order_id":"ORD-1004","customer_name":"Imran Sheikh","item":"USB cables","quantity":10,"delivery_city":"Chennai"}


## E5
Output:
{"order_id":"ORD-1005","customer_name":"Sneha Pillai","item":"green backpack","quantity":null,"delivery_city":"Kochi"}


## V2 Scorecard

Model: ChatGPT
Date: 07 Oct 2026

| ID | order_id | customer_name | item | quantity | delivery_city | Format (JSON, exact keys) | Score |
|----|----------|---------------|------|----------|---------------|---------------------------|-------|
| E1 | Y | Y | Y | Y | Y | Y | 6/6 |
| E2 | Y | Y | Y | Y | Y | Y | 6/6 |
| E3 | Y (null) | Y | Y | Y | Y | Y | 6/6 |
| E4 | Y | Y | Y | Y | Y | Y | 6/6 |
| E5 | Y | Y | Y | N (null, expected 1) | Y | Y | 5/6 |

**V2 total score: 29 / 30**

Problems found:
- E5: "a green backpack" was returned as quantity null instead of 1. The model did not treat "a" as one.
