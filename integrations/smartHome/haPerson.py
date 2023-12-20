from datetime import timedelta, datetime, timezone, time

import config
import requests
from math import radians, sin, cos, sqrt, atan2

urlStart = "http://" + config.HOME_ASSISTANT_URL + "/api"

headers = {
    "Authorization": "Bearer " + config.HOME_ASSISTANT_TOKEN,
    "Content-Type": "application/json",
}


def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius der Erde in Kilometern
    R = 6371.0

    # Umrechnung der Breiten- und Längengrade von Grad in Radian
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Deltas der Breiten- und Längengrade
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine-Formel
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Entfernung in Kilometern
    distance = R * c

    return distance



def get_all_informations_for_all_persons():
    url = urlStart + "/states"

    response = requests.get(url, headers=headers)

    config_map = dict()

    for each in response.json():
        if each.get("entity_id").startswith("person."):
            eachEntityId = each.get("entity_id")
            each.pop("entity_id")

            if each.get("attributes").get("latitude") is not None:
                config_map.update({eachEntityId: each})

    return config_map


def get_all_persons_locations():
    url = urlStart + "/states"

    response = requests.get(url, headers=headers)

    config_list = []

    for each in response.json():
        if each.get("entity_id").startswith("person."):
            eachEntityId = each.get("entity_id")

            if each.get("attributes").get("latitude") is not None:
                config_map = {
                    "Entity ID": eachEntityId,
                    "Last Changed": each.get("last_changed"),
                    "State": each.get("state"),
                    "Latitude": each.get("attributes").get("latitude"),
                    "Longitude": each.get("attributes").get("longitude")
                }
                config_list.append(config_map)

    return config_list


def get_person_location(entity_id):
    url = urlStart + "/states/" + entity_id

    response = requests.get(url, headers=headers)

    config_list = []

    if response.json().get("attributes").get("latitude") is not None:
        config_map = {
            "Entity ID": entity_id,
            "Last Changed": response.json().get("last_changed"),
            "State": response.json().get("state"),
            "Latitude": response.json().get("attributes").get("latitude"),
            "Longitude": response.json().get("attributes").get("longitude")
        }
        config_list.append(config_map)

    return config_list


def get_distance_from_home(entity_id):
    home_latitude = 49.554908752441406
    home_longitude = 8.653414726257324

    location = get_person_location(entity_id)
    if location is None:
        return None
    elif location[0].get("State") == "home":
        return 0.0
    else:
        return haversine_distance(home_latitude, home_longitude, location[0].get("Latitude"), location[0].get("Longitude"))


def get_person_logbook(entity_id, start_date, end_date):
    if entity_id is not None and end_date is not None:
        url = f"{urlStart}/logbook/{start_date}?end_time={end_date}&entity={entity_id}"
    elif end_date is not None:
        url = f"{urlStart}/logbook/{start_date}?end_time={end_date}"
    else:
        url = f"{urlStart}/logbook/{start_date}"

    response = requests.get(url, headers=headers)

    return response.json()


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


print(get_distance_from_home("person.ralf"))


# person.ralf
