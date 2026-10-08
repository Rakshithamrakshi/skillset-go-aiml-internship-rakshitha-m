# AI Coding Audit: To-Do Web App (Task 3.4)

AI assistant: ChatGPT (exact model version not recorded). Date: 08 Oct 2026.
Original code: prompts/chatgpt_original_reply.md (unedited). Corrected code: app/app.py and app/templates/index.html.
Evidence: audit/check_app.py (original) and audit/check_fixed_app.py (corrected), run with Flask's test client.

## Audit table

| Code/Feature | AI Suggestion | My Review | Problem Found | Correction | Final Status |
|---|---|---|---|---|---|
| app.run | `app.run(debug=True)` | Terminal showed "Debug mode: on", "Debugger is active" and a PIN | Debug mode left on (security) | `debug=False`, host 127.0.0.1 and port 5000 set explicitly | Fixed, verified: flag absent from app.py |
| Task identity | Tasks addressed by list index (`/toggle/<int:task_id>`) | Test: two stale pages both pressed Delete on task A | Second delete removed task B too (`[]` left) | Each task gets a uuid; routes use the id | Fixed, verified: `['B']` left |
| load_tasks | Accepts any JSON list | File `[1, 2]`: page opened with 2 rows, Done returned status 500 (`AttributeError: 'int' object has no attribute 'get'`) | Wrong-type data crashes a route | Skip items that are not dicts with text | Fixed, verified: 0 rows, no 500 |
| Damaged file | Treated as empty list | After "{broken", adding a task overwrote the file | Damaged content silently lost | File renamed to tasks.json.damaged first (and ignored by Git) | Fixed, verified: copy kept |
| Length and empty checks | Server-side checks | 100 accepted, 101 and spaces-only rejected | None found | None | Meets R2 |
| Unsafe text | Jinja auto-escaping | `<b>bold</b>` shown as plain text | None found | None | OK |
| Magic number | `100` written in code | Reviewed by reading | Hard-coded value | `MAX_TASK_LENGTH` constant | Fixed (reading only) |
| CSRF token | None | Read only, not tested | Not a confirmed problem; local app | None | Not addressed, noted as a limit |

## Limits

- Tests used Flask's test client, not a real browser or real second tab.
- One model, one run. Model version not recorded.
- T5 restart: with the corrected app, "keep me" was added, the app was stopped and started again, and the task was still shown after refresh (seen in the browser; terminal showed two starts with "Debug mode: off").