from models.todo_list_model import ToDoListModel

class TodoController:
    def __init__(self):
        self.model = ToDoListModel()
    
    def get_all_tasks(self):
        return self.model.get_all()
    
    def add_task(self, description):
        self.model.add(description)
    
    def delete_task(self, task_id):
        self.model.delete(task_id)
    
    def toggle_task_status(self, task_id):
        tasks = self.get_all_tasks()
        current_status = 'pending'
        for task in tasks:
            if task.get('id') == task_id:
                current_status = task.get('status')
                break
        new_status = 'completed' if current_status == 'pending' else 'pending'
        self.model.update_status(task_id, new_status)