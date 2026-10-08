# Summarization Test Inputs (fixed for all prompt versions)

Category: Summarization (about 300 words into 3 bullets)
All texts are invented for this exercise. No real people or data.

## Texts

**S1. A school library change**

Greenfield Public School has decided to change how its library works from next month. Until now, students could borrow up to two books for one week, and the library closed at 3 PM. Teachers felt this was too limiting, because many students wanted to read more and needed time after classes to use the library. After a survey of 400 students, the school found that 72 percent wanted to borrow more books and 65 percent wanted longer opening hours. The principal therefore approved a new plan. From next month, students can borrow up to four books for two weeks. The library will stay open until 5 PM on weekdays. However, the library will remain closed on Saturdays because there are not enough staff members. To help with the extra work, the school will train 10 student volunteers to scan returned books and arrange shelves. Late returns will still cost 2 rupees per day for each book, but the maximum fine for one book will be capped at 40 rupees. The school hopes the new rules will encourage reading habits and reduce the number of students who skip the library because of time limits. After three months, the school will run another survey and decide whether the changes should continue. If the results are positive, the school may also open the library on Saturday mornings next year, provided it can hire an additional librarian. Parents have been informed through a letter and are welcome to give feedback to the class teachers. Students who want to be volunteers must apply to the head librarian by the end of this week.

**S2. A community bike-sharing pilot**

The town of Riverbend is starting a six-month bike-sharing pilot in January. The council has placed 60 bicycles at 6 stations near the bus stand, the market, the college and the lake. Riders pay 10 rupees for the first 30 minutes and 5 rupees for each extra 15 minutes. Monthly passes cost 250 rupees and give unlimited rides of up to 45 minutes each. The council chose these locations after counting how many people walk between them every day. Officials say that short trips under three kilometres make up almost half of all trips in the town, and that many of these are made by car or scooter. The bikes have locks, lights and a basket, and each one carries a tracking device so that missing bikes can be found. Riders must register using a phone number and a government ID, and children under 16 may not use the bikes. The council has set aside 12 lakh rupees for the pilot, which covers the bikes, the stations and two maintenance workers. Some shop owners worry that the stations will take up parking space, so the council has promised to remove one station if more than ten complaints are received in the first month. At the end of the pilot, the council will count total rides, check how many bikes were damaged or lost, and survey riders. If the pilot succeeds, the council plans to expand to 200 bicycles and 20 stations across the town by next year.

**S3. A new office recycling program**

Brightline Software, a company with 150 employees, is launching a recycling program at its office next week. Until now, all waste was collected in a single bin, and the facilities team estimated that over half of it was paper and plastic that could be recycled. Under the new program, every floor will have three colour-coded bins: blue for paper, yellow for plastic and metal, and green for food waste. The green waste will be collected by a local composting service twice a week at a cost of 3,000 rupees per month. The company will also remove all desk-side bins to encourage people to walk to the shared bins, and this change has been the most debated one. A team of six volunteers, called the green team, will check the bins every Friday and report the amount of mixed waste. Each floor will get a short training session during the first week, and printed guides will be placed above the bins. To increase participation, the company will share a monthly chart showing which floor has the cleanest bins, and the winning floor will get a free team lunch. The management hopes to cut general waste by 40 percent within six months. If the target is not reached, the program will be reviewed and the bin layout may be changed. Employees can send questions or complaints to the facilities team by email, and a feedback form will be open for the first month.

## Key points a good summary must cover (written BEFORE running any prompt)

| ID | Key point 1 | Key point 2 | Key point 3 |
|----|-------------|-------------|-------------|
| S1 | Students can now borrow 4 books for 2 weeks (was 2 books for 1 week) | Library open until 5 PM on weekdays, closed Saturdays (staff shortage); 10 student volunteers help | A survey after 3 months decides whether to continue; Saturday opening possible next year if another librarian is hired |
| S2 | Six-month pilot: 60 bikes, 6 stations, with set fees (10 rupees for 30 min, monthly pass 250 rupees) | Riders must register with phone number and ID, no children under 16; 12 lakh rupee budget | Success judged on rides, damage and rider survey; expand to 200 bikes and 20 stations if it works; a station is removed if more than 10 complaints |
| S3 | Three colour-coded bins on every floor and desk-side bins removed | Green team of six volunteers checks bins weekly; training, guides, and monthly floor competition with a free lunch prize | Goal: cut general waste by 40 percent in six months, otherwise the program is reviewed |

## Scoring criteria (written before running)

- Rule 1: The reply has exactly 3 bullet points and no other text (no title, no intro, no closing line). 1 point, otherwise 0.
- Rule 2: Each bullet is one sentence of at most 25 words. 1 point, otherwise 0.
- Rule 3: The 3 bullets together cover at least 5 of the 6 key points listed above for that text, counting key points 1 to 3 in the table as 2 sub-points each. 1 point, otherwise 0.
- Rule 4: No fact in the summary is wrong or invented. 1 point, otherwise 0.
- Maximum per text: 4 points. Maximum per full run of 3 texts: 12 points.

## Run log

- Model name: ChatGPT
- Date: 07 Oct 2026