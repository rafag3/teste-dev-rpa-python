from dataclasses import dataclass
from datetime import datetime

@dataclass
class Clima:
    cidade: str
    temperatura: float
    sensacao_termica: float
    condicao: str
    data_coleta: datetime
