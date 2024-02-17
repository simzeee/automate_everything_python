import requests


def get_weather(city, units="metrics", api_key="26631f0f41b95fb9f5ac0df9a8f43c92"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    r = requests.get(url)
    content = r.json()
    with open("data.tx", "a") as file:
        for dicty in content["list"]:
            file.write(
                f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n"
            )


print(get_weather(city="Washington"))
