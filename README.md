# Projeto Forecast Finanças com Streamlit e Python

Este é um aplicativo de previsão de ações desenvolvido em Python. O aplicativo permite que você informe um ticker de ação no formato do yahoofinance (por exemplo, AAPL para Apple, MSFT para Microsoft, e nas brasileiras acrescentar o .SA por exemplo MGLU3.SA, PETR4.SA) e visualize tabelas e gráficos relacionados à ação, além de gerar previsões de preços futuros utilizando o modelo Prophet.

## Funcionalidades

- **Input de Ticker de Ação**: Informe o ticker da ação que deseja analisar.
- **Slider da quantidade de dias de previsão**: Informe a quantidade de dias que deseja realizar a previsão.
- **Exibição de Tabelas**: Dados históricos do preço da ação extraídos da API do Yahoo Finance.
- **Gráficos Interativos**: Gráficos de preços e tendências da ação, com suporte interativo fornecido pelo Plotly.
- **Previsão de Preços**: Previsão dos preços futuros da ação utilizando o modelo Prophet.
  
## Bibliotecas Utilizadas

### 1. [Pandas](https://pandas.pydata.org/)
Pandas é uma biblioteca fundamental para análise de dados em Python. Ela permite a manipulação de dados em estruturas como DataFrames, facilitando a leitura, processamento e transformação dos dados históricos de ações.

### 2. [Prophet](https://facebook.github.io/prophet/)
Prophet é uma ferramenta de modelagem de séries temporais desenvolvida pelo Facebook, que facilita a previsão de dados com tendências sazonais. No aplicativo, usamos o Prophet para prever o preço futuro da ação com base em dados históricos.

### 3. [yfinance](https://pypi.org/project/yfinance/)
YFinance é uma API que permite acessar dados financeiros do Yahoo Finance. Utilizamos essa biblioteca para buscar os dados históricos das ações, incluindo preços de abertura, fechamento, volume, etc.

### 4. [Plotly](https://plotly.com/)
Plotly é uma biblioteca que fornece gráficos interativos para o Python. Com ela, criamos gráficos de séries temporais dos preços históricos e também os gráficos da previsão gerada pelo Prophet.

### 5. [Streamlit](https://streamlit.io/)
Streamlit é uma biblioteca que facilita a criação de aplicativos web interativos para análise de dados em Python. Utilizamos o Streamlit para construir a interface do aplicativo, onde o usuário pode inserir o ticker da ação e visualizar os resultados.

## Instalação e Execução

### Pré-requisitos

- Python 3.8 ou superior.
- [Poetry](https://python-poetry.org/) instalado para gerenciamento de dependências.

### Passos para Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/stock-forecast-app.git
    cd stock-forecast-app
    ```

2. Instale as dependências usando o Poetry:
    ```bash
    poetry install
    ```

3. Ative o ambiente virtual criado pelo Poetry:
    ```bash
    poetry shell
    ```

4. Execute o aplicativo:
    ```bash
    streamlit run app.py
    ```

## Como Usar

1. No campo de input, insira o ticker da ação localizado no yahoo-finance (https://finance.yahoo.com/) (por exemplo, AAPL, MSFT, GOOG, MGLU3.SA, PTR4.SA).
2. O aplicativo exibirá uma tabela com os dados históricos da ação.
3. Veja os gráficos interativos dos preços da ação.
4. A previsão de preços futuros será exibida em forma de tabela e gráficos.

## Estrutura do Projeto

```plaintext
stock-forecast-app/
│
├── app.py           # Arquivo principal do aplicativo Streamlit
├── README.md        # Instruções de uso
├── pyproject.toml   # Arquivo de configuração do Poetry
└── poetry.lock      # Outros arquivos e diretórios
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
