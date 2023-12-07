import config
import requests

url = config.HOME_ASSISTANT_URL
token = config.HOME_ASSISTANT_TOKEN

if url is None or token is None:
    print("ERROR: Umgebungsvariablen nicht gesetzt.")

# Prüfe, ob die Umgebungsvariablen den erwarteten Typ haben
elif not isinstance(url, str) or not isinstance(token, str):
    print("ERROR: Ungültige Werte für Umgebungsvariablen.")
    # Hier könntest du das Programm beenden oder anderweitig reagieren.

else:
    url = "http://" + url + "/api/calendars"

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)

    print(response.text)