from flask import Flask, render_template, request, redirect, url_for
from controllers.todo_controller import TodoController

app = Flask(__name__)
controller = TodoController()

@app.route('/')
def index():
    tasks = controller.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    description = request.form.get('description')
    controller.add_task(description)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    """Handles updating a task's status (toggle)."""
    controller.toggle_task_status(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Handles the deletion of a task."""
    controller.delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)