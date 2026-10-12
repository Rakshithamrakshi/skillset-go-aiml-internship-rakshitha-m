# Task 3.4: AI-Assisted Coding (To-Do Web App)

Week 3 of the Skill Set Go EduTech AI/ML internship.

## Goal

Build a small application with an AI coding assistant, then review the generated code, correct it where necessary and audit it.

## What was built

A local to-do web app (Python, Flask, one HTML template). It lists tasks, adds tasks (1 to 100 characters), marks them done or not done, deletes them, and saves them in `tasks.json`.

## Method

1. I wrote the requirements and my audit checklist before asking the AI (`prompts/requirements.md`).
2. ChatGPT wrote the first version. Its unedited reply is in `prompts/chatgpt_original_reply.md`.
3. I ran the app and wrote test scripts (`audit/check_app.py` for the original, `audit/check_fixed_app.py` for the corrected version) using Flask's test client.
4. I recorded only the problems that the tests or the terminal output showed, then corrected them and re-ran the same checks.

## Problems found and fixed

| Problem | Evidence | Fix |
|---|---|---|
| Debug mode left on | Terminal showed "Debug mode: on" and a debugger PIN | `debug=False` |
| Tasks identified by list position | Second delete from a stale page removed another task | Each task has a unique id |
| Wrong-type JSON crashed a route | File `[1, 2]` then Done gave status 500 | Skip items that are not valid tasks |
| Damaged file silently overwritten | Adding a task replaced the damaged content | Damaged file kept as `tasks.json.damaged` |

The full table is in `audit/audit_notes.md`.

## Limitations

- Tests used Flask's test client, not a real browser or a real second tab.
- Not addressed: CSRF protection (the app is for local use only), and no automated unit test suite.
- One model (ChatGPT), one run. The exact model version was not recorded.

## Folder structure

```
Task-3.4-AI-Assisted-Coding/
├── README.md
├── prompts/       requirements.md and the unedited ChatGPT reply
├── app/           app.py and templates/index.html (corrected version)
├── audit/         audit_notes.md and the two check scripts
└── screenshots/   evidence screenshots
```

## How to run

From the repository root:

```
pip install flask
python Week-3\Task-3.4-AI-Assisted-Coding\app\app.py
```

Then open http://127.0.0.1:5000. Stop with Ctrl+C. Your tasks are stored in `app/tasks.json`, which Git ignores.

## How to re-run the checks

```
python Week-3\Task-3.4-AI-Assisted-Coding\audit\check_fixed_app.py
```