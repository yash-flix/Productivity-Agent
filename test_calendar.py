from app.tools.calendar import list_calendar_events

print("Testing Calendar Tool...\n")

result = list_calendar_events.invoke(
    {
        "day": "today"
    }
)

print(result)