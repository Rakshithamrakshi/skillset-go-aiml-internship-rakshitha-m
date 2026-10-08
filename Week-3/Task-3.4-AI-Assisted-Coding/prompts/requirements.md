# To-Do Web App: Requirements (written BEFORE asking the AI)

Task 3.4: AI-Assisted Coding
AI assistant: ChatGPT
Date: 08 Oct 2026

## What the app does

A small to-do list web app built with Python and Flask, running locally.

## Functional requirements

- R1. The home page lists all tasks, each with its text and a done / not done status.
- R2. A form adds a task. The text must be 1 to 100 characters after removing spaces at the start and end. Empty or longer text is rejected with a short error message.
- R3. A button marks a task done or not done.
- R4. A button deletes a task.
- R5. Tasks are saved in a local JSON file named tasks.json next to app.py, so they remain after a restart.
- R6. If tasks.json is missing, the app starts with an empty list. If the file is empty or damaged, the app must not crash.
- R7. No login and no user accounts. The app is for use on this computer only.

## Technical rules

- Python and Flask only, plus the Python standard library.
- Two files: app.py and templates/index.html.
- No tests are requested from the AI. I will write my own tests.

## What I will check in the AI code (my audit list, written before seeing the code)

- Does it meet R1 to R7?
- Bugs and incorrect logic
- Security (unsafe output in the page, debug mode, who can reach the app, secret keys)
- Error handling (bad input, missing or damaged file)
- Hard-coded values
- Privacy (what is stored and where)
- Unnecessary code and poor naming
- Performance, where relevant