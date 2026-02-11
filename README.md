# Teste Técnico – Dev RPA (Python)

Este projeto foi desenvolvido como parte de um teste técnico para a vaga de **Desenvolvedor RPA**  por **Rafael Nascimento** com o objetivo de demonstrar coleta de dados utilizando **duas abordagens diferentes**:

1. **Web Scraping**
2. **Consumo de API pública**

Em ambos os casos, os dados coletados são normalizados no mesmo formato e salvos em arquivos **CSV**.

-------------------------------------------------------

## Objetivo

Coletar dados de clima da cidade de **São Paulo** utilizando:
- Um site público (via scraping)
- Uma API pública (OpenWeatherMap)

E gerar arquivos CSV organizados com as seguintes informações:
- Cidade
- Temperatura
- Sensação térmica
- Condição climática
- Data/hora da coleta

---

## Tecnologias utilizadas

- Python 3
- requests
- beautifulsoup4
- CSV (biblioteca padrão do Python)

---

## Arquitetura

Projeto estruturado em camadas:

- domain: regras de negócio
- infra: integração externa (API / CSV)
- services: casos de uso
- controllers: interface
- main: ponto de entrada

Inspirado em MVC / Clean Architecture.
