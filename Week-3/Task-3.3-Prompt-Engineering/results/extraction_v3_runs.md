# Extraction V3 Runs

Model: ChatGPT
Date: 07 Oct 2026
Change from V2: added the rule: If a quantity is written as "a" or "an", use 1.

## E1
Output:
{"order_id":"ORD-1001","customer_name":"Meera Iyer","item":"blue notebooks","quantity":2,"delivery_city":"Pune"}


## E2
Output:
{
"order_id": "ORD-1002",
"customer_name": "Karan Mehta",
"item": "steel water bottles",
"quantity": 3,
"delivery_city": "Jaipur"
}


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
{"order_id":"ORD-1005","customer_name":"Sneha Pillai","item":"green backpack","quantity":1,"delivery_city":"Kochi"}


## V3 Scorecard

Model: ChatGPT
Date: 07 Oct 2026

| ID | order_id | customer_name | item | quantity | delivery_city | Format (JSON, exact keys) | Score |
|----|----------|---------------|------|----------|---------------|---------------------------|-------|
| E1 | Y | Y | Y | Y | Y | Y | 6/6 |
| E2 | Y | Y | Y | Y | Y | Y | 6/6 |
| E3 | Y (null) | Y | Y | Y | Y | Y | 6/6 |
| E4 | Y | Y | Y | Y | Y | Y | 6/6 |
| E5 | Y | Y | Y | Y | Y | Y | 6/6 |

**V3 total score: 30 / 30**

Problems found: none in this single run.