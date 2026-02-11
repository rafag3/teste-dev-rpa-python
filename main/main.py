from infra.api_client import OpenWeatherClient
from infra.csv_repository import ClimaCSVRepository
from services.clima_service import ClimaService
from controllers.clima_controller import ClimaController


def main():

    api_client = OpenWeatherClient()
    repository = ClimaCSVRepository()

    service = ClimaService(api_client, repository)
    controller = ClimaController(service)

    controller.executar("São Paulo")


if __name__ == "__main__":
    main()
