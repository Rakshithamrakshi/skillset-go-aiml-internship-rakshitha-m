# ChatGPT original reply (saved BEFORE any change by me)

Model: ChatGPT (exact model version not recorded)
Date: 08 Oct 2026

## Prompt I sent
Build a small to-do web app with Python and Flask.

Requirements:
1. The home page lists all tasks, each with its text and a done / not done status.
2. A form adds a task. The text must be 1 to 100 characters after removing spaces at the start and end. Empty or longer text is rejected with a short error message.
3. A button marks a task done or not done.
4. A button deletes a task.
5. Tasks are saved in a local JSON file named tasks.json in the same folder as app.py, so they remain after a restart.
6. If tasks.json is missing, start with an empty list. If the file is empty or damaged, do not crash.
7. No login and no accounts. The app is for use on this computer only.

Technical rules:
- Use only Flask and the Python standard library.
- Use exactly two files: app.py and templates/index.html.
- Add short comments.
- Give the full content of each file in its own code block, with the file name above it.
- After the code, give the command to run it.
- Do not write tests.

## ChatGPT reply
### `app.py`

```python
from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    # Load tasks safely from the JSON file.
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


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
        elif len(text) > 100:
            error = "Task must be 100 characters or less."
        else:
            tasks.append({
                "text": text,
                "done": False
            })
            save_tasks(tasks)
            return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks, error=error)


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    tasks = load_tasks()

    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id].get("done", False)
        save_tasks(tasks)

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = load_tasks()

    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 700px;
            margin: 40px auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        form.add-form {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input[type="text"] {
            flex: 1;
            padding: 10px;
        }

        button {
            padding: 8px 12px;
            cursor: pointer;
        }

        .error {
            color: red;
            margin-bottom: 15px;
        }

        .task {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }

        .task-text.done {
            text-decoration: line-through;
            color: #777;
        }

        .actions {
            display: flex;
            gap: 5px;
        }
    </style>
</head>
<body>
    <h1>To-Do List</h1>

    <form class="add-form" method="POST">
        <input
            type="text"
            name="text"
            maxlength="100"
            placeholder="Enter a task"
        >
        <button type="submit">Add</button>
    </form>

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}

    {% for task in tasks %}
        <div class="task">
            <span class="task-text {% if task.done %}done{% endif %}">
                {{ task.text }}
            </span>

            <div class="actions">
                <form method="POST" action="{{ url_for('toggle_task', task_id=loop.index0) }}">
                    <button type="submit">
                        {% if task.done %}Not Done{% else %}Done{% endif %}
                    </button>
                </form>

                <form method="POST" action="{{ url_for('delete_task', task_id=loop.index0) }}">
                    <button type="submit">Delete</button>
                </form>
            </div>
        </div>
    {% else %}
        <p>No tasks yet.</p>
    {% endfor %}
</body>
</html>
```

### Run the app

From the folder containing `app.py`:

```bash
pip install Flask
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

`tasks.json` will be created automatically in the same folder when the first task is added.
