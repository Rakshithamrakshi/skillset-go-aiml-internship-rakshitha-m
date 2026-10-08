# Summarization V1 Runs

Model: ChatGPT
Date: 07 Oct 2026
Prompt used: Summarize this text: [TEXT]

## S1
Output:
Greenfield Public School will introduce new library rules next month based on student feedback. Students will be able to borrow **up to four books for two weeks**, and the library will remain open until **5 PM on weekdays**. It will still be closed on Saturdays due to limited staff.

The school will train **10 student volunteers** to help with returned books and shelving. Late fees will remain **₹2 per day per book**, with a maximum of **₹40 per book**. After three months, the school will survey students again to evaluate the changes. If successful, Saturday morning hours may be introduced next year if an additional librarian is hired. Students interested in volunteering must apply by the **end of this week**.


## S2
Output:
Riverbend will launch a **six-month bike-sharing pilot in January** with **60 bicycles at 6 stations**. Riders will pay ₹10 for the first 30 minutes, ₹5 for each additional 15 minutes, or ₹250 for a monthly pass with unlimited rides up to 45 minutes each.

The program aims to encourage cycling for short trips under 3 km. Bikes will have safety features and tracking devices, while users must register with a phone number and government ID; children under 16 cannot use them. The pilot costs **₹12 lakh** and includes two maintenance workers.

The council will monitor complaints about parking, bike damage/loss, total rides, and rider feedback. If successful, the program could expand to **200 bicycles and 20 stations** next year.


## S3
Output:
Brightline Software is launching a recycling program next week. Each floor will have **blue bins for paper, yellow for plastic/metal, and green for food waste**, with food waste composted twice a week for ₹3,000 per month. Desk-side bins will be removed, a change that has sparked debate. A six-person **Green Team** will monitor waste weekly, while employees receive training and printed guides. Monthly competitions will reward the floor with the cleanest bins with a free team lunch. The company aims to **reduce general waste by 40% within six months** and will review the program if the target is not met.



## V1 Scorecard

Model: ChatGPT
Date: 07 Oct 2026

| ID | Rule 1: exactly 3 bullets | Rule 2: one sentence, max 25 words each | Rule 3: key points covered | Rule 4: no wrong facts | Score |
|----|---------------------------|------------------------------------------|----------------------------|------------------------|-------|
| S1 | N (2 paragraphs) | N | Y | Y | 2/4 |
| S2 | N (3 paragraphs) | N | Y | Y | 2/4 |
| S3 | N (1 paragraph) | N | Y | Y | 2/4 |

**V1 total score: 6 / 12**

Problems found:
- No reply used bullet points; all were paragraphs with several sentences.
- S2 did not mention that a station is removed after more than ten complaints (only partly covered).
- Note: S1 has only five distinct key ideas in the table (its first cell has one idea), and all five were covered.
- Scoring was done by eye from a screenshot; word counts were not measured.