import requests
from bs4 import BeautifulSoup
from datetime import datetime
from models import Clima

URL = "https://www.tempo.com/sao-paulo.htm"


def coletar_clima_scraping() -> Clima:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    temperatura_tag = soup.select_one(".dato-temperatura")
    condicao_tag = soup.select_one(".descripcion")

    if not temperatura_tag or not condicao_tag:
        raise RuntimeError("Não foi possível localizar os dados no site.")

    temperatura = float(temperatura_tag.text.replace("°", "").strip())
    condicao = condicao_tag.text.strip()

    return Clima(
        cidade="São Paulo",
        temperatura=temperatura,
        sensacao_termica=temperatura,  # aproximação simples
        condicao=condicao,
        data_coleta=datetime.now()
    )


if __name__ == "__main__":
    clima = coletar_clima_scraping()
    print(clima)
from csv_writer import salvar_csv

if __name__ == "__main__":
    clima = coletar_clima_scraping()
    salvar_csv(clima, "data/clima_scraping.csv")
    print("Arquivo clima_scraping.csv gerado com sucesso.")
