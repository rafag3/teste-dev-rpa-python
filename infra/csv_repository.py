import csv
from domain.clima import Clima


class ClimaCSVRepository:

    def salvar(self, clima: Clima, caminho: str):

        with open(caminho, "a", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                clima.cidade,
                clima.temperatura,
                clima.sensacao_termica,
                clima.condicao,
                clima.data_coleta.isoformat()
            ])
