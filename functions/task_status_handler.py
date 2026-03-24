from datetime import datetime


def handler(event, context):
    return {
        "message": f"Task #{event['task_id']} ({event['title']}) changed status to {event['status']}",
        "timestamp": datetime.utcnow().isoformat()
    }
