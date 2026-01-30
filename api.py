import requests
from datetime import datetime
from models import Clima

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "6de440b8cd0a227284a2323ae3d75062"  #API pessoa, por isto não compartilhada.


def coletar_clima_api(cidade: str) -> Clima:
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(API_URL, params=params, timeout=10)

    if response.status_code == 401:
        raise RuntimeError("API key inválida ou ainda não ativada.")

    response.raise_for_status()
    data = response.json()

    return Clima(
        cidade=data["name"],
        temperatura=data["main"]["temp"],
        sensacao_termica=data["main"]["feels_like"],
        condicao=data["weather"][0]["description"],
        data_coleta=datetime.now()
    )


if __name__ == "__main__":
    from csv_writer import salvar_csv

    clima = coletar_clima_api("São Paulo")
    salvar_csv(clima, "data/clima_api.csv")
    print("Arquivo clima_api.csv gerado com sucesso.")
