from datetime import datetime, timedelta

from langchain_core.tools import tool

from app.services.calendar_service import CalendarService

calendar = CalendarService()


@tool
def list_calendar_events(day: str = "today") -> str:
    """
    List Google Calendar events for today or tomorrow.

    Args:
        day: "today" or "tomorrow"
    """

    day = day.lower()

    if day == "today":
        start = datetime.now()

    elif day == "tomorrow":
        start = datetime.now() + timedelta(days=1)

    else:
        return "Only 'today' and 'tomorrow' are supported."

    end = start + timedelta(days=1)

    events = calendar.list_events(start, end)

    if not events:
        return f"No events found for {day}."

    result = []

    for event in events:

        start_time = event["start"].get(
            "dateTime",
            event["start"].get("date")
        )

        result.append(
            f"{start_time} - {event.get('summary', 'Untitled Event')}"
        )

    return "\n".join(result)


@tool
def create_calendar_event(
    title: str,
    when: str,
    duration_minutes: int = 60,
) -> str:
    """
    Create a Google Calendar event.

    Args:
        title: Event title.
        when: Natural language datetime.
        duration_minutes: Meeting duration.
    """

    event = calendar.create_event(
        title,
        when,
        duration_minutes
    )

    return (
        f"Event '{event['summary']}' "
        f"created successfully."
    )


@tool
def update_calendar_event(
    title: str,
    when: str,
    duration_minutes: int = 60,
) -> str:
    """
    Update an existing calendar event.

    Args:
        title: Existing event title.
        when: New natural language date/time.
        duration_minutes: Event duration.
    """

    updated = calendar.update_event(
        title,
        when,
        duration_minutes
    )

    if updated is None:
        return "Event not found."

    return "Event updated successfully."


@tool
def delete_calendar_event(
    title: str,
) -> str:
    """
    Delete a calendar event.

    Args:
        title: Event title.
    """

    deleted = calendar.delete_event(title)

    if not deleted:
        return "Event not found."

    return "Event deleted successfully."


@tool
def find_free_slots(
    when: str = "today",
    duration_minutes: int = 60,
) -> str:
    """
    Find available meeting slots.

    Args:
        when: today, tomorrow, next monday...
        duration_minutes: Required meeting duration.
    """

    slots = calendar.find_free_slots(
        when,
        duration_minutes
    )

    if not slots:
        return "No free slots available."

    result = []

    for start, end in slots:

        result.append(
            f"{start.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')}"
        )

    return "\n".join(result)