import config
import requests
from datetime import datetime, timedelta

urlStart = "http://" + config.HOME_ASSISTANT_URL

headers = {
    "Authorization": "Bearer " + config.HOME_ASSISTANT_TOKEN,
    "Content-Type": "application/json",
}


def get_calendars():
    url = urlStart + "/api/calendars"

    response = requests.get(url, headers=headers)

    return response.text


def get_calendar_events(calendar_name):
    current_date = datetime.utcnow().isoformat() + "Z"

    seven_days_from_now = datetime.utcnow() + timedelta(days=7)
    seven_days_from_now = seven_days_from_now.isoformat() + "Z"

    # Füge das aktuelle Datum als Parameter zum API-Aufruf hinzu
    url = f"{urlStart}/api/calendars/{calendar_name}?start={current_date}&end={seven_days_from_now}"
    response = requests.get(url, headers=headers)

    return response.text


print(get_calendars())
print(get_calendar_events("calendar.arbeit"))