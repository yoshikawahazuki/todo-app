from flask import Flask, render_template, request, redirect, flash
import json
import uuid

app = Flask(__name__)
app.secret_key = "aaa"

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

@app.route("/")
def index():
    tasks = load_tasks()
    tasks = sorted(tasks, key=lambda t: t["done"])
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if not task or not task.strip():
        flash("1文字以上入力してください")
        return redirect("/")
    task = task.strip()

    if len(task) > 10:
        flash("文字数が長すぎます。10文字以内で入力してください")
        return redirect("/")
    
    tasks = load_tasks()
    tasks.append({"id": str(uuid.uuid4()),"text": task.strip(), "done": False})
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<task_id>")
def delete(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return redirect("/")

@app.route("/toggle/<task_id>")
def toggle(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
            break
    save_tasks(tasks)
    return redirect("/")
        

if __name__ == "__main__":
    app.run(debug=True)
