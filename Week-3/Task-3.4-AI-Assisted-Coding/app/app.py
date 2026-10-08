# To-do web app: corrected version after auditing the original ChatGPT code.
import json
import os
import uuid

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")
MAX_TASK_LENGTH = 100


def load_tasks():
    # Load tasks from the JSON file. Never crash on a missing or bad file.
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except ValueError:
        # Damaged file: keep a copy instead of silently overwriting it later.
        try:
            os.replace(TASKS_FILE, TASKS_FILE + ".damaged")
        except OSError:
            pass
        return []
    except OSError:
        return []

    if not isinstance(data, list):
        return []

    tasks = []
    changed = False
    for item in data:
        # Skip anything that is not a task dictionary with text.
        if not (isinstance(item, dict) and isinstance(item.get("text"), str)):
            continue
        if "id" not in item:
            item["id"] = uuid.uuid4().hex  # older files get ids once
            changed = True
        tasks.append(
            {"id": str(item["id"]), "text": item["text"], "done": bool(item.get("done", False))}
        )

    if changed:
        save_tasks(tasks)
    return tasks


def save_tasks(tasks):
    # Save tasks to the JSON file.
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


@app.route("/", methods=["GET", "POST"])
def index():
    tasks = load_tasks()
    error = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if not text:
            error = "Task cannot be empty."
        elif len(text) > MAX_TASK_LENGTH:
            error = f"Task must be {MAX_TASK_LENGTH} characters or less."
        else:
            tasks.append({"id": uuid.uuid4().hex, "text": text, "done": False})
            save_tasks(tasks)
            return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks, error=error)


@app.route("/toggle/<task_id>", methods=["POST"])
def toggle_task(task_id):
    # Find the task by its id, not by its position in the list.
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            save_tasks(tasks)
            break
    return redirect(url_for("index"))


@app.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = load_tasks()
    remaining = [task for task in tasks if task["id"] != task_id]
    if len(remaining) != len(tasks):
        save_tasks(remaining)
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Local use only, with the debugger turned off.
    app.run(host="127.0.0.1", port=5000, debug=False)