from models import Clima
from datetime import datetime

clima = Clima(
    cidade="São Paulo",
    temperatura=25.0,
    sensacao_termica=26.0,
    condicao="ensolarado",
    data_coleta=datetime.now()
)

print(clima)
