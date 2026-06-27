import re

from langchain_core.tools import tool

from app.services.meeting_service import MeetingService
from app.database.database import SessionLocal
from app.database.todo_repository import add_task


service = MeetingService()


@tool
def summarize_meeting(
    transcript: str,
    create_todos: bool = True
):
    """
    Summarize a meeting transcript.

    Optionally extract action items and
    automatically add them as todos.
    """

    summary = service.summarize(
        transcript
    )

    added = 0

    if create_todos:

        db = SessionLocal()

        try:

            action_items = re.findall(

                r"- (.+)",

                summary.split(
                    "Action Items"
                )[-1]

            )

            for task in action_items:

                add_task(

                    db=db,

                    task=task,

                    priority="Medium"

                )

                added += 1

        finally:

            db.close()

    return f"""
Meeting Summary

{summary}

Todos Added:

{added}
"""