from fastapi import FastAPI
from pydantic import BaseModel
from functions.task_status_handler import handler

app = FastAPI(title="StudyBoard Event Service")

EVENT_LOG = []


class TaskEvent(BaseModel):
    task_id: int
    title: str
    status: str


@app.post("/events/task-status")
def process_event(event: TaskEvent):
    result = handler(event.model_dump(), None)
    EVENT_LOG.append(result)
    return result


@app.get("/events")
def get_events():
    return EVENT_LOG
