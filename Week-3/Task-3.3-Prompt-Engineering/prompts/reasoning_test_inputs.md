# Reasoning Test Inputs (fixed for all prompt versions)

Category: Reasoning (word problems with traps)
All problems are invented for this exercise. No personal data.

## Problems

**R1.** A mug and a spoon cost ₹66 together. The mug costs ₹60 more than the spoon. How much does the spoon cost?

**R2.** Asha buys 3 packs of pencils with 12 pencils in each pack. She gives 5 pencils to her brother. Her sister is 9 years old and owns 4 erasers. How many pencils does Asha have left?

**R3.** A workshop starts at 10:50 AM and lasts 3 hours 25 minutes. A 40-minute lunch begins right after it ends. At what time does lunch end?

**R4.** A shirt originally costs ₹500. The shop raises the price by 20%. Later it lowers the new price by 20%. What is the final price?

**R5.** 4 printers print 4 posters in 4 minutes. At the same speed per printer, how many minutes would 12 printers need to print 12 posters?

## Expected answers (written BEFORE running any prompt)

| ID | Expected final answer | Working (short) |
|----|-----------------------|-----------------|
| R1 | ₹3 | Spoon = s, mug = s + 60, so 2s + 60 = 66, s = 3 (trap: ₹6) |
| R2 | 31 pencils | 3 x 12 = 36, minus 5 = 31 (sister's age and erasers are irrelevant) |
| R3 | 2:55 PM | 10:50 + 3h25m = 2:15 PM, plus 40 min = 2:55 PM |
| R4 | ₹480 | 500 x 1.2 = 600, then 600 x 0.8 = 480 (trap: ₹500) |
| R5 | 4 minutes | Each printer makes 1 poster per 4 minutes, so 12 printers make 12 posters in 4 minutes (trap: 12) |

## Scoring criteria (written before running)

- Rule 1: The last line of the reply starts with "Answer:" and gives the final answer. 1 point, otherwise 0.
- Rule 2: The reply is under 100 words. 1 point, otherwise 0.
- Correct final answer: 1 point, otherwise 0.
- Maximum per problem: 3 points. Maximum per full run of 5 problems: 15 points.

## Run log

- Model name: (fill in after you run)
- Date: 07 Oct 2026