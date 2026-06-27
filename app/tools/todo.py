from langchain_core.tools import tool

from app.database.database import SessionLocal
from app.database import todo_repository


@tool
def add_todo(task: str, priority: str = "Medium") -> str:
    """
    Add a new todo item.
    """

    db = SessionLocal()

    try:

        todo = todo_repository.add_task(
            db=db,
            task=task,
            priority=priority
        )

        return f"Task '{todo.task}' added successfully."

    finally:
        db.close()


@tool
def list_todos() -> str:
    """
    List all todo items.
    """

    db = SessionLocal()

    try:

        todos = todo_repository.get_all_tasks(db)

        if not todos:
            return "No tasks found."

        output = []

        for todo in todos:

            status = "✅" if todo.completed else "❌"

            output.append(
                f"{todo.id}. {todo.task} ({todo.priority}) {status}"
            )

        return "\n".join(output)

    finally:
        db.close()


@tool
def complete_todo(task_id: list[int]) -> str:
    """
    Mark a todo as completed.
    """

    db = SessionLocal()

    try:

        task = todo_repository.complete_task(db, task_id)

        if task is None:
            return "Task not found."

        return f"Completed '{task.task}'."

    finally:
        db.close()


@tool
def delete_todo(task_id: int) -> str:
    """
    Delete a todo item.
    """

    db = SessionLocal()

    try:

        deleted = todo_repository.delete_task(db, task_id)

        if not deleted:
            return "Task not found."

        return "Task deleted."

    finally:
        db.close()