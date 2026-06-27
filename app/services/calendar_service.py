from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import dateparser


SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]


class CalendarService:

    def __init__(self):
        creds = None

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file(
                "token.json",
                SCOPES
            )

        if not creds or not creds.valid:

            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json",
                    SCOPES
                )

                creds = flow.run_local_server(port=0)

            with open("token.json", "w") as token:
                token.write(creds.to_json())

        self.service = build(
            "calendar",
            "v3",
            credentials=creds
        )

    # --------------------------------------------------
    # Parse natural language datetime
    # --------------------------------------------------

    def parse_datetime(
        self,
        text: str
    ) -> datetime:
        """Convert natural language into a datetime.

        Examples:
        tomorrow 3 PM
        next monday 10 AM
        friday 6 pm
        """

        dt = dateparser.parse(
            text,
            settings={
                "TIMEZONE": "Asia/Kolkata",
                "RETURN_AS_TIMEZONE_AWARE": True,
                "PREFER_DATES_FROM": "future"
            }
        )

        if dt is None:
            raise ValueError(
                f"Could not understand date: {text}"
            )

        return dt

    # --------------------------------------------------
    # Read Events
    # --------------------------------------------------

    def list_events(
        self,
        start_time: datetime,
        end_time: datetime,
    ):

        india = ZoneInfo("Asia/Kolkata")

        if start_time.tzinfo is None:
            start_time = start_time.replace(tzinfo=india)

        if end_time.tzinfo is None:
            end_time = end_time.replace(tzinfo=india)

        events = self.service.events().list(
            calendarId="primary",
            timeMin=start_time.isoformat(),
            timeMax=end_time.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        return events.get("items", [])

    # --------------------------------------------------
    # Search Event
    # --------------------------------------------------

    def find_event_by_title(
        self,
        title: str
    ):

        now = datetime.utcnow()

        future = now + timedelta(days=365)

        events = self.list_events(
            now,
            future
        )

        for event in events:

            summary = event.get(
                "summary",
                ""
            )

            if summary.lower() == title.lower():
                return event

        return None

    # --------------------------------------------------
    # Create Event
    # --------------------------------------------------

    def create_event(
        self,
        title: str,
        when: str,
        duration_minutes: int = 60
    ):

        start_time = self.parse_datetime(
            when
        )

        end_time = (
            start_time +
            timedelta(
                minutes=duration_minutes
            )
        )

        body = {
            "summary": title,
            "start": {
                "dateTime": start_time.astimezone(
                    ZoneInfo("Asia/Kolkata")
                ).isoformat(),
                "timeZone": "Asia/Kolkata"
            },
            "end": {
                "dateTime": end_time.astimezone(
                    ZoneInfo("Asia/Kolkata")
                ).isoformat(),
                "timeZone": "Asia/Kolkata"
            }
        }

        created = self.service.events().insert(
            calendarId="primary",
            body=body
        ).execute()

        return created

    # --------------------------------------------------
    # Update Event
    # --------------------------------------------------

    def update_event(
        self,
        title: str,
        when: str,
        duration_minutes: int = 60
    ):

        event = self.find_event_by_title(
            title
        )

        if event is None:
            return None

        start = self.parse_datetime(
            when
        )

        end = (
            start +
            timedelta(
                minutes=duration_minutes
            )
        )

        event["start"] = {
            "dateTime": start.astimezone(
                ZoneInfo("Asia/Kolkata")
            ).isoformat(),
            "timeZone": "Asia/Kolkata"
        }

        event["end"] = {
            "dateTime": end.astimezone(
                ZoneInfo("Asia/Kolkata")
            ).isoformat(),
            "timeZone": "Asia/Kolkata"
        }

        updated = self.service.events().update(
            calendarId="primary",
            eventId=event["id"],
            body=event
        ).execute()

        return updated

    # --------------------------------------------------
    # Delete Event
    # --------------------------------------------------

    def delete_event(
        self,
        title: str
    ):

        event = self.find_event_by_title(title)

        if event is None:
            return False

        self.service.events().delete(
            calendarId="primary",
            eventId=event["id"]
        ).execute()

        return True

    # --------------------------------------------------
    # Free Slots
    # --------------------------------------------------

    def find_free_slots(
        self,
        when: str = "today",
        duration_minutes: int = 60
    ):

        date = self.parse_datetime(
            when
        )

        start_day = date.replace(
            hour=9,
            minute=0,
            second=0,
            microsecond=0
        )

        end_day = date.replace(
            hour=18,
            minute=0,
            second=0,
            microsecond=0
        )

        events = self.list_events(
            start_day,
            end_day
        )

        free_slots = []

        current = start_day

        for event in events:

            event_start = datetime.fromisoformat(
                event["start"]["dateTime"]
                .replace("Z", "")
            )

            event_end = datetime.fromisoformat(
                event["end"]["dateTime"]
                .replace("Z", "")
            )

            if (
                event_start - current
            ).total_seconds() >= duration_minutes * 60:

                free_slots.append(
                    (
                        current,
                        event_start
                    )
                )

            current = max(
                current,
                event_end
            )

        if (
            end_day - current
        ).total_seconds() >= duration_minutes * 60:

            free_slots.append(
                (
                    current,
                    end_day
                )
            )

        return free_slots