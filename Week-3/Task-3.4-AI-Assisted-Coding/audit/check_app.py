"""Behaviour check for the ORIGINAL ChatGPT app.py.
Uses Flask's test client (no server needed) and prints what actually happens.
Backs up tasks.json first and restores it at the end."""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(HERE, "..", "app")
sys.path.insert(0, os.path.abspath(APP_DIR))

import app as todo  # imports app.py; does not start the server

client = todo.app.test_client()
TASKS = todo.TASKS_FILE
BACKUP = TASKS + ".bak"


def write_file(text):
    with open(TASKS, "w", encoding="utf-8") as f:
        f.write(text)


def read_file():
    with open(TASKS, "r", encoding="utf-8") as f:
        return f.read()


def count_saved():
    try:
        return len(json.loads(read_file()))
    except json.JSONDecodeError:
        return "file is not valid JSON"


def main():
    # T3: task length and spaces-only text
    for label, text in [("100 chars", "a" * 100), ("101 chars", "a" * 101), ("spaces only", "   ")]:
        write_file("[]")
        r = client.post("/", data={"text": text})
        has_error = b'class="error"' in r.data
        print(f"T3 {label}: status {r.status_code}, tasks saved {count_saved()}, error shown {has_error}")

    # T6: damaged file
    write_file("{broken")
    r = client.get("/")
    print("T6 damaged file, open page: status", r.status_code)
    r = client.post("/", data={"text": "after damage"})
    print("T6 damaged file, add a task: status", r.status_code)
    print("T6 file content afterwards:", read_file().replace("\n", " "))

    # T7: valid JSON but wrong type
    write_file("[1, 2]")
    r = client.get("/")
    rows = r.data.count(b'class="task"')
    print("T7 file [1, 2], open page: status", r.status_code, ", rows shown", rows)
    r = client.post("/toggle/0")
    print("T7 file [1, 2], press Done on row 0: status", r.status_code)

    # Two browser tabs: both pages show task A, both press its Delete button
    write_file(json.dumps([{"text": "A", "done": False}, {"text": "B", "done": False}]))
    client.post("/delete/0")  # tab 1 deletes A
    client.post("/delete/0")  # tab 2 still shows A and presses Delete on it
    left = [t["text"] for t in json.loads(read_file())]
    print("Two tabs, both delete A: tasks left", left)

    # Saving
    write_file("[]")
    client.post("/", data={"text": "keep me"})
    print("Saved file after adding a task:", read_file().replace("\n", " "))


if os.path.exists(TASKS):
    shutil.copy(TASKS, BACKUP)
try:
    main()
finally:
    if os.path.exists(BACKUP):
        shutil.copy(BACKUP, TASKS)
        os.remove(BACKUP)
    elif os.path.exists(TASKS):
        os.remove(TASKS)