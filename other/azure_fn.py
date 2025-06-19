import azure.functions as func
import logging
import json
from datetime import datetime

{
    "bindings": [
        {
            "name": "req",
            "type": "queueTrigger",
            "direction": "in",
            "queueName": "notifications",
            "connection": "AzureWebJobsStorage",
        }
    ]
}


def main(req: func.QueueMessage) -> None:
    logging.info(
        "Python queue trigger function processed a queue item.",
        req.get_body().decode("utf-8"),
    )

    # Process the queue message
    message_body = json.loads(req.get_body().decode("utf-8"))
    user_id = message_body.get("user_id")
    notification = message_body.get("notification")
    if user_id and notification:
        logging.info(f"User ID: {user_id}, Notification: {notification}")


{
    "bindings": [
        {
            "name": "timer",
            "type": "timeTrigger",
            "direction": "in",
            "schedule": "0 */5 * * * *",  # Every 5 minutes
        }
    ],
}


def timer_trigger(timer: func.TimerRequest) -> None:
    utc_timestamp = datetime.now(datetime.timezone.utc).isoformat()
    logging.info(f"Timer trigger function executed at {utc_timestamp}")

    if timer.past_due:
        logging.warning("The timer is past due!")
