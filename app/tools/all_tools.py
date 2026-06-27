from app.tools.todo import (
    add_todo,
    list_todos,
    complete_todo,
    delete_todo,
)

from app.tools.slides import create_presentation
from app.tools.excel import analyze_excel

from app.tools.calendar import (
    list_calendar_events,
    create_calendar_event,
    update_calendar_event,
    delete_calendar_event,
    find_free_slots,
)
from app.tools.meetings import summarize_meeting

TOOLS = [
    # Todo
    add_todo,
    list_todos,
    complete_todo,
    delete_todo,

    # Slides
    create_presentation,

    # Excel
    analyze_excel,

    # Calendar
    list_calendar_events,
    create_calendar_event,
    update_calendar_event,
    delete_calendar_event,
    find_free_slots,

    #meetings
    summarize_meeting
]