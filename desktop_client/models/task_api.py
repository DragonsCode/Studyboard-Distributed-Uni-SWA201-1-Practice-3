import requests


class TaskApiModel:
    BASE_URL = "http://127.0.0.1:8000"

    def get_tasks(self):
        response = requests.get(f"{self.BASE_URL}/tasks", timeout=5)
        response.raise_for_status()
        return response.json()

    def create_task(self, title, description):
        response = requests.post(
            f"{self.BASE_URL}/tasks",
            json={"title": title, "description": description},
            timeout=5
        )
        response.raise_for_status()
        return response.json()

    def update_status(self, task_id, status):
        response = requests.patch(
            f"{self.BASE_URL}/tasks/{task_id}/status",
            json={"status": status},
            timeout=5
        )
        response.raise_for_status()
        return response.json()
