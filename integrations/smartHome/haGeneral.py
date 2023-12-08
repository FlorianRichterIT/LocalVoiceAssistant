from datetime import timedelta, datetime

import config
import requests

urlStart = "http://" + config.HOME_ASSISTANT_URL + "/api"

headers = {
    "Authorization": "Bearer " + config.HOME_ASSISTANT_TOKEN,
    "Content-Type": "application/json",
}


def get_API_state():
    url = urlStart + "/"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Lade den JSON-Inhalt der Antwort
        data = response.json()

        # Extrahiere den Wert des "message"-Schlüssels
        message_value = data.get("message")

        cleaned_message = message_value.rstrip(".")

        return cleaned_message

    return f"Fehler bei der Anfrage. Statuscode: {response.status_code}"


def get_config():
    url = urlStart + "/config"

    response = requests.get(url, headers=headers)

    return response.json()


def get_events():
    url = urlStart + "/events"

    response = requests.get(url, headers=headers)

    return response.json()


def get_services():
    url = urlStart + "/services"

    response = requests.get(url, headers=headers)

    return response.json()


def get_history(entity_id):
    url = urlStart + "/history/period?filter_entity_id=" + entity_id

    response = requests.get(url, headers=headers)

    return response.json()


def get_logbook(entity_id, start_date, end_date):
    if entity_id is not None and end_date is not None:
        url = f"{urlStart}/logbook/{start_date}?end_time={end_date}&entity={entity_id}"
    elif end_date is not None:
        url = f"{urlStart}/logbook/{start_date}?end_time={end_date}"
    else:
        url = f"{urlStart}/logbook/{start_date}"

    response = requests.get(url, headers=headers)

    return response.json()


def get_states():
    url = urlStart + "/states"

    response = requests.get(url, headers=headers)

    return response.json()


def get_states_of_entity(entity_id):
    url = urlStart + "/states/" + entity_id

    response = requests.get(url, headers=headers)

    return response.json()


def get_error_log():
    url = urlStart + "/error_log"

    response = requests.get(url, headers=headers)

    return response.json()


def get_camera_proxy(entity_id):
    url = urlStart + "/camera_proxy/" + entity_id + "?time=" + 1701994164851

    response = requests.get(url, headers=headers)

    return response.json()


"""
print(get_API_state())
print(get_config())
for event in get_events():
    print(f"Event: {event['event']}, Listener Count: {event['listener_count']}")
for each in get_services():
    print(each)
print(get_history) 

for each in get_logbook(
        "light.schreibtischlampe",
        (datetime.utcnow() + timedelta(days=-7)).isoformat(),
        datetime.utcnow()
):
    print(each)
    
print(get_states)
print(get_states_of_entity("light.schreibtischlampe"))
"""

print(get_error_log)
