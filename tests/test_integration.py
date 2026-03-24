import requests

TASK_SERVICE = "http://127.0.0.1:8000"
EVENT_SERVICE = "http://127.0.0.1:8001"


def run_test():
    created = requests.post(
        f"{TASK_SERVICE}/tasks",
        json={"title": "Prepare slides", "description": "Create practice 3 presentation"},
        timeout=5
    ).json()

    requests.patch(
        f"{TASK_SERVICE}/tasks/{created['id']}/status",
        json={"status": "IN_PROGRESS"},
        timeout=5
    )

    tasks = requests.get(f"{TASK_SERVICE}/tasks", timeout=5).json()
    events = requests.get(f"{EVENT_SERVICE}/events", timeout=5).json()

    assert len(tasks) > 0, "Task list is empty"
    assert len(events) > 0, "Event log is empty"

    print("Integration test passed")
    print("Tasks:", tasks)
    print("Events:", events)


if __name__ == "__main__":
    run_test()
