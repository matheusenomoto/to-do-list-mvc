from data import task_mock_data

class ToDoListModel:
    def __init__(self):
        self._tasks = task_mock_data.load_tasks()
        self._id_counter = self._get_next_id()
    
    def _get_next_id(self):
        if not self._tasks:
            return 1
        return max(task.get('id', 0) for task in self._tasks) + 1
    
    def _save(self):
        task_mock_data.save_tasks(self._tasks)
    
    def get_all(self):
        return sorted(self._tasks, key=lambda x: x['id'])
    
    def add(self, description):
        if not description:
            return
        
        task = {
            'id': self._id_counter,
            'description': description,
            'status': 'pending'
        }

        self._tasks.append(task)
        self._id_counter += 1
        self._save()
    
    def delete(self, task_id):
        self._tasks = [task for task in self._tasks if task.get('id') != task_id]
        self._save()
    
    def update_status(self, task_id, new_status):
        for task in self._tasks:
            if task.get('id') == task_id:
                task['status'] = new_status
                self._save()
                break
            
    
