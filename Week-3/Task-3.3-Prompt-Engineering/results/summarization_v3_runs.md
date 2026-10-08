# Summarization V3 Runs

Model: ChatGPT
Date: 07 Oct 2026
Change from V2: added the sentence "Each bullet must be one sentence of at most 25 words."

## S1
Output:
* From next month, students can borrow four books for two weeks, and the library will stay open until 5 PM weekdays.
* Saturdays remain closed, while 10 student volunteers will help scan returned books and arrange shelves to support library staff.
* Late fines remain ₹2 per day, capped at ₹40, with changes reviewed after three months based on student feedback.


## S2
Output:
* Riverbend will launch a six-month bike-sharing pilot in January with 60 bicycles across six stations near busy locations.
* Riders pay ₹10 for 30 minutes, then ₹5 per additional 15 minutes, while monthly passes cost ₹250.
* The ₹12-lakh pilot will evaluate usage, bike damage, losses, and rider feedback before potentially expanding to 200 bicycles and 20 stations.


## S3
Output:
* Brightline Software will introduce three colour-coded bins for paper, plastic/metal, and food waste across all office floors.
* Employees will receive training, desk-side bins will be removed, and a six-member green team will monitor mixed waste weekly.
* The company aims to reduce general waste by 40% within six months, using competitions, rewards, and employee feedback to encourage participation.


## V3 Scorecard

Model: ChatGPT
Date: 07 Oct 2026

| ID | Rule 1: exactly 3 bullets | Rule 2: one sentence, max 25 words each | Rule 3: key points covered | Rule 4: no wrong facts | Score |
|----|---------------------------|------------------------------------------|----------------------------|------------------------|-------|
| S1 | Y | Y (19, 19, 21 words) | N (4 of 5 ideas) | Y | 3/4 |
| S2 | Y | Y (18, 17, 21 words) | Y | Y | 4/4 |
| S3 | Y | Y (17, 19, 21 words) | Y | Y | 4/4 |

**V3 total score: 11 / 12**

Problems found:
- S1 left out that Saturday opening is possible next year if another librarian is hired.
- S2 left out the registration and age rules and the station-removal condition (still passes Rule 3).
- S3 bullet 3 links employee feedback to encouraging participation, which is a loose reading of the text.
- Word counts were done by hand from a screenshot.