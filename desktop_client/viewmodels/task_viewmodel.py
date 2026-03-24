from desktop_client.models.task_api import TaskApiModel


class TaskViewModel:
    def __init__(self):
        self.model = TaskApiModel()
        self.tasks = []

    def refresh(self):
        self.tasks = self.model.get_tasks()
        return self.tasks

    def add_task(self, title, description):
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        self.model.create_task(title, description)
        return self.refresh()

    def move_to_in_progress(self, task_id):
        self.model.update_status(task_id, "IN_PROGRESS")
        return self.refresh()

    def move_to_done(self, task_id):
        self.model.update_status(task_id, "DONE")
        return self.refresh()
