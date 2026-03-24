from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="StudyBoard Task Service")

TASKS = []
NEXT_ID = 1
EVENT_SERVICE_URL = "http://127.0.0.1:8001/events/task-status"


class TaskCreate(BaseModel):
    title: str
    description: str = ""


class TaskStatusUpdate(BaseModel):
    status: str


@app.get("/tasks")
def get_tasks():
    return TASKS


@app.post("/tasks")
def create_task(payload: TaskCreate):
    global NEXT_ID

    task = {
        "id": NEXT_ID,
        "title": payload.title,
        "description": payload.description,
        "status": "TODO"
    }
    NEXT_ID += 1
    TASKS.append(task)
    return task


@app.patch("/tasks/{task_id}/status")
def update_status(task_id: int, payload: TaskStatusUpdate):
    for task in TASKS:
        if task["id"] == task_id:
            task["status"] = payload.status

            try:
                requests.post(
                    EVENT_SERVICE_URL,
                    json={
                        "task_id": task["id"],
                        "title": task["title"],
                        "status": task["status"]
                    },
                    timeout=3
                )
            except requests.RequestException:
                pass

            return task

    raise HTTPException(status_code=404, detail="Task not found")
