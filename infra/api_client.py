import requests
from datetime import datetime
from domain.clima import Clima
from main.config import API_KEY # pyright: ignore[reportMissingImports]



class OpenWeatherClient:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def buscar_clima(self, cidade: str) -> Clima:

        params = {
            "q": cidade,
            "appid": API_KEY,
            "units": "metric",
            "lang": "pt_br"
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 401:
            raise RuntimeError("API Key inválida.")

        response.raise_for_status()

        data = response.json()

        return Clima(
            cidade=data["name"],
            temperatura=data["main"]["temp"],
            sensacao_termica=data["main"]["feels_like"],
            condicao=data["weather"][0]["description"],
            data_coleta=datetime.now()
        )
