class ClimaService:

    def __init__(self, api_client, repository):
        self.api_client = api_client
        self.repository = repository

    def coletar_e_salvar(self, cidade: str, caminho: str):

        clima = self.api_client.buscar_clima(cidade)

        self.repository.salvar(clima, caminho)

        return clima
