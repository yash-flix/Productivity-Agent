from sqlalchemy.orm import Session

from app.database.models import Todo




def add_task(
    db: Session,
    task: str,
    priority: str = "Medium"
):

    todo = Todo(
        task=task,
        priority=priority
    )

    db.add(todo)

    db.commit()

    db.refresh(todo)

    return todo

def find_task_by_name(
    db,
    task_name: str
):

    return (

        db.query(Todo)

        .filter(

            Todo.task.ilike(f"%{task_name}%")

        )

        .first()

    )

def get_all_tasks(db: Session):

    return db.query(Todo).all()


def complete_task_by_id(
    db: Session,
    task_id: int
):

    task = db.query(Todo).filter(
        Todo.id == task_id
    ).first()

    if task is None:
        return None

    task.completed = True

    db.commit()

    db.refresh(task)

    return task


def complete_task_by_name(
    db,
    task_name: str
):

    task = find_task_by_name(
        db,
        task_name
    )

    if task is None:
        return None

    task.completed = True

    db.commit()

    db.refresh(task)

    return task

def complete_all_tasks(db):

    tasks = (

        db.query(Todo)

        .filter(

            Todo.completed == False

        )

        .all()

    )

    for task in tasks:

        task.completed = True

    db.commit()

    return len(tasks)


def delete_task(
    db: Session,
    task_id: int
):

    task = db.query(Todo).filter(
        Todo.id == task_id
    ).first()

    if task is None:
        return False

    db.delete(task)

    db.commit()

    return True