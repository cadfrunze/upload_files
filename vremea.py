from requests import Response, get
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY: str = os.getenv("api_key")
URL: str = "https://api.openweathermap.org/data/2.5/weather"

param: dict[str | str] = {
    "q": "Cluj-Napoca",
    "appid": API_KEY,
    "units": "metric",
    "lang": "ro"
}

data: Response = get(URL, params=param)
data.raise_for_status()
data: dict = data.json()
print(f"Description: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C")
