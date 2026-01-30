import csv
from models import Clima


def salvar_csv(clima: Clima, arquivo: str):
    with open(arquivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "cidade",
            "temperatura",
            "sensacao_termica",
            "condicao",
            "data_coleta"
        ])
        writer.writerow([
            clima.cidade,
            clima.temperatura,
            clima.sensacao_termica,
            clima.condicao,
            clima.data_coleta
        ])
