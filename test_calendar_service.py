from datetime import datetime, timedelta

from app.services.calendar_service import CalendarService

service = CalendarService()

events = service.list_events(
    datetime.now(),
    datetime.now() + timedelta(days=1)
)

print(events)