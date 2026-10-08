"""Behaviour check for the CORRECTED app.py (same cases as check_app.py)."""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.abspath(os.path.join(HERE, "..", "app"))
sys.path.insert(0, APP_DIR)

import app as todo  # does not start the server

client = todo.app.test_client()
TASKS = todo.TASKS_FILE
BACKUP = TASKS + ".bak"
DAMAGED = TASKS + ".damaged"


def write_file(text):
    with open(TASKS, "w", encoding="utf-8") as f:
        f.write(text)


def read_file(path=TASKS):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def count_saved():
    try:
        return len(json.loads(read_file()))
    except json.JSONDecodeError:
        return "file is not valid JSON"


def main():
    for label, text in [("100 chars", "a" * 100), ("101 chars", "a" * 101), ("spaces only", "   ")]:
        write_file("[]")
        r = client.post("/", data={"text": text})
        error_shown = b'class="error"' in r.data
        print(f"T3 {label}: status {r.status_code}, tasks saved {count_saved()}, error shown {error_shown}")

    if os.path.exists(DAMAGED):
        os.remove(DAMAGED)
    write_file("{broken")
    r = client.get("/")
    print("T6 damaged file, open page: status", r.status_code)
    print("T6 damaged copy kept:", os.path.exists(DAMAGED))
    if os.path.exists(DAMAGED):
        print("T6 damaged copy content:", read_file(DAMAGED))
    r = client.post("/", data={"text": "after damage"})
    print("T6 add a task: status", r.status_code, ", saved tasks", count_saved())

    write_file("[1, 2]")
    r = client.get("/")
    print("T7 file [1, 2], open page: status", r.status_code, ", rows shown",
          r.data.count(b'class="task"'))
    r = client.post("/toggle/abc")
    print("T7 press Done on an unknown id: status", r.status_code)

    write_file(json.dumps([{"id": "a", "text": "A", "done": False},
                           {"id": "b", "text": "B", "done": False}]))
    client.post("/delete/a")
    client.post("/delete/a")
    print("Two tabs, both delete A: tasks left", [t["text"] for t in json.loads(read_file())])

    write_file(json.dumps([{"text": "old task", "done": False}]))
    client.get("/")
    print("Old file without id: id added:", "id" in json.loads(read_file())[0])

    write_file("[]")
    client.post("/", data={"text": "keep me"})
    task_id = json.loads(read_file())[0]["id"]
    client.post(f"/toggle/{task_id}")
    print("Toggle by id, done is now:", json.loads(read_file())[0]["done"])

    with open(os.path.join(APP_DIR, "app.py"), encoding="utf-8") as f:
        print("Debug flag turned on in app.py:", "debug=True" in f.read())


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
    if os.path.exists(DAMAGED):
        os.remove(DAMAGED)