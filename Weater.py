#!/usr/bin/env python3
import json
import requests

try:
    r = requests.get("https://wttr.in/?format=j1", timeout=5)
    weather = r.json()["current_condition"][0]
    code = weather["weatherCode"]

    icons = {
        "113": "☀️", "116": "⛅", "119": "☁️", "122": "☁️",
        "176": "🌧️", "200": "⛈️", "230": "🌨️", "248": "🌫️"
    }

    icon = icons.get(code, "❓")
    temp = weather["temp_C"]
    tooltip = f"{weather['weatherDesc'][0]['value']}\nFeels like: {weather['FeelsLikeC']}°C\nHumidity: {weather['humidity']}%\nWind: {weather['windspeedKmph']} km/h"

    print(json.dumps({
        "text": f"{icon} {temp}°C",
        "tooltip": tooltip
    }))

except Exception:
    print(json.dumps({
        "text": "⛅ --°C",
        "tooltip": "Weather unavailable"
    }))
    
