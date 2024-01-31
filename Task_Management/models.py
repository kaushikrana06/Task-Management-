# models.py

class Task:
    def __init__(self, id, title, is_completed=False):
        self.id = id
        self.title = title
        self.is_completed = is_completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'is_completed': self.is_completed
        }

class TaskStore:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_all_tasks(self):
        return [task.to_dict() for task in self.tasks.values()]

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def bulk_add_tasks(self, tasks_data):
        new_tasks = []
        for task_data in tasks_data:
            task = Task(self.next_id, task_data['title'], task_data.get('is_completed', False))
            self.tasks[self.next_id] = task
            new_tasks.append(task)
            self.next_id += 1
        return new_tasks

    def bulk_delete_tasks(self, task_ids):
        for task_id in task_ids:
            self.delete_task(task_id)        

    def update_task(self, task_id, title=None, is_completed=None):
        task = self.get_task(task_id)
        if task:
            task.title = title if title is not None else task.title
            task.is_completed = is_completed if is_completed is not None else task.is_completed

task_store = TaskStore()






