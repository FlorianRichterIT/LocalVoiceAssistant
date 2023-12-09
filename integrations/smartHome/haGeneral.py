import string
from datetime import timedelta, datetime, timezone, time

import config
import requests

urlStart = "http://" + config.HOME_ASSISTANT_URL + "/api"

headers = {
    "Authorization": "Bearer " + config.HOME_ASSISTANT_TOKEN,
    "Content-Type": "application/json",
}


def is_API_running():
    url = urlStart + "/"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Lade den JSON-Inhalt der Antwort
        data = response.json()

        # Extrahiere den Wert des "message"-Schlüssels
        message_value = data.get("message")

        if message_value == "API running.":
            return True
        else:
            return False

    return False


def get_config():
    url = urlStart + "/config"

    response = requests.get(url, headers=headers)

    map = dict()

    for key, value in response.json().items():
        map.update({key: value})

    return map


def get_events():
    url = urlStart + "/events"

    response = requests.get(url, headers=headers)

    return response.json()


def get_services():
    url = urlStart + "/services"

    response = requests.get(url, headers=headers)

    map = dict()

    for eachService in response.json():
        map.update({eachService.get("domain"): eachService})

    return map


def get_history_past_day(entity_id):
    url = urlStart + "/history/period?filter_entity_id=" + entity_id

    response = requests.get(url, headers=headers)

    """config_map = dict()

    for each in response.json():
        for entry in each:
            last_changed = entry.get("last_changed")
            config_map.update({last_changed: entry})"""

    return response.json()


def get_history_with_date(entity_id, start_date):
    url = urlStart + "/history/period/" + start_date + "?filter_entity_id=" + entity_id

    response = requests.get(url, headers=headers)

    return response.json()


def get_history_with_date_range(entity_id, start_date, end_date):
    url = urlStart + "/history/period/" + start_date + "?end_time=" + end_date + "&filter_entity_id=" + entity_id

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


def get_all_states():
    url = urlStart + "/states"

    response = requests.get(url, headers=headers)

    config_map = dict()

    for each in response.json():
        eachEntityId = each.get("entity_id")
        each.pop("entity_id")
        config_map.update({eachEntityId: each})

    return config_map


def get_states_of_entity(entity_id):
    url = urlStart + "/states/" + entity_id

    response = requests.get(url, headers=headers)

    config_map = dict()

    for key in response.json():
        config_map.update({key: response.json()[key]})

    return config_map


def get_error_log():
    url = urlStart + "/error_log"

    response = requests.get(url, headers=headers)

    return response.json


def get_camera_proxy(entity_id):
    url = urlStart + "/camera_proxy/" + entity_id + "?time=" + 1701994164851

    response = requests.get(url, headers=headers)

    return response.json()


config_map = get_history_past_day("light.schreibtischlampe")

for each in config_map:
    for entry in each:
        print(entry)
        print(datetime.fromisoformat(entry.get("last_changed")).time())
