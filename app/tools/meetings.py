import re

from langchain_core.tools import tool

from app.services.meeting_service import MeetingService
from app.database.database import SessionLocal
from app.database.todo_repository import add_task


service = MeetingService()


INVALID_TASKS = {
    "",
    "none",
    "none.",
    "none mentioned",
    "none mentioned.",
    "n/a",
    "na",
    "-",
    "nothing",
    "no action items",
    "no action item",
}


@tool
def summarize_meeting(
    transcript: str,
    create_todos: bool = True
):
    """
    Summarize a meeting transcript.

    Optionally extracts action items and
    automatically adds them as todos.
    """

    summary = service.summarize(transcript)

    added = 0

    if create_todos:

        db = SessionLocal()

        try:

            if "Action Items" in summary:

                action_section = summary.split("Action Items", 1)[1]

            else:

                action_section = summary

            action_items = re.findall(
                r"[-•]\s+(.+)",
                action_section
            )

            for task in action_items:

                task = task.strip()

                normalized = (
                    task.lower()
                    .strip(" .:-")
                )

                if normalized in INVALID_TASKS:
                    continue

                if len(task) < 3:
                    continue

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