# Summarization V2 Runs

Model: ChatGPT
Date: 07 Oct 2026
Change from V1: asked for exactly 3 bullet points and nothing else (no title, introduction or closing line).

## S1
Output:
* From next month, students can borrow up to four books for two weeks, and the library will stay open until 5 PM on weekdays but remain closed on Saturdays.
* Ten student volunteers will help with returned books and shelves; late fees remain ₹2 per day per book, capped at ₹40 per book.
* The school will review the changes after three months, with possible Saturday opening next year if results are positive and another librarian is hired.


## S2
Output:
* Riverbend will launch a six-month bike-sharing pilot in January with 60 bikes at six stations, charging ₹10 for the first 30 minutes and ₹5 for each additional 15 minutes; monthly passes cost ₹250.
* The bikes include safety and tracking features, require phone-number and government-ID registration, and are restricted to users aged 16 and above; the ₹12 lakh pilot budget covers bikes, stations, and maintenance.
* After six months, the council will evaluate rides, bike damage/loss, complaints, and rider feedback; if successful, the program will expand to 200 bikes and 20 stations next year.


## S3
Output:
* Brightline Software is launching a recycling program with separate bins for paper, plastic/metal, and food waste, aiming to reduce general waste by 40% in six months.
* Desk-side bins will be removed, employees will receive training and printed guides, and a six-member Green Team will monitor waste every Friday.
* A monthly clean-bin competition with a free team lunch will encourage participation; the program will be reviewed if the six-month waste-reduction target is not met.



## V2 Scorecard

Model: ChatGPT
Date: 07 Oct 2026

| ID | Rule 1: exactly 3 bullets | Rule 2: one sentence, max 25 words each | Rule 3: key points covered | Rule 4: no wrong facts | Score |
|----|---------------------------|------------------------------------------|----------------------------|------------------------|-------|
| S1 | Y | N (bullet 1 about 29 words) | Y | Y | 3/4 |
| S2 | Y | N (bullets about 33, 32, 28 words) | Y | Y | 3/4 |
| S3 | Y | N (bullet 1 about 26 words) | Y | Y | 3/4 |

**V2 total score: 9 / 12**

Problems found:
- All three replies had exactly 3 bullets and no extra text, but bullets were too long and often joined two ideas with a semicolon.
- S2 did not mention that a station is removed after more than ten complaints.
- Word counts were done by hand from a screenshot, so S3 bullet 1 (26 words) is borderline.