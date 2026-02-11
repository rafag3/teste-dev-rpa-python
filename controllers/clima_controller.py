class ClimaController:

    def __init__(self, service):
        self.service = service

    def executar(self, cidade: str):

        caminho = "data/clima.csv"

        clima = self.service.coletar_e_salvar(
            cidade,
            caminho
        )

        print("Coleta realizada com sucesso!")
        print(clima)
